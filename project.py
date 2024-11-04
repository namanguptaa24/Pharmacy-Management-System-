import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

# Load or create data file
DATA_FILE = "pharmacy_data.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Tkinter GUI setup
root = tk.Tk()
root.title("Enhanced Pharmacy Management System")
root.geometry("900x600")
root.configure(bg="lightblue")

current_index = -1

# Form Functions
def add_item():
    data = load_data()
    item_name = entry_name.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    category = entry_category.get()
    discount = entry_discount.get()
    expiry = entry_expiry.get()

    if not item_name or not price or not quantity or not category or not discount or not expiry:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return

    try:
        price = float(price)
        quantity = int(quantity)
        discount = float(discount)
    except ValueError:
        messagebox.showwarning("Input Error", "Price, Quantity, and Discount must be numbers.")
        return

    new_item = {
        "name": item_name,
        "price": price,
        "quantity": quantity,
        "category": category,
        "discount": discount,
        "expiry_date": expiry
    }
    data.append(new_item)
    save_data(data)
    clear_fields()
    messagebox.showinfo("Success", "Item added successfully!")

def delete_item():
    global current_index
    data = load_data()
    if current_index < 0 or current_index >= len(data):
        messagebox.showwarning("Selection Error", "No item selected to delete.")
        return
    del data[current_index]
    save_data(data)
    current_index = -1
    clear_fields()
    messagebox.showinfo("Success", "Item deleted successfully!")

def update_item():
    global current_index
    data = load_data()
    if current_index < 0 or current_index >= len(data):
        messagebox.showwarning("Selection Error", "No item selected to update.")
        return

    item_name = entry_name.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    category = entry_category.get()
    discount = entry_discount.get()
    expiry = entry_expiry.get()

    if not item_name or not price or not quantity or not category or not discount or not expiry:
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return

    try:
        price = float(price)
        quantity = int(quantity)
        discount = float(discount)
    except ValueError:
        messagebox.showwarning("Input Error", "Price, Quantity, and Discount must be numbers.")
        return

    data[current_index] = {
        "name": item_name,
        "price": price,
        "quantity": quantity,
        "category": category,
        "discount": discount,
        "expiry_date": expiry
    }
    save_data(data)
    clear_fields()
    messagebox.showinfo("Success", "Item updated successfully!")

def search_item():
    data = load_data()
    item_name = entry_name.get()
    for index, item in enumerate(data):
        if item['name'] == item_name:
            display_item(item, index)
            return
    messagebox.showinfo("Not Found", f"Item '{item_name}' not found.")

def display_item(item, index):
    global current_index
    current_index = index
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_discount.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)

    entry_name.insert(0, item["name"])
    entry_price.insert(0, str(item["price"]))
    entry_quantity.insert(0, str(item["quantity"]))
    entry_category.insert(0, item["category"])
    entry_discount.insert(0, str(item["discount"]))
    entry_expiry.insert(0, item["expiry_date"])

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_discount.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)
    global current_index
    current_index = -1

# UI Elements
tk.Label(root, text="Pharmacy Management System", font=("Arial", 24, "bold"), bg="lightblue").grid(row=0, columnspan=2, pady=20)

tk.Label(root, text="Item Name:", bg="lightblue", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Item Price:", bg="lightblue", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_price = tk.Entry(root, font=("Arial", 12))
entry_price.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Quantity:", bg="lightblue", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_quantity = tk.Entry(root, font=("Arial", 12))
entry_quantity.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Category:", bg="lightblue", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
entry_category = tk.Entry(root, font=("Arial", 12))
entry_category.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Discount (%):", bg="lightblue", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
entry_discount = tk.Entry(root, font=("Arial", 12))
entry_discount.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

tk.Label(root, text="Expiry Date (YYYY-MM-DD):", bg="lightblue", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
entry_expiry = tk.Entry(root, font=("Arial", 12))
entry_expiry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

# Buttons
button_add = tk.Button(root, text="Add Item", width=15, command=add_item)
button_add.grid(row=7, column=0, padx=10, pady=10)

button_delete = tk.Button(root, text="Delete Item", width=15, command=delete_item)
button_delete.grid(row=7, column=1, padx=10, pady=10)

button_update = tk.Button(root, text="Update Item", width=15, command=update_item)
button_update.grid(row=8, column=0, padx=10, pady=10)

button_search = tk.Button(root, text="Search Item", width=15, command=search_item)
button_search.grid(row=8, column=1, padx=10, pady=10)

button_clear = tk.Button(root, text="Clear Fields", width=15, command=clear_fields)
button_clear.grid(row=9, column=0, padx=10, pady=10)

root.mainloop()
