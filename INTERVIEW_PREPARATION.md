# Interview Preparation — Retail Revenue & Profit Intelligence

Use these answers only for work actually completed. Do not claim the final interactive Power BI report is built or published until you have validated it.

## 1. What problem does the project solve?
It organizes retail transactions into sales, profit, cost, customer, product, regional and channel metrics so a business user can understand performance and compare segments.

## 2. Where did the data come from?
A deterministic Python script generates synthetic transactions. It is not a real retailer's production dataset.

## 3. What is the grain of the dataset?
One row per generated order transaction. The generator creates a unique OrderID for each row; this simplified dataset does not model multiple line items per order.

## 4. How do you calculate sales?
NetSales is Quantity multiplied by UnitPrice after DiscountRate. The CSV stores this precomputed amount.

## 5. How is profit calculated?
Profit = NetSales − Cost. The validator checks this row by row.

## 6. What is the difference between profit and profit margin?
Profit is an absolute currency amount; Profit Margin % = Total Profit / Total Sales. For this dataset the margin is approximately 25.30%.

## 7. Why use DAX measures instead of calculated columns?
Measures aggregate dynamically in the current filter context, which is appropriate for KPIs, category comparisons and slicer-driven reports.

## 8. Why create a Calendar table?
A dedicated date table supports year/month grouping and time-intelligence functions such as SAMEPERIODLASTYEAR. The relationship should link Calendar[Date] to RetailSales[OrderDate].

## 9. How do you validate the data?
The script verifies 1,200 records, required schema, unique order IDs, sales arithmetic and profit arithmetic; it then prints aggregate totals to compare against the report.

## 10. What are the verified headline results?
Sales INR 15,099,553.95; profit INR 3,819,871.35; cost INR 11,279,682.60; 1,200 orders; 360 customers; 4,790 units; margin 25.30%. These are synthetic-data metrics.

## 11. What would you improve next?
Build a fresh Power BI report from the validated CSV, test measures and slicers, compare KPI totals, export the PDF from the same report, and publish only if account permissions allow.

## 12. What is currently incomplete?
The legacy PBIX is separate from the static PDF and has not been validated as a matching implementation. Be transparent about this distinction.

## Suggested concise project pitch
“I developed a reproducible retail analytics project using Python-generated synthetic transactions, data validation and a Power BI reporting specification. The dataset covers 1,200 orders and supports revenue, cost, profit, margin, customer and category analysis. I also documented the DAX measures and dashboard design. The final interactive Power BI implementation is a separate completion step.”
