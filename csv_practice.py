import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("--- Exercise 2 ---")

with open (SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("--- Exercise 3 ---")
with open(SALES_FILE, "r") as f:
    reader= csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

print(" --- Exercise 4---")

total_revenue = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("--- Exercise 5---")

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)

        total = price * quantity

        if total > 100:
            high_value.append([product, price, quantity, total])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value)

print(f"Wrote {len(high_value)} rows out of {rows_read}")

print( "--- Exercise 6---")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader (f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x {price:.2f} = ${total:.2f}")

# csv.reader accesses values by their numerical position.
# DictReader accesses values by column name, making code easier to read.


print(" --- Exercise 7 ----")

summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])

        summary[product] = summary.get(product, 0) + total

for product in sorted(summary.keys()):
    print(f"{product}: ${summary[product]:.2f}")

print("--- Exercise 8---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} | Total Revenue: ${total_revenue:.2f}\n")

print("Log entry added!")

# Self assesment questions 

# 1. Python and Excel can both read, organize, and calculate data, but they approach the process differently. Excel makes it easier to view data, create charts, and perform calculations visually. Python is better for automating repetitive tasks, processing large amounts of data, and handling multiple files at once. Python can also repeat the same ETL process without requiring someone to manually perform each step.

# 2. A business that could benefit from an append-mode log file is an online store tracking customer orders. Every time an order is processed, the program could add the date, time, and order total to a log file. Append mode is useful because it adds new information without deleting previous records. This allows the business to keep a history of transactions and review past activity.

