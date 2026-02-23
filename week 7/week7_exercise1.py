# Product Pricing Manager (Polished Version)

# -----------------------
# Define discounts
# -----------------------
category_discounts = {
    'Electronics': 0.10,
    'Clothing': 0.15,
    'Books': 0.05,
    'Home': 0.12
}

tier_discounts = {
    'Premium': 0.05,
    'Standard': 0.00,
    'Budget': 0.02
}

# -----------------------
# Initialize data structures
# -----------------------
products = []  # List to store product info and calculated prices
total_discount_percentages = []  # For calculating average discount

# Hardcoded product data (you can later replace this with file input)
products_data = [
    "Computer,999.99,Electronics,Premium",
    "Jacket,129.99,Clothing,Standard",
    "Book,49.99,Books,Standard",
    "Instant Pot,79.99,Home,Budget",
    "Apple Headphones,199.99,Electronics,Premium"
]

# -----------------------
# Process product data
# -----------------------
for line_num, line in enumerate(products_data, start=1):
    try:
        name, base_price_str, category, tier = line.split(',')
        base_price = float(base_price_str)

        # Apply discounts
        cat_discount = category_discounts.get(category, 0)
        tier_discount = tier_discounts.get(tier, 0)
        total_discount = cat_discount + tier_discount
        discount_amount = base_price * total_discount
        final_price = base_price - discount_amount

        # Store calculated data
        products.append({
            'name': name,
            'base_price': base_price,
            'category': category,
            'tier': tier,
            'total_discount_pct': total_discount * 100,
            'discount_amount': discount_amount,
            'final_price': final_price
        })

        total_discount_percentages.append(total_discount * 100)

    except ValueError:
        print(f"Line {line_num}: Invalid format or price '{line}' skipped.")

# -----------------------
# Write pricing report
# -----------------------
try:
    with open('pricing_report.txt', 'w') as report:
        # Report Header
        report.write("PRICING REPORT\n")
        report.write("="*75 + "\n")
        report.write(f"{'Product Name':30} {'Base Price':>12} {'Discount %':>12} "
                     f"{'Discount $':>12} {'Final Price':>12}\n")
        report.write("-"*75 + "\n")

        # Product details
        for product in products:
            report.write(f"{product['name']:30} "
                         f"${product['base_price']:>10.2f} "
                         f"{product['total_discount_pct']:>10.2f}% "
                         f"${product['discount_amount']:>10.2f} "
                         f"${product['final_price']:>10.2f}\n")

except IOError:
    print("Error: Could not write to 'pricing_report.txt'.")
    exit(1)

# -----------------------
# Console summary
# -----------------------
if products:
    total_products = len(products)
    avg_discount = sum(total_discount_percentages) / total_products
    print(f"Total products processed: {total_products}")
    print(f"Average discount applied: {avg_discount:.2f}%")
else:
    print("No products were processed successfully.")
