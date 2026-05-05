"""
Professional Expense Tracker
Internship Project

Features:
- Continuous expense entry
- View all expenses
- View total
- Clean UX flow
"""

def display_menu():
    print("\n" + "=" * 45)
    print("         EXPENSE TRACKER SYSTEM")
    print("=" * 45)
    print("1. Add Expenses (Multiple)")
    print("2. View All Expenses")
    print("3. View Total")
    print("4. Exit")
    print("=" * 45)


def add_expenses(expenses):
    print("\n Enter expenses one by one")
    print(" Type 'done' to stop\n")

    while True:
        user_input = input("Enter amount: ")

        if user_input.lower() == "done":
            break

        try:
            expense = float(user_input)
            if expense < 0:
                print(" Cannot be negative")
                continue

            expenses.append(expense)
            print(f" Added: {expense:.2f} | Total: {sum(expenses):.2f}")

        except ValueError:
            print(" Invalid input")


def main():
    expenses = []

    while True:
        display_menu()
        choice = input("Select option (1-4): ").strip()

        if choice == "1":
            add_expenses(expenses)

        elif choice == "2":
            if not expenses:
                print(" No expenses yet")
            else:
                print("\n Expenses List:")
                for i, exp in enumerate(expenses, 1):
                    print(f"{i}. {exp:.2f}")

        elif choice == "3":
            print(f"\n Total: {sum(expenses):.2f}")

        elif choice == "4":
            print("\n FINAL SUMMARY")
            print(f"Entries: {len(expenses)}")
            print(f"Total Spent: {sum(expenses):.2f}")
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice")


if __name__ == "__main__":
    main()