# Product Pricing Manager

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

# -----------------------
# Read product data
# -----------------------
try:
    with open('products.txt', 'r') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue  # skip empty lines
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

except FileNotFoundError:
    print("Error: 'products.txt' file not found.")
    exit(1)

# -----------------------
# Write pricing report
# -----------------------
try:
    with open('pricing_report.txt', 'w') as report:
        # Write header
        report.write(f"{'Product Name':30} {'Base Price':>10} {'Discount %':>12} "
                     f"{'Discount $':>12} {'Final Price':>12}\n")
        report.write("="*80 + "\n")

        # Write product info
        for product in products:
            report.write(f"{product['name']:30} "
                         f"${product['base_price']:>9.2f} "
                         f"{product['total_discount_pct']:>11.2f}% "
                         f"${product['discount_amount']:>11.2f} "
                         f"${product['final_price']:>11.2f}\n")

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
