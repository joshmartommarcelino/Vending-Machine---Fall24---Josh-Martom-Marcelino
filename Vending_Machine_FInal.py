# VENDING MACHINE PROGRAM
# LOADS INVENTORY FROM DICTIONARY
def load_inventory():
    return {
        '001': {"name": 'Lays Tomato Ketchup', "price": 2.90, "stock": 5},
        '002': {"name": 'Snickers', "price": 3.40, "stock": 3},
        '003': {"name": 'M&Ms', "price": 2.50, "stock": 8},
        '004': {"name": 'Pepsi', "price": 2.80, "stock": 10},
        '005': {"name": 'Sprite', "price": 2.50, "stock": 15},
        '006': {"name": 'Coke', "price": 2.20, "stock": 20},
        '007': {"name": 'Vimto', "price": 2.80, "stock": 14},
        '008': {"name": 'Cheetos', "price": 3.20, "stock": 7},
        '009': {"name": 'Chips Ahoy', "price": 2.70, "stock": 12},
        '010': {"name": 'Doritos', "price": 2.50, "stock": 18},
        '011': {"name": 'Stix', "price": 3.90, "stock": 10},
        '012': {"name": 'Water', "price": 1.50, "stock": 6},
        '013': {"name": 'Oman Pofaki Chips', "price": 2.30, "stock": 16},
        '014': {"name": 'Mars', "price": 3.00, "stock": 11},
        '015': {"name": 'Skittles', "price": 2.75, "stock": 9},
        '016': {"name": 'Bounty', "price": 2.50, "stock": 4},
        '017': {"name": 'Sour Punk', "price": 3.50, "stock": 13},
        '018': {"name": 'Loacker Wafer Chocolate', "price": 3.20, "stock": 5},
        '019': {"name": 'Reese Peanut Butter Cups', "price": 2.80, "stock": 19},
        '020': {"name": 'Gummy Bears', "price": 3.00, "stock": 17},
        '021': {"name": 'Strawberry Milk', "price": 2.75, "stock": 9},
        '022': {"name": 'Chocolate Milk', "price": 2.50, "stock": 4},
        '023': {"name": 'Banana Milk', "price": 3.50, "stock": 13},
        '024': {"name": 'Milk', "price": 3.20, "stock": 5},
        '025': {"name": 'Boba', "price": 2.80, "stock": 19},
    }
# GLOBAL INVENTORY
inventory = load_inventory()
# DISPLAYS THE INVENTORY
def display_inventory():
    print("\nAvailable Items:")
    print(f"{'ID':<5}{'Name':<25}{'Price':<10}{'Stock':<10}")
    print("-" * 50)
    for item_id, item_info in inventory.items():
        print(f"{item_id:<5}{item_info['name']:<25}${item_info['price']:<10}{item_info['stock']:<10}")
# FETCHES ITEM ID
def get_item_info(item_id):
    if item_id in inventory.items():
        item_info = inventory[item_id]
        return f'Item: {item_info[0]}, Price: ${item_info[1]}, Stock: {item_info[2]}'
    else:
        return 'Item not found.'   
# UPDATES STOCK
def update_stock(item_id, quantity):
    if item_id in load_inventory:
        item_info = load_inventory[item_id]
        if item_info[2] >= quantity:
            item_info[2] -= quantity
            return f'Successfully updated stock for {item_info[0]}: {item_info[2]}'
        else:
            return 'Not enough stock.'
    else:
        return 'Item not found.'
# SUGGEST PRODUCTS BASED ON CATEGORY
def suggest_items(category):
    suggestions = [item['name'] for item in inventory.values() if item['category'] == category and item['stock'] > 0]
    return suggestions
#PURCHASE PRODUCTS
def purchase():
    while True:
        display_inventory()
        item_id = input("\nEnter the Item ID to purchase (or 'exit' to quit): ").strip()
        if item_id.lower() == 'exit':
            print("Thank you for using the vending machine!")
            break

        if item_id not in inventory:
            print("Invalid item ID. Please try again.")
            continue

        item = inventory[item_id]
        print(f"Selected Item: {item['name']}, Price: ${item['price']}, Stock: {item['stock']}")

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if item['stock'] < quantity:
            print("Insufficient stock. Please select a lower quantity.")
            continue

        total_cost = item['price'] * quantity
        print(f"Total Cost: ${total_cost:.2f}")

        try:
            money_inserted = float(input("Please enter the sufficient amount of money: "))
            if money_inserted < total_cost:
                print("Insufficient funds. Transaction canceled.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        change = money_inserted - total_cost
        update_stock(item_id, quantity)
        print(f"Purchase successful! Your change: ${change:.2f}")
        print(f"{item['name']} dispensed.")

        # Suggest related items
        suggestions = suggest_items(item['category'])
        if suggestions:
            print("\nYou might also like:")
            for suggestion in suggestions:
                print(f" - {suggestion}")

        another_purchase = input("\nWould you like to purchase another item? (yes/no): ").strip().lower()
        if another_purchase != 'yes':
            print("Thank you for using the vending machine!")
            break
# MAIN FUNCTION
def main():
    print("Welcome to the Vending Machine!")
    while True:
        print("\nMenu:")
        print("1. Display Inventory")
        print("2. Purchase Items")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_inventory()
        elif choice == '2':
            purchase()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()