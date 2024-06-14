import tkinter as tk
from datetime import datetime

class FinanceManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Personal Finance Manager")
        master.configure(bg="#2C3E50")
        master.geometry("800x600")  # Set default size

        # Configure colors and fonts
        self.bg_color = "#2C3E50"
        self.fg_color = "#ECF0F1"
        self.button_bg_color = "#3498DB"
        self.button_fg_color = "#ECF0F1"
        self.font_title = ("Helvetica", 24, "bold")
        self.font_label = ("Helvetica", 14)
        self.font_button = ("Helvetica", 14, "bold")

        self.label = tk.Label(master, text="Welcome to Personal Finance Manager", font=self.font_title, bg=self.bg_color, fg=self.fg_color)
        self.label.pack(pady=20)

        self.transaction_frame = tk.Frame(master, bg=self.bg_color)
        self.transaction_frame.pack(expand=True, fill='both', padx=20, pady=20)

        for row in range(4):
            self.transaction_frame.grid_rowconfigure(row, weight=1)
        for col in range(2):
            self.transaction_frame.grid_columnconfigure(col, weight=1)

        self.add_income_button = tk.Button(self.transaction_frame, text="Add Income", command=self.add_income, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.add_income_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.add_expense_button = tk.Button(self.transaction_frame, text="Add Expense", command=self.add_expense, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.add_expense_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.view_transactions_button = tk.Button(self.transaction_frame, text="View Transactions", command=self.view_transactions, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.view_transactions_button.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.view_today_button = tk.Button(self.transaction_frame, text="View Today's Transactions", command=self.view_today, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.view_today_button.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.view_week_button = tk.Button(self.transaction_frame, text="View This Week's Transactions", command=self.view_week, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.view_week_button.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

        self.view_month_button = tk.Button(self.transaction_frame, text="View This Month's Transactions", command=self.view_month, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.view_month_button.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        self.balance_button = tk.Button(self.transaction_frame, text="Calculate Balance", command=self.calculate_balance, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.balance_button.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        self.exit_button = tk.Button(self.transaction_frame, text="Exit", command=master.quit, fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        self.exit_button.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

        # Initialize FinanceManager
        self.finance_manager = FinanceManager()

    def add_income(self):
        self.open_transaction_window("Add Income", self.add_income_transaction)

    def add_expense(self):
        self.open_transaction_window("Add Expense", self.add_expense_transaction)

    def open_transaction_window(self, title, add_transaction_func):
        transaction_window = tk.Toplevel(self.master)
        transaction_window.title(title)
        transaction_window.configure(bg=self.bg_color)
        transaction_window.geometry("400x200")  # Set default size

        date_label = tk.Label(transaction_window, text="Date (YYYY-MM-DD):", font=self.font_label, bg=self.bg_color, fg=self.fg_color)
        date_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        date_entry = tk.Entry(transaction_window, font=self.font_label)
        date_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        description_label = tk.Label(transaction_window, text="Description:", font=self.font_label, bg=self.bg_color, fg=self.fg_color)
        description_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        description_entry = tk.Entry(transaction_window, font=self.font_label)
        description_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        amount_label = tk.Label(transaction_window, text="Amount:", font=self.font_label, bg=self.bg_color, fg=self.fg_color)
        amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        amount_entry = tk.Entry(transaction_window, font=self.font_label)
        amount_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        add_button = tk.Button(transaction_window, text="Add", command=lambda: add_transaction_func(date_entry.get(), description_entry.get(), amount_entry.get()), fg=self.button_fg_color, bg=self.button_bg_color, font=self.font_button)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_income_transaction(self, date, description, amount):
        self.add_transaction(date, description, float(amount))

    def add_expense_transaction(self, date, description, amount):
        self.add_transaction(date, description, -float(amount))

    def view_transactions(self):
        self.finance_manager.view_transactions()

    def view_today(self):
        self.finance_manager.view_transactions_today()

    def view_week(self):
        self.finance_manager.view_transactions_week()

    def view_month(self):
        self.finance_manager.view_transactions_month()

    def calculate_balance(self):
        self.finance_manager.calculate_balance()

    def add_transaction(self, date, description, amount):
        self.finance_manager.add_transaction(date, description, amount)
        print("Transaction added successfully!")

class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount):
        self.transactions.append(Transaction(date, description, amount))
        print("Transaction added successfully!")

    def view_transactions(self):
        if self.transactions:
            print("\nTransaction History:")
            for transaction in self.transactions:
                print(f"Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}")
        else:
            print("Your transaction history is empty!")

    def view_transactions_today(self):
        today = datetime.now().strftime('%Y-%m-%d')
        today_transactions = [transaction for transaction in self.transactions if transaction.date == today]

        if today_transactions:
            print("\nToday's Transactions:")
            for transaction in today_transactions:
                print(f"Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}")
        else:
            print("No transactions recorded for today.")

    def view_transactions_week(self):
        current_week = datetime.now().isocalendar()[1]
        week_transactions = [transaction for transaction in self.transactions if datetime.strptime(transaction.date, '%Y-%m-%d').isocalendar()[1] == current_week]

        if week_transactions:
            print("\nThis Week's Transactions:")
            for transaction in week_transactions:
                print(f"Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}")
        else:
            print("No transactions recorded for this week.")

    def view_transactions_month(self):
        current_month = datetime.now().strftime('%m')
        month_transactions = [transaction for transaction in self.transactions if datetime.strptime(transaction.date, '%Y-%m-%d').strftime('%m') == current_month]

        if month_transactions:
            print("\nThis Month's Transactions:")
            for transaction in month_transactions:
                print(f"Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}")
        else:
            print("No transactions recorded for this month.")

    def calculate_balance(self):
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        total_expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        balance = total_income + total_expenses
        print(f"\nTotal Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Current Balance: {balance}")

root = tk.Tk()
finance_manager_gui = FinanceManagerGUI(root)
root.mainloop()