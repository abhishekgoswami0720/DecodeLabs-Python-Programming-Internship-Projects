def get_expense():
    
    raw_input_value = input("Enter an expense amount (or 'done' to finish): ").strip()

    if raw_input_value.lower() == "done":
        return None

    try:
        expense = float(raw_input_value)
        if expense < 0:
            print("⚠️  Expenses can't be negative. Try again.")
            return -1
        return expense
    except ValueError:
        print("⚠️  That's not a valid number. Please try again.")
        return -1


def main():
    print("Welcome to your Python Expense Tracker! 💰")
    print("Enter your expenses one by one. Type 'done' when you're finished.\n")

    total = 0.0         
    expense_count = 0   

    while True:
        expense = get_expense()

        if expense is None:
            break
        if expense == -1:
            continue

        total += expense   
        expense_count += 1
        print(f"✅ Added ₹{expense:.2f}. Running total: ₹{total:.2f}\n")
    print("\n===== EXPENSE SUMMARY =====")
    if expense_count == 0:
        print("No expenses were entered.")
    else:
        print(f"Number of expenses: {expense_count}")
        print(f"Total Spent: ₹{total:.2f}")
        print(f"Average expense: ₹{total / expense_count:.2f}")


if __name__ == "__main__":
    main()