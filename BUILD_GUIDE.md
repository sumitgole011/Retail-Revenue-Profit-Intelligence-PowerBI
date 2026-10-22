# Power BI build guide

1. Open Power BI Desktop, select Get Data > Text/CSV and import `awanish_retail_sales.csv` from the companion starter ZIP.
2. In Power Query, set `OrderDate` to Date and monetary columns to Decimal Number; load the table as `RetailSales`.
3. Under Modeling, create the `Calendar` table from `DAX_measures.txt` and relate `Calendar[Date]` (one) to `RetailSales[OrderDate]` (many).
4. Create the DAX measures individually using Modeling > New measure. Format currency and percentages.
5. Import `theme.json` using View > Themes > Browse for themes.
6. Build three report pages:
   - Executive Pulse: KPI cards for Total Sales, Total Profit, Profit Margin %, Total Orders; monthly line chart by Calendar[YearMonth]; channel mix chart.
   - Product & Margin Lab: category sales/profit comparison, profit-margin ranking and discount breakdown.
   - Regional & Customer Lens: region sales/profit comparison, Distinct Customers and Average Order Value.
7. Add slicers for Year, Region, Category and Channel. Test filtering and cross-highlighting.
8. Save as `Awanish_Retail_Intelligence.pbix`. Export screenshots from the actual report once built.

**Project status:** This is a reproducible starter; a functioning .pbix has not been built or uploaded yet. The sample data is synthetic and the conceptual dashboard preview is not evidence of a finished Power BI report.

General inspiration: https://github.com/sachinkumar1609/PowerBI-Project
