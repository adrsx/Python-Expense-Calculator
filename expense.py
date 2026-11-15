expenses = []

while True:
    print("\n===== Expense Manager =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense Added Successfully!")

    elif choice == 2:
        print("\nExpenses List:")

        for expense in expenses:
            print(expense["category"], "-", expense["amount"])

    elif choice == 3:
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expense =", total)

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
