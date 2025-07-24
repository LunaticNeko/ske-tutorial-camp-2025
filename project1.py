def main():
    print("="*20)
    print("EXPENSE TRACKER MENU")
    print("="*20)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View by Category")
    print("4. Spending Summary")
    print("5. Exit")

    print()

    # validate menu choice
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if not (1 <= choice <= 5):
                raise ValueError
            break
        except:
            print("Invalid Choice. Please try again.")
            continue

    if choice == 1:
        print()

        while True:
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount. Please try again.")
                continue

            if amount < 0:
                print("Amount cannot be less than zero. Please try again.")
                continue
            else:
                break

        valid_categories = ["food", "transport", "entertainment", "shopping", "bills"]
        
        # validate the category
        while True:
            try:
                category = input("Enter category (" + ", ".join(valid_categories) + "): ")
                if category not in valid_categories:
                    raise ValueError
                break
            except:
                print("Invalid Category. Please try again.")
                continue

        print(f"Added {amount} in {category}")

# This makes the program run the main function when executed
if __name__ == "__main__":
    main()
