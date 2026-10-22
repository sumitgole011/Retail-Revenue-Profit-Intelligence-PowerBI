"""Validate generated synthetic retail CSV and print its actual KPIs.
Run after: python generate_dataset.py
"""
import csv
from collections import Counter
from decimal import Decimal
from pathlib import Path

path = Path(__file__).with_name("sumit_retail_sales.csv")
required = ["OrderID","OrderDate","CustomerID","Region","Category","Product",
            "Quantity","UnitPrice","DiscountRate","NetSales","Cost","Profit","Channel"]
with path.open(newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    assert reader.fieldnames == required, f"Unexpected CSV schema: {reader.fieldnames}"
    rows = list(reader)
assert len(rows) == 1200, f"Expected 1,200 transactions; got {len(rows)}"
ids = [row["OrderID"] for row in rows]
assert len(set(ids)) == len(ids), "Order IDs are not unique"
D = Decimal
for i, row in enumerate(rows, start=1):
    sales = D(row["NetSales"])
    cost = D(row["Cost"])
    profit = D(row["Profit"])
    assert abs(sales - cost - profit) <= D("0.01"), f"Profit mismatch in row {i}"
    expected = D(row["Quantity"]) * D(row["UnitPrice"]) * (D("1") - D(row["DiscountRate"]))
    assert abs(expected - sales) <= D("0.01"), f"NetSales mismatch in row {i}"
sales = sum((D(r["NetSales"]) for r in rows), D("0"))
profit = sum((D(r["Profit"]) for r in rows), D("0"))
cost = sum((D(r["Cost"]) for r in rows), D("0"))
units = sum(int(r["Quantity"]) for r in rows)
customers = len(set(r["CustomerID"] for r in rows))
print("PASS: 1,200 records; schema, unique orders and row arithmetic verified")
print(f"Net sales: INR {sales:,.2f}")
print(f"Profit: INR {profit:,.2f}")
print(f"Cost: INR {cost:,.2f}")
print(f"Units sold: {units:,}")
print(f"Orders: {len(ids):,}")
print(f"Distinct customers: {customers:,}")
print(f"Profit margin: {(profit / sales * 100 if sales else 0):.2f}%")
