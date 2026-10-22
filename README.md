# Retail Revenue & Profit Intelligence
### Power BI portfolio project by Sumit Gole

Explore retail revenue, profitability, product mix, sales channels and regional performance through a **synthetic retail dataset**, reusable DAX measures and a two-page dashboard design.

> **Project maturity:** Data generator, documentation, visual reference PDF and an earlier/reference PBIX are included. The existing PBIX is **not** the interactive implementation of the synthetic-data PDF. A new matching PBIX still needs to be built and validated in Power BI Desktop.

## Business problem
A retailer needs to understand where revenue comes from, which categories contribute to profit, how regional and channel performance differs, and whether sales growth translates into margin. This project lays out an analytical reporting workflow for those questions using demonstration data.

## Tools and techniques
- **Power BI Desktop:** data modeling, relationships, report pages, slicers and visuals (implementation instructions)
- **DAX:** revenue, profit, margin, order value, customer count and year-over-year measures (proposed definitions)
- **Python 3:** deterministic synthetic transaction generator, standard library only
- **CSV:** transparent, inspectable source for the planned interactive report
- **JSON:** optional custom Midnight Teal report theme

## Project workflow
```text
generate_dataset.py
       |
       v
sumit_retail_sales.csv  [generated locally]
       |
       v
Power BI Desktop > Power Query > RetailSales
       |
       v
Calendar relationship + DAX measures
       |
       v
Executive Overview / Profitability Deep Dive
       |
       v
New validated PBIX > PDF export
```

## Planned report pages
**Executive Overview:** total sales, total profit, units sold, profit margin, monthly revenue trend, category contribution, regional breakdown, channel split and top products.

**Profitability Deep Dive:** category profit contribution, margin comparison, total orders, distinct customers, average order value and cost.

The [dashboard PDF](Sumit_Gole_Retail_Intelligence_Dashboard.pdf) is a **static design/reference**, not an export of the existing PBIX. Values displayed in that PDF have **not been reconciled against the current generator output**.

## Repository contents

| File | Description |
|---|---|
| [generate_dataset.py](generate_dataset.py) | Reproducible synthetic data generator; creates 1,200 rows |
| [validate_dataset.py](validate_dataset.py) | Validates CSV schema, arithmetic and prints actual KPI totals |
| [DAX_measures.txt](DAX_measures.txt) | Proposed DAX for the generated CSV |
| [theme.json](theme.json) | Optional Midnight Teal theme |
| [BUILD_GUIDE.md](BUILD_GUIDE.md) | Steps to build and test a matching interactive dashboard |
| [Sumit_Gole_Retail_Intelligence_Dashboard.pdf](Sumit_Gole_Retail_Intelligence_Dashboard.pdf) | Static two-page dashboard reference |
| [Sumit_Gole_Retail_Store_Analysis.pbix](Sumit_Gole_Retail_Store_Analysis.pbix) | Separate legacy/reference report; **not aligned to the PDF** |

## Run locally
1. Install **Python 3** and **Power BI Desktop** (Windows).
2. Clone this repository and run:
   ```bash
   python generate_dataset.py
   python validate_dataset.py
   ```
3. Import the generated `sumit_retail_sales.csv` into Power BI Desktop and follow [BUILD_GUIDE.md](BUILD_GUIDE.md).
4. Build and save a **new** `Sumit_Gole_Retail_Intelligence.pbix`. Reopen, refresh, validate its KPIs and export the final report to PDF.

**CSV schema:** `OrderID`, `OrderDate`, `CustomerID`, `Region`, `Category`, `Product`, `Quantity`, `UnitPrice`, `DiscountRate`, `NetSales`, `Cost`, `Profit`, `Channel`.

## Data quality and limitations
- Synthetic transactions; no real customer or company data.
- The generator creates 1,200 transactions with deterministic pseudo-random choices. Run the validator for **actual** totals; previously published PDF figures are not guaranteed to match.
- DAX measures are **not verified** in the legacy PBIX.
- The theme is **not confirmed** to be applied in the legacy PBIX.
- The legacy PBIX has **not** been functionally tested in Power BI Desktop.
- The PDF and legacy PBIX should **not** be presented as the same completed report.

## Ownership and inspiration
Synthetic-data workflow, documentation and project branding: **Sumit Gole**. The legacy PBIX was supplied as a reference and its underlying report design should not be represented as newly authored. General inspiration: [PowerBI-Project](https://github.com/sachinkumar1609/PowerBI-Project).

## Next milestone
Build and validate the new Power BI report using the generated CSV; export the PDF **from that report**, replace the static reference PDF, and then update this status.
