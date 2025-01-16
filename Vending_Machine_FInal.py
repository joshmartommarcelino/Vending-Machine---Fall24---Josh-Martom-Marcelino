#VENDING MACHINE PROGRAM
#IMPORTS TK FOR GUI
import tkinter as tk
from tkinter import messagebox

#LOADS INVENTORY FROM DICTIONARY
def load_inventory():
    return {
        '001': {"name": 'Lays Tomato Ketchup', "price": 3.50, "stock": 5, "category": "Snacks"},
        '002': {"name": 'Snickers', "price": 3.00, "stock": 3, "category": "Chocolate"},
        '003': {"name": 'M&Ms', "price": 2.50, "stock": 8, "category": "Chocolate"},
        '004': {"name": 'Pepsi', "price": 2.50, "stock": 10, "category": "Drinks"},
        '005': {"name": 'Sprite', "price": 2.50, "stock": 15, "category": "Drinks"},
        '006': {"name": 'Coke', "price": 2.50, "stock": 20, "category": "Drinks"},
        '007': {"name": 'Vimto', "price": 2.50, "stock": 14, "category": "Drinks"},
        '008': {"name": 'Cheetos', "price": 3.50, "stock": 7, "category": "Chips"},
        '009': {"name": 'Chips Ahoy', "price": 2.50, "stock": 12, "category": "Snacks"},
        '010': {"name": 'Doritos', "price": 2.50, "stock": 18, "category": "Snacks"},
        '011': {"name": 'Stix', "price": 3.50, "stock": 10, "category": "Snacks"},
        '012': {"name": 'Water', "price": 1.50, "stock": 6, "category": "Drinks"},
        '013': {"name": 'Oman Pofaki Chips', "price": 2.50, "stock": 16, "category": "Snacks"},
        '014': {"name": 'Mars', "price": 3.00, "stock": 11, "category": "Chocolate"},
        '015': {"name": 'Skittles', "price": 2.50, "stock": 9, "category": "Chocolate"},
        '016': {"name": 'Bounty', "price": 2.50, "stock": 4, "category": "Chocolate"},
        '017': {"name": 'Sour Punk', "price": 3.50, "stock": 13, "category": "Snacks"},
        '018': {"name": 'Loacker Wafer Chocolate', "price": 3.50, "stock": 5, "category": "Chocolate"},
        '019': {"name": 'Reese Peanut Butter Cups', "price": 2.50, "stock": 19, "category": "Chocolate"},
        '020': {"name": 'Gummy Bears', "price": 3.00, "stock": 17, "category": "Snacks"},
        '021': {"name": 'Strawberry Milk', "price": 2.50, "stock": 9, "category": "Drinks"},
        '022': {"name": 'Chocolate Milk', "price": 2.50, "stock": 4, "category": "Drinks"},
        '023': {"name": 'Banana Milk', "price": 3.50, "stock": 13, "category": "Drinks"},
        '024': {"name": 'Milk', "price": 3.50, "stock": 5, "category": "Drinks"},
        '025': {"name": 'Boba', "price": 2.50, "stock": 19, "category": "Drinks"},
    }
#GLOBAL INVENTORY
inventory = load_inventory()
#FUNCTIONS FOR GUI 
def display_inventory():
    inventory_text.delete(1.0, tk.END)
    inventory_text.insert(tk.END, f"{'ID':<5}{'Name':<25}{'Price':<10}{'Stock':<10}\n")
    inventory_text.insert(tk.END, "-" * 50 + "\n")
    for item_id, item_info in inventory.items():
        inventory_text.insert(
            tk.END, f"{item_id:<5}{item_info['name']:<25}${item_info['price']:<10}{item_info['stock']:<10}\n"
        )
# FILTER INVENTORY BY CATEGORY
def filter_inventory(category):
    inventory_text.delete(1.0, tk.END)
    inventory_text.insert(tk.END, f"{'ID':<5}{'Name':<25}{'Price':<10}{'Stock':<10}\n")
    inventory_text.insert(tk.END, "-" * 50 + "\n")
    for item_id, item_info in inventory.items():
        if item_info["category"] == category or category == "All":
            inventory_text.insert(
                tk.END, f"{item_id:<5}{item_info['name']:<25}${item_info['price']:<10}{item_info['stock']:<10}\n"
            )
# SUGGEST ITEMS BASED ON CATEGORY
def suggest_items(category):
    # Suggest items from the same category that are in stock
    suggestions = [
        item_info["name"] for item_id, item_info in inventory.items()
        if item_info["category"] == category and item_info["stock"] > 0
    ]
    return suggestions[:3]  # Limit to 3 suggestions
# PURCHASE AND CHECKOUT FUNCTIONS
cart = []

def purchase_item():
    item_id = item_id_entry.get().strip()
    quantity = quantity_entry.get().strip()

    if item_id not in inventory:
        messagebox.showerror("Error", "Invalid item ID.")
        return

    if not quantity.isdigit() or int(quantity) <= 0:
        messagebox.showerror("Error", "Quantity must be a positive integer.")
        return

    quantity = int(quantity)
    item = inventory[item_id]

    if item['stock'] < quantity:
        messagebox.showerror("Error", "Insufficient stock.")
        return

    total_cost = item['price'] * quantity
    cart.append({"name": item['name'], "quantity": quantity, "cost": total_cost})
    item['stock'] -= quantity

    display_inventory()

    # Display success message
    messagebox.showinfo("Success", f"Added {quantity}x {item['name']} to your cart.")

    # Generate and display suggestions
    suggestions = suggest_items(item['category'])
    if suggestions:
        messagebox.showinfo(
            "Suggestions",
            f"You might also like:\n" + "\n".join(suggestions)
        )
    # Clear inputs
    item_id_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
def checkout():
    if not cart:
        messagebox.showinfo("Checkout", "Your cart is empty!")
        return

    total_cost = sum(item['cost'] for item in cart)
    try:
        money_inserted = float(money_entry.get().strip())
        if money_inserted < total_cost:
            messagebox.showerror("Error", "Insufficient funds.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid money input.")
        return

    change = money_inserted - total_cost
    receipt = "\n".join([f"{item['quantity']}x {item['name']} - ${item['cost']:.2f}" for item in cart])

    messagebox.showinfo(
        "Checkout",
        f"Purchase successful!\n\nItems:\n{receipt}\n\nTotal Cost: ${total_cost:.2f}\nYour Change: ${change:.2f}"
    )
    cart.clear()  # EMPTIES THE CART
    money_entry.delete(0, tk.END)

# GUI SETUP
root = tk.Tk()
root.title("Vending Machine")

# INVENTORY DISPLAY WITH SCROLLBAR
inventory_frame = tk.Frame(root)
inventory_frame.pack(pady=10)

inventory_text = tk.Text(inventory_frame, height=15, width=60, state="normal", wrap="none")
inventory_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

inventory_scrollbar = tk.Scrollbar(inventory_frame, orient="vertical", command=inventory_text.yview)
inventory_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

inventory_text.config(yscrollcommand=inventory_scrollbar.set)
display_inventory()

# CATEGORY FILTER
category_label = tk.Label(root, text="Filter by Category:")
category_label.pack()

categories = ["All", "Snacks", "Chocolate", "Drinks"]
category_var = tk.StringVar(root)
category_var.set("All")

category_menu = tk.OptionMenu(root, category_var, *categories, command=filter_inventory)
category_menu.pack()

# PURCHASE SECTION
purchase_frame = tk.Frame(root)
purchase_frame.pack(pady=10)

tk.Label(purchase_frame, text="Item ID: ").grid(row=0, column=0, padx=5, pady=5)
item_id_entry = tk.Entry(purchase_frame, width=10)
item_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(purchase_frame, text="Quantity: ").grid(row=1, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(purchase_frame, width=10)
quantity_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(purchase_frame, text="Money: ").grid(row=2, column=0, padx=5, pady=5)
money_entry = tk.Entry(purchase_frame, width=10)
money_entry.grid(row=2, column=1, padx=5, pady=5)

purchase_button = tk.Button(purchase_frame, text="Purchase", command=purchase_item)
purchase_button.grid(row=3, column=0, columnspan=2, pady=10)

checkout_button = tk.Button(purchase_frame, text="Checkout", command=checkout)
checkout_button.grid(row=4, column=0, columnspan=2, pady=10)

# RUNNING THE GUI
root.mainloop()