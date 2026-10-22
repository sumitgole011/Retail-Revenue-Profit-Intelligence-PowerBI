# Build and validate the Power BI dashboard — Sumit Gole

## 1. Generate and verify data
Run `python generate_dataset.py`, then `python validate_dataset.py`. Confirm 1,200 rows, the required 13 fields, unique order IDs, and no arithmetic inconsistencies. **Use the totals printed by the validator as the source of truth**, not the values in the static PDF.

## 2. Import and model
In Power BI Desktop use **Get Data > Text/CSV** and select `sumit_retail_sales.csv`. Name the table `RetailSales`. Set `OrderDate` to Date, `Quantity` to Whole Number and monetary fields to Decimal Number. Format `DiscountRate` as Percentage.

Create the `Calendar` calculated table in `DAX_measures.txt` using **Modeling > New table**. Mark it as a date table and create a one-to-many relationship from `Calendar[Date]` to `RetailSales[OrderDate]`. Create the other DAX definitions one at a time using **New measure**. Sort `Calendar[Month]` by `Calendar[MonthNo]`; sort `YearMonth` chronologically.

## 3. Build the planned pages
**Page 1 — Executive Overview:** cards for Total Sales, Total Profit, Units Sold and Profit Margin %; monthly sales column chart; category sales donut; region sales bar chart; channel sales donut; top products by sales.

**Page 2 — Profitability Deep Dive:** category profit donut; category profit margin bar chart; cards for Total Orders, Distinct Customers, Average Order Value and Total Cost.

Import `theme.json` via View > Themes > Browse for themes. Add Year, Region, Category and Channel slicers. Verify cross-filter behavior.

## 4. Reconcile numbers
With all slicers cleared, compare the Power BI cards to `python validate_dataset.py` output. Confirm that `Total Sales` equals the CSV sum of `NetSales`, `Total Profit` equals sum of `Profit`, `Units Sold` equals sum of `Quantity`, `Total Orders` equals unique OrderID count, and `Distinct Customers` equals unique CustomerID count. Profit margin should equal profit divided by sales. **The existing static PDF may display different numbers; do not treat it as a verified export.**

## 5. Save and export
Save as `Sumit_Gole_Retail_Intelligence.pbix`. Reopen and refresh the saved file, confirm slicers and KPIs, and export a fresh PDF from Power BI Desktop. Replace the static dashboard PDF only after the visuals and values match.

## Current limitation
`Sumit_Gole_Retail_Store_Analysis.pbix` is a separate legacy/reference report, not the implementation of this guide. The new PBIX has not been built or tested in Power BI Desktop.
