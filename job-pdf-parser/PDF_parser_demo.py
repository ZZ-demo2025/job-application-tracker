# -*- coding: utf-8 -*-

import os
import shutil
from PyPDF2 import PdfReader
import re
import pandas as pd
from datetime import datetime

curr_dir = os.path.dirname(__file__)
os.chdir(curr_dir)

input_dir = os.path.join(curr_dir, "sample_input")

# workday url matching pat
pat_url = r"https://(.+)\.wd[0-9]\.myworkdayjobs.com\S*/([^/\s]+)"

state_abbri = {"Florida": "FL",
               "Minnesota": "MN", 
               "Ohio": "OH",
               "FL": "FL", 
               "MN": "MN",
               "OH": "OH"}

def InfoParser(PdfDir):
    """
    parse job information from pdf and return structured data as dict.
    
    """
    reader = PdfReader(PdfDir)
    page = reader.pages[0]
    extracted_text = page.extract_text(Tj_sep='\n')
    
    #join broken words in pdf
    extracted_text = re.sub(r'([A-Za-z])\s+([a-z])', r"\1\2", extracted_text)
    
    #match workday url in footer
    url = re.search(pat_url, extracted_text, flags=re.MULTILINE)
    
    #match locations
    pat_state = "|".join(state_abbri)
    locations = re.findall(pat_state, extracted_text, flags=re.MULTILINE)
    
    #use file creation time as apply time
    apply_time = os.path.getmtime(PdfDir)
    apply_time = datetime.fromtimestamp(apply_time)

    try:
        company = url.group(1)
        position = url.group(2).split("_")
        
        pat_id = r"(.+[0-9])[\-\?]?.*"
        position_id = re.search(pat_id, position[1]).group(1)
        position = position[0]
    
        location = "\n".join(set(state_abbri[loc] for loc in locations))
        url = url.group(0)
    except:
        company = None
        position = None
        position_id = None
        location = None

    record = {"Job_id": position_id, 
              "Company": company,
              "Job_title": position,
              "location": location,
              "apply_time": apply_time,
              "url": url}
    
    return record

def RenamePdf(PdfDir, record):
    """
    rename pdf with job info. move and save it by company. 

    """
    try:
        new_name = f'{record["Job_id"]}_{record["Job_title"]}_{record["location"]}.pdf'

        new_path = os.path.join(curr_dir, f'sample_output_{record["Company"]}')
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        
        old_file_dir = os.path.join(curr_dir, PdfDir)
        new_file_dir = os.path.join(new_path, new_name)
        shutil.move(old_file_dir, new_file_dir)
    except:
        pass
    
if __name__ == "__main__":
    files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    
    records = []
    for f in files:
        f = os.path.join(input_dir, f)
        record  = InfoParser(f)
        records.append(record)
        RenamePdf(f, record)
        
    df = pd.DataFrame(records)
    df.to_excel("example_output.xlsx", index=False)