# sec_files
#### Transforms / prepares financial statement data from the Securities and Exchange Commission (SEC.gov) for machine learning
---

**DATA** (json files ~1.1G and ~1.2G respectively)
- recent filings: https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip      
- financial numbers: https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip      

**SEC** Website: https://www.sec.gov/edgar/sec-api-documentation
- contains more information on the data
- same links as above are located at bottom of webpage as of 2023-05

---
### Brief Description
#### Part I (assembles-data.ipynb)
1. finds all filings for annual financial statements (identified as 10-K) from `submissions` folder
2. pulls financial numbers for those filings (identifed using accn) from `companyfacts` and writes them to `assembled-data` 

#### Part II (company-csv.ipynb)
1. writes csv files that contain all financial statements for a single company to `company-fin-sets`

#### Part III (yearly-csv.ipynb)
1. creates a `master.csv` that combines all financial statements from `company-fin-sets`
2. seperates financial statements in `master.csv` by year and writes them into `yearly-fin-sets`

---
### Notes
- some files / folders are too large and have been added as zip files
- the `samples` folder contains a singular file from certain folders `(submissions`, `companyfacts`, `company-fin-sets`, `yearly-fin-sets`)
