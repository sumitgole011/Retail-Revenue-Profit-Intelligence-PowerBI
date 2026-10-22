# Power BI build guide — Sumit Gole

1. Import `sumit_retail_sales.csv` in Power BI Desktop using Get Data > Text/CSV (rename the starter CSV accordingly).
2. Set OrderDate to Date, monetary columns to Decimal Number, and name the loaded table `RetailSales`.
3. Create the Calendar table from `DAX_measures.txt` and relate Calendar[Date] to RetailSales[OrderDate].
4. Add measures one at a time and format currency and percentage fields.
5. Import `theme.json` using View > Themes.
6. Build Executive Pulse, Product & Margin Lab, and Regional & Customer Lens pages.
7. Add Year, Region, Category and Channel slicers; test filters.
8. Save as `Sumit_Gole_Retail_Intelligence.pbix`.

**Status:** A functioning PBIX is not yet included. Synthetic demo data only.

General inspiration: https://github.com/sachinkumar1609/PowerBI-Project
