# Personal Expense Tracker

# -----------------------
# Initialize Data Structures
# -----------------------
expense_records = []  # List of tuples: (category, amount, date)
category_totals = {}  # Dictionary to sum spending by category
unique_categories = set()  # Set to track all distinct categories

print("Welcome to Personal Expense Tracker!\n")

# -----------------------
# Collect Expense Data
# -----------------------
num_expenses = 0
while num_expenses < 5:
    print(f"Enter Expense {num_expenses + 1}:")

    category = input("  Category (e.g., Food, Transport): ").strip()

    # Validate amount input
    while True:
        try:
            amount = float(input("  Amount ($): "))
            if amount >= 0:
                break
            else:
                print("    Amount cannot be negative.")
        except ValueError:
            print("    Please enter a valid number.")

    date = input("  Date (YYYY-MM-DD): ").strip()

    # Store expense as a tuple
    expense_records.append((category, amount, date))

    num_expenses += 1
    print()  # Blank line for readability

# -----------------------
# Categorize and Sum Expenses
# -----------------------
for category, amount, _ in expense_records:
    unique_categories.add(category)
    category_totals[category] = category_totals.get(category, 0) + amount

# -----------------------
# Calculate Overall Statistics
# -----------------------
amounts = [amount for _, amount, _ in expense_records]

overall_stats = {
    'total_spending': sum(amounts),
    'average_expense': sum(amounts) / len(amounts) if amounts else 0,
    'highest_expense': max(amounts) if amounts else 0,
    'lowest_expense': min(amounts) if amounts else 0
}

# -----------------------
# Generate Spending Report
# -----------------------
print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${overall_stats['total_spending']:.2f}")
print(f"Average Expense: ${overall_stats['average_expense']:.2f}")
print(f"Highest Expense: ${overall_stats['highest_expense']:.2f}")
print(f"Lowest Expense: ${overall_stats['lowest_expense']:.2f}")

print("\n=== UNIQUE CATEGORIES SPENT ON ===")
for category in sorted(unique_categories):
    print(f"- {category}")

print("\n=== SPENDING BY CATEGORY ===")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")

print("\nThank you for using Personal Expense Tracker!")
