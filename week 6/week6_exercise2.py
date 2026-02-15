# Student Grade Analyzer

# -----------------------
# Part A: Data Collection
# -----------------------

student_records = []  # List to hold tuples (name, score)

print("Welcome to the Student Grade Analyzer!\n")

for i in range(1, 7):
    print(f"Enter information for Student {i}:")
    name = input("  Name: ")

    # Input validation for score
    while True:
        try:
            score = float(input("  Score (0-100): "))
            if 0 <= score <= 100:
                break
            else:
                print("    Score must be between 0 and 100.")
        except ValueError:
            print("    Please enter a valid number.")

    # Store as tuple in the list
    student_records.append((name, score))
    print()  # Blank line for readability

# -----------------------
# Part B: Statistics
# -----------------------

# Extract just the scores for calculations
scores = [score for _, score in student_records]

stats = {
    'highest': max(scores),
    'lowest': min(scores),
    'average': sum(scores) / len(scores)
}

# -----------------------
# Part C: Unique Grades
# -----------------------

unique_scores = set(scores)

# -----------------------
# Part D: Grade Distribution
# -----------------------

grade_distribution = {}
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1

# -----------------------
# Display Results
# -----------------------

print("\n=== STUDENT RECORDS ===")
for name, score in student_records:
    print(f"{name}: {score}")

print("\n=== STATISTICS ===")
print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")

print("\n=== UNIQUE SCORES ===")
print(sorted(unique_scores))  # sorted for readability

print("\n=== GRADE DISTRIBUTION ===")
for score, count in sorted(grade_distribution.items()):
    print(f"Score {score}: {count} student{'s' if count > 1 else ''}")
