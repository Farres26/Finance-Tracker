#logic of program (the functions)
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

DATA_FILE = 'data.csv'

def add_transaction(): # tansaction function
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

def view_summary(): # summary function
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

def view_by_category():
    category_totals = defaultdict(float)
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4 or row[1] != 'expense':
                    continue
                category_totals[row[2]] += float(row[3])
        print("\n--- Spending by Category ---")
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
    except FileNotFoundError:
        print("No transactions found.")

def view_monthly_summary():
    income_by_month = defaultdict(float)
    expense_by_month = defaultdict(float)
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4:
                    continue
                date_str, t_type, _, amount = row
                month = date_str[:7]  # YYYY-MM
                if t_type == 'income':
                    income_by_month[month] += float(amount)
                elif t_type == 'expense':
                    expense_by_month[month] += float(amount)
        print("\n--- Monthly Summary ---")
        months = sorted(set(income_by_month.keys()) | set(expense_by_month.keys()))
        for month in months:
            income = income_by_month[month]
            expense = expense_by_month[month]
            print(f"{month} - Income: ${income:.2f}, Expense: ${expense:.2f}, Balance: ${income - expense:.2f}")
    except FileNotFoundError:
        print("No transactions found.")

def plot_category_spending(): # pie chart function
    category_totals = defaultdict(float)
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4 or row[1] != 'expense':
                    continue
                category_totals[row[2]] += float(row[3])
        if not category_totals:
            print("No spending data available.")
            return

        labels = list(category_totals.keys())
        values = list(category_totals.values())

        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Spending by Category')
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No transactions found.")

def plot_monthly_spending(): # bar chart function
    monthly_expenses = defaultdict(float)
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4 or row[1] != 'expense':
                    continue
                month = row[0][:7]
                monthly_expenses[month] += float(row[3])
        if not monthly_expenses:
            print("No spending data available.")
            return

        months = sorted(monthly_expenses.keys())
        values = [monthly_expenses[m] for m in months]

        plt.figure(figsize=(10, 5))
        plt.bar(months, values, color='skyblue')
        plt.title('Monthly Expenses')
        plt.xlabel('Month')
        plt.ylabel('Amount ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("No transactions found.")
