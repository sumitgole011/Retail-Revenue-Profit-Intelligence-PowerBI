"""Generate the exact synthetic dataset used by the dashboard PDF.
Author: Sumit Gole. Python standard library only.
Run: python generate_dataset.py
"""
import csv
import datetime
import random
from pathlib import Path

random.seed(1609)
regions = ["North", "South", "East", "West"]
categories = {
    "Electronics": ["Headphones", "Smartwatch", "Keyboard", "Speaker"],
    "Home": ["Lamp", "Storage Box", "Desk Chair", "Coffee Maker"],
    "Fashion": ["Backpack", "Sneakers", "Jacket", "Wallet"],
    "Fitness": ["Yoga Mat", "Resistance Bands", "Dumbbells", "Bottle"],
}
headers = ["OrderID", "OrderDate", "CustomerID", "Region", "Category", "Product",
           "Quantity", "UnitPrice", "DiscountRate", "NetSales", "Cost", "Profit", "Channel"]
rows = []
for i in range(1, 1201):
    date = datetime.date(2024, 1, 1) + datetime.timedelta(days=random.randint(0, 729))
    region = random.choice(regions)
    category = random.choice(list(categories))
    product = random.choice(categories[category])
    quantity = random.randint(1, 7)
    unit_price = {
        "Electronics": random.randint(1000, 9000),
        "Home": random.randint(600, 7000),
        "Fashion": random.randint(500, 5500),
        "Fitness": random.randint(300, 4500),
    }[category]
    discount = random.choice([0, 0.05, 0.10, 0.15, 0.20])
    sales = round(quantity * unit_price * (1 - discount), 2)
    cost = round(quantity * unit_price * random.uniform(.52, .82), 2)
    profit = round(sales - cost, 2)
    rows.append([
        f"ORD-{i:05d}", date.isoformat(), f"C{random.randint(1, 380):04d}",
        region, category, product, quantity, unit_price, discount, sales,
        cost, profit, random.choice(["Online", "Retail", "Marketplace"])
    ])
output = Path(__file__).with_name("sumit_retail_sales.csv")
with output.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rows)
print(f"Created {output.name} with {len(rows)} synthetic transactions")
