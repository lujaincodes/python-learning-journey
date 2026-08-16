# Expense Analyzer

expenses = [12.5, 7.25, 30, 5.5, 18]

# Calculate initial values
total = 0
highest = expenses[0]
lowest = expenses[0]

for expense in expenses:
    total += expense

    if expense > highest:
        highest = expense

    if expense < lowest:
        lowest = expense

average = total / len(expenses)
number = len(expenses)

print(f"\nThe total expense is: {total}")
print(f"The average expense is: {average}")
print(f"The highest expense is: {highest}")
print(f"The lowest expense is: {lowest}")
print(f"The number of expenses is: {number}")


# Add new expenses
extra = input("\nWhat other expenses do you have? (separate with commas): ")

new_expenses = extra.split(",")

for new_expense in new_expenses:
    new_expense = float(new_expense.strip())
    expenses.append(new_expense)


# Recalculate everything
total = 0
highest = expenses[0]
lowest = expenses[0]

for expense in expenses:
    total += expense

    if expense > highest:
        highest = expense

    if expense < lowest:
        lowest = expense

average = total / len(expenses)
number = len(expenses)


# Final results
print("\nUpdated expenses:", expenses)
print("\nThe values after updating:")
print(f"- Total expense: {total}")
print(f"- Average expense: {average}")
print(f"- Highest expense: {highest}")
print(f"- Lowest expense: {lowest}")
print(f"- Number of expenses: {number}")
