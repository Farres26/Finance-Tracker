# file is made for main menu and launches program
import csv
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

DATA_FILE = 'data.csv'

# Add a transaction
def add_transaction():
    try:
        amount = float(input("Enter the amount: "))
        category = input("Enter the category (e.g., Food, Rent, Salary): ").title()
        t_type = input("Type (income or expense): ").lower()
        date = input("Enter the date (YYYY-MM-DD), or press Enter for today: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')

        with open(DATA_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, t_type, category, amount])
        print("✅ Transaction added!")
    except ValueError:
        print("❌ Please enter a valid number.")

# View summary
def view_summary():
    income = 0
    expense = 0
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                if row[1] == 'income':
                    income += float(row[3])
                elif row[1] == 'expense':
                    expense += float(row[3])
        print(f"\n--- Financial Summary ---")
        print(f"Total Income:  ${income:.2f}")
        print(f"Total Expense: ${expense:.2f}")
        print(f"Balance:       ${income - expense:.2f}")
    except FileNotFoundError:
        print("No transactions found yet.")

# Menu loop
def main():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add a transaction")
        print("2. View summary")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Start the app
if __name__ == "__main__":
    main()
