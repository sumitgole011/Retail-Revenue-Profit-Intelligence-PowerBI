# Build and validate the matching Power BI dashboard — Sumit Gole

## 1. Prepare reproducible data
Run `python generate_dataset.py` in this repository. Confirm `sumit_retail_sales.csv` has **1,200 records and 13 columns**. Data is synthetic, not a real company's sales.

## 2. Import and model
In Power BI Desktop: **Get Data > Text/CSV** > `sumit_retail_sales.csv`. Name the table `RetailSales`. Set `OrderDate` to Date, `Quantity` to Whole Number, and `UnitPrice`, `DiscountRate`, `NetSales`, `Cost`, `Profit` to Decimal Number. Format `DiscountRate` as percentage.

Create the `Calendar` calculated table from `DAX_measures.txt` using **Modeling > New table**. Mark it as a date table, and relate `Calendar[Date]` (one) to `RetailSales[OrderDate]` (many). Create each measure from the DAX file separately using **New measure**.

## 3. Build report pages matching the PDF
**Page 1 — Executive Overview:** cards for Total Sales, Total Profit, Units Sold and Profit Margin %; monthly NetSales bar chart; Category sales donut; Region sales horizontal bars; Channel sales donut; Top 5 Products sales bars.

**Page 2 — Profitability Deep Dive:** Category profit donut, Category Profit Margin % bar chart, and cards for Total Orders, Distinct Customers, Average Order Value and Total Cost.

Import `theme.json` from View > Themes > Browse for themes. Add date/region/category slicers if useful. The supplied PDF is a **static conceptual dashboard**, not an interactive PBIX export.

## 4. Verify totals
With all filters cleared, verify:
- Total Sales = **15,099,553.95**
- Total Profit = **3,819,871.35**
- Units Sold = **4,790**
- Total Orders = **1,200**
- Distinct Customers = **360**
- Profit Margin % = approximately **25.30%**

## 5. Save and export
Save the new report as `Sumit_Gole_Retail_Intelligence.pbix`, **not** `Sumit_Gole_Retail_Store_Analysis.pbix` (the latter is a separate legacy/reference report). Open the saved file again, refresh data, test slicers and verify totals. Then use File > Export > Export to PDF. Replace the static PDF only after confirming the new export reflects the same visuals and data.

## Current limitation
The new matching PBIX has **not** been built or validated in Power BI Desktop. The existing PBIX cannot be considered an implementation of this guide. Do not present it as such.
