# Job Application Tracker
A lightweight Python tool that extracts structured job metadata from PDF job descriptions (e.g., Workday exports), cleans messy text, and generates a standardized application tracking sheet.

## Features:
- Regex-based extraction of job title, company, location, job ID, and application time
- Cleans fragmented PDF text and normalizes structure
- Automatically renames and organizes files into company folders
- Produces an Excel tracking file for downstream analysis
- Sample documents taken from publicly available Workday job postings

## Tech stack
**Python · PyPDF2 · Pandas · Regex · File automation**

## Future Roadmap (depending on whether I get hired first)

#### Support for additional PDF formats
Handling variations across Workday, Linkedin, Company Career Sites, and other sites.

#### HTML scraper for active postings
Replace PDF parser for active postings, while PDF parser handles the expired ones.

#### Google Drive integration
Automatically generate permanent shareable links for stored job descriptions. Implemented in tracking sheet to click and access.

#### Gmail parsing for application updates
Read automated emails (interviews, rejections, status changes)  
- update tracking sheet  
- timestamp each change.

#### Resume version tracking
Track which resume variant was sent with each application.

#### Automated nightly batch processing
Package as a batch file → run via Task Scheduler → fully hands-free updates.

#### Power BI dashboard
Create BI dashboard to analyze tracking data and inform job-search strategy.

---

This roadmap reflects ongoing work and experiments as I continue refining my job-search workflow using automation and data tools.
