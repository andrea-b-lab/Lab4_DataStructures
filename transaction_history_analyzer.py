# LAB 4: TRANSACTION HISTORY ANALYZER

# 1. STUDENT-SPECIFIC INPUTS
LAST_NAME = input("Enter your last name: ").strip().upper()
FAVORITE_ARTIST = input("Enter your favorite artist: ").strip().upper()

while not LAST_NAME or not FAVORITE_ARTIST:
    print("Please enter both inputs.")
    LAST_NAME = input("Enter your last name: ").strip().upper()
    FAVORITE_ARTIST = input("Enter your favorite artist: ").strip().upper()

while True:
    try:
        SEED_NUM = int(input("Enter your seed number: "))
        break
    except ValueError:
        print("Please enter a valid whole number.")

# 2. CUSTOMERS AND PRODUCTS
CUSTOMERS = [
    f"{LAST_NAME}_C{i}"
    for i in range(1, 6)
]

PRODUCTS = [
    "NOTEBOOK",
    "PEN",
    "USB",
    "HEADPHONES",
    "CALCULATOR"
]

# Sample fixed prices; replace if your instructor
# specified exact prices elsewhere in the handout.
PRICES = {
    "NOTEBOOK": 35.00,
    "PEN": 15.00,
    "USB": 250.00,
    "HEADPHONES": 350.00,
    "CALCULATOR": 180.00
}

# 3. GENERATE TRANSACTION RECORDS
transactions = []

for i, customer in enumerate(CUSTOMERS):
    for j, product in enumerate(PRODUCTS):
        artist_char = FAVORITE_ARTIST[
            (i + j) % len(FAVORITE_ARTIST)
        ]

        quantity = (
            ord(artist_char) + SEED_NUM + i + j
        ) % 10 + 1

        transaction = {
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "price": PRICES[product],
            "total": quantity * PRICES[product]
        }

        transactions.append(transaction)

# 4. ADD ONE REPEATED CUSTOMER-PRODUCT TRANSACTION
transactions.append(transactions[0].copy())

# 5. IDENTIFY REPEATED TRANSACTIONS
seen = set()
repeated_transactions = []

for transaction in transactions:
    key = (
        transaction["customer"],
        transaction["product"]
    )

    if key in seen:
        repeated_transactions.append(transaction)
    else:
        seen.add(key)

# 6. ORGANIZE TRANSACTIONS
organized_transactions = sorted(
    transactions,
    key=lambda t: (t["customer"], t["product"])
)

# 7. GENERATED TRANSACTION RECORDS
print("\n" + "=" * 95)
print("                 FINAL CONSOLIDATED TRANSACTION REPORT")
print("=" * 95)

print(f"Last Name: {LAST_NAME}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")
print(f"Seed Number: {SEED_NUM}")
print(f"Number of Transactions: {len(transactions)}")

print("\n1. GENERATED TRANSACTION RECORDS")
print("-" * 95)
print(
    f"{'CUSTOMER':<22}{'PRODUCT':<18}"
    f"{'QUANTITY':>10}{'PRICE':>15}{'TOTAL':>15}"
)

for t in transactions:
    print(
        f"{t['customer']:<22}"
        f"{t['product']:<18}"
        f"{t['quantity']:>10}"
        f"{t['price']:>15.2f}"
        f"{t['total']:>15.2f}"
    )

# 8. ORGANIZED TRANSACTION DATA
print("\n2. ORGANIZED TRANSACTION DATA")
print("-" * 95)

for t in organized_transactions:
    print(
        f"{t['customer']} | {t['product']} | "
        f"Qty: {t['quantity']} | "
        f"Price: {t['price']:.2f} | "
        f"Total: {t['total']:.2f}"
    )

# 9. REPEATED AND DISTINCT TRANSACTIONS
print("\n3. REPEATED CUSTOMER-PRODUCT TRANSACTIONS")
print("-" * 95)

if repeated_transactions:
    for t in repeated_transactions:
        print(
            f"{t['customer']} purchased {t['product']} "
            f"again | Qty: {t['quantity']} | "
            f"Total: {t['total']:.2f}"
        )
else:
    print("No repeated transactions.")

distinct_products = set(t["product"] for t in transactions)
distinct_customers = set(t["customer"] for t in transactions)

print(f"\nDistinct customers: {len(distinct_customers)}")
print(f"Distinct products: {len(distinct_products)}")

# 10. TRANSACTION VALUES
print("\n4. TRANSACTION VALUES")
print("-" * 95)

for t in transactions:
    print(
        f"{t['customer']} - {t['product']}: "
        f"{t['quantity']} x {t['price']:.2f} = "
        f"{t['total']:.2f}"
    )

# 11. CUSTOMER SUMMARIES
print("\n5. CUSTOMER SUMMARIES")
print("-" * 95)

customer_totals = {}

for customer in CUSTOMERS:
    customer_transactions = [
        t for t in transactions
        if t["customer"] == customer
    ]

    total_spent = sum(
        t["total"] for t in customer_transactions
    )

    total_items = sum(
        t["quantity"] for t in customer_transactions
    )

    customer_totals[customer] = total_spent

    print(
        f"{customer}: "
        f"{len(customer_transactions)} transactions | "
        f"{total_items} items | "
        f"Total spent: {total_spent:.2f}"
    )

# 12. PRODUCT SUMMARIES
print("\n6. PRODUCT SUMMARIES")
print("-" * 95)

product_totals = {}

for product in PRODUCTS:
    product_transactions = [
        t for t in transactions
        if t["product"] == product
    ]

    total_quantity = sum(
        t["quantity"] for t in product_transactions
    )

    total_sales = sum(
        t["total"] for t in product_transactions
    )

    product_totals[product] = total_sales

    print(
        f"{product}: "
        f"{total_quantity} units sold | "
        f"Sales: {total_sales:.2f}"
    )

# 13. ORDERED RESULTS
print("\n7. ORDERED RESULTS: CUSTOMERS BY TOTAL SPENDING")
print("-" * 95)

ranked_customers = sorted(
    customer_totals.items(),
    key=lambda item: (-item[1], item[0])
)

for rank, (customer, total) in enumerate(
    ranked_customers, start=1
):
    print(f"{rank}. {customer} - {total:.2f}")

print("\nPRODUCTS BY TOTAL SALES")
print("-" * 95)

ranked_products = sorted(
    product_totals.items(),
    key=lambda item: (-item[1], item[0])
)

for rank, (product, total) in enumerate(
    ranked_products, start=1
):
    print(f"{rank}. {product} - {total:.2f}")

# 14. OVERALL TRANSACTION SUMMARY
print("\n8. OVERALL TRANSACTION SUMMARY")
print("-" * 95)

overall_quantity = sum(
    t["quantity"] for t in transactions
)

overall_sales = sum(
    t["total"] for t in transactions
)

print(f"Total transaction records: {len(transactions)}")
print(f"Distinct customers: {len(distinct_customers)}")
print(f"Distinct products: {len(distinct_products)}")
print(f"Total items purchased: {overall_quantity}")
print(f"Overall transaction value: {overall_sales:.2f}")

print("\n" + "=" * 95)
print("                    END OF TRANSACTION REPORT")
print("=" * 95)
