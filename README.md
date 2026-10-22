# Retail Revenue & Profit Intelligence — Sumit Gole

**Portfolio status:** Reproducible synthetic-data analytics project with a dashboard-style PDF. **The existing PBIX is a legacy/reference report and does NOT yet implement the synthetic-data dashboard shown in the PDF.**

## What is in this repository?

| File | Purpose | Status |
|---|---|---|
| `Sumit_Gole_Retail_Intelligence_Dashboard.pdf` | Two-page static dashboard generated from synthetic retail data | Available; not a PBIX export |
| `Sumit_Gole_Retail_Store_Analysis.pbix` | Existing, separately sourced Retail Store Analysis report with renamed page labels | Legacy/reference; **not matched to PDF**; Power BI Desktop validation pending |
| `generate_dataset.py` | Deterministically generates 1,200 synthetic transactions | Reproducible; Python standard library |
| `sumit_retail_sales.csv` | Synthetic source data | Generate locally with `python generate_dataset.py`; not checked in |
| `DAX_measures.txt` | Proposed measures for **new** `RetailSales` table | Not verified inside legacy PBIX |
| `theme.json` | Optional midnight-teal report theme | Not verified as applied to legacy PBIX |
| `BUILD_GUIDE.md` | Instructions to build the matching report in Power BI Desktop | Available |

## Reproduce the PDF data

Run `python generate_dataset.py`. The generated CSV has 1,200 rows, 13 columns and covers 2024–2025. Expected aggregates:

| Metric | Expected value |
|---|---:|
| Net sales | INR 15,099,553.95 |
| Profit | INR 3,819,871.35 |
| Units sold | 4,790 |
| Distinct orders | 1,200 |
| Distinct customers | 360 |

The dashboard PDF uses these synthetic figures; they do **not** establish the values inside the legacy PBIX.

## Build the matching interactive dashboard

Follow [BUILD_GUIDE.md](BUILD_GUIDE.md) to import the generated CSV, create the DAX measures, build the report pages and save a **new** `Sumit_Gole_Retail_Intelligence.pbix`. Only after opening, refreshing and validating that new report in Power BI Desktop should its pages be exported as a matching PDF.

## Attribution and limitations

Project branding and synthetic analysis: **Sumit Gole**. Original reference material and an existing PBIX were supplied separately; changing page labels does not establish original authorship of the underlying PBIX design. General inspiration: [PowerBI-Project](https://github.com/sachinkumar1609/PowerBI-Project).

**Do not describe the PDF as an export of the current PBIX or claim the current PBIX has been validated.**
