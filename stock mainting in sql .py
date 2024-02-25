import tkinter as tk
from tkinter import ttk
import sqlite3

class StockMaintenanceApp:
    def __init__(self, root, database):
        self.root = root
        self.root.title("Stock Maintenance Application")

        # Create a database connection
        self.conn = sqlite3.connect(database)
        self.create_table()

        # Create variables
        self.product_name_var = tk.StringVar()
        self.quantity_var = tk.IntVar()
        self.price_var = tk.DoubleVar()

        # Create labels
        tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(root, text="Price:").grid(row=2, column=0, padx=10, pady=5)

        # Create entry widgets
        tk.Entry(root, textvariable=self.product_name_var).grid(row=0, column=1, padx=10, pady=5)
        tk.Entry(root, textvariable=self.quantity_var).grid(row=1, column=1, padx=10, pady=5)
        tk.Entry(root, textvariable=self.price_var).grid(row=2, column=1, padx=10, pady=5)

        # Create buttons
        tk.Button(root, text="Add Stock", command=self.add_stock).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="View Stock", command=self.view_stock).grid(row=4, column=0, columnspan=2, pady=10)

        # Create a listbox to display stock
        self.stock_listbox = tk.Listbox(root)
        self.stock_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def create_table(self):
        # Create a table if it doesn't exist
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock (
                id INTEGER PRIMARY KEY,
                product_name TEXT,
                quantity INTEGER,
                price REAL
            )
        ''')
        self.conn.commit()

    def add_stock(self):
        # Get values from entry widgets
        product_name = self.product_name_var.get()
        quantity = self.quantity_var.get()
        price = self.price_var.get()

        # Add stock to the database
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO stock (product_name, quantity, price) VALUES (?, ?, ?)
        ''', (product_name, quantity, price))
        self.conn.commit()

        # Clear entry widgets
        self.product_name_var.set("")
        self.quantity_var.set(0)
        self.price_var.set(0.0)

    def view_stock(self):
        # Retrieve stock from the database
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM stock')
        stock_data = cursor.fetchall()

        # Display stock in the listbox
        self.stock_listbox.delete(0, tk.END)  # Clear existing entries
        for row in stock_data:
            stock_entry = f"{row[1]} - Quantity: {row[2]}, Price: {row[3]}"
            self.stock_listbox.insert(tk.END, stock_entry)

if __name__ == "__main__":
    root = tk.Tk()
    app = StockMaintenanceApp(root, "sales_database.db")
    root.mainloop()
