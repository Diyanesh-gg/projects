# Import required libraries
import tkinter as tk
from tkinter import messagebox

# Define the Stock class
class Stock:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

# Define the StockMaintainApp class
class StockMaintainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Maintenance App")

        # Create and set up variables
        self.stock_list = []
        self.item_var = tk.StringVar()
        self.quantity_var = tk.StringVar()

        # Create and set up GUI components
        tk.Label(root, text="Item:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.item_var).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.quantity_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Button(root, text="Add Stock", command=self.add_stock).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="View Stock", command=self.view_stock).grid(row=3, column=0, columnspan=2, pady=10)

    def add_stock(self):
        item = self.item_var.get()
        quantity = self.quantity_var.get()

        if item and quantity:
            stock_item = Stock(item, quantity)
            self.stock_list.append(stock_item)
            messagebox.showinfo("Success", "Stock added successfully!")
        else:
            messagebox.showerror("Error", "Please enter both item and quantity.")

    def view_stock(self):
        if not self.stock_list:
            messagebox.showinfo("Stock", "No stock available.")
        else:
            stock_info = "\n".join([f"{stock.item}: {stock.quantity}" for stock in self.stock_list])
            messagebox.showinfo("Stock", f"Current Stock:\n{stock_info}")

# Create the main application window
root = tk.Tk()
app = StockMaintainApp(root)

# Start the Tkinter event loop
root.mainloop()
