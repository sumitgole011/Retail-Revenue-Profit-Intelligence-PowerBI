# Retail Revenue & Profit Intelligence — Portfolio Case Study

**Project owner:** Sumit Gole  
**Project type:** Retail business intelligence / synthetic-data demonstration  
**Status:** Dataset generator and validator ready; static dashboard concept available; matching interactive Power BI report pending independent completion.

## Business context
Retail managers need a clear view of revenue, cost and profit across categories, regions, products and channels. This project demonstrates how a transactional dataset can support those decisions.

## Questions addressed
1. How much revenue and profit does the retailer generate?
2. Which categories and products contribute the most sales?
3. How do regions and channels compare?
4. Which categories offer stronger profit margins?
5. How do sales and profit change over time?

## Dataset and approach
The project generates 1,200 **synthetic** order transactions dated across 2024–2025. Each row includes order, customer, product, geography, channel, quantity, unit price, discount, net sales, cost and profit. A Python validator checks required columns, unique order IDs and row-level financial arithmetic.

### Verified baseline (generated CSV)
| KPI | Value |
|---|---:|
| Total sales | INR 15,099,553.95 |
| Total profit | INR 3,819,871.35 |
| Total cost | INR 11,279,682.60 |
| Orders | 1,200 |
| Distinct customers | 360 |
| Units sold | 4,790 |
| Profit margin | 25.30% |

These are synthetic-data aggregates, **not real business results**.

## Analytics design
The planned interactive report uses a calendar relationship and DAX for Total Sales, Total Profit, Total Cost, Profit Margin, Average Order Value, Distinct Customers and year-over-year comparisons. The two-page concept separates executive performance from profitability diagnostics.

## How to reproduce
Run:
```bash
python3 generate_dataset.py
python3 validate_dataset.py
```
Then follow [BUILD_GUIDE.md](BUILD_GUIDE.md) to build a new Power BI report.

## Responsible interpretation
The numbers above are descriptive metrics from generated data. They do not prove actual retail growth, operational performance or commercial outcomes. A category ranking or time-series conclusion must be calculated from the generated CSV or final Power BI report, not inferred from the static PDF.

## Current limitations
- Existing `Sumit_Gole_Retail_Store_Analysis.pbix` is a legacy/reference report and is **not matched** to the synthetic dataset or static dashboard PDF.
- No interactive report link, verified PBIX export or independently tested DAX implementation is claimed here.
- PDF figures have not been reconciled to a newly built Power BI report.

## Portfolio value
Demonstrates a reproducible analytics workflow: synthetic data generation, financial KPI definition, data-quality validation, report specification, and technical documentation. Interactive report implementation remains the next milestone.
