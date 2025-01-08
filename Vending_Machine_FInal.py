def load_inventory():
    inventory_file = 'inventory.txt'
    inventory = {
        '001': {"name": 'Lays Tomato Ketchup', "price": 2.90, "stock": 5},
        '002': {"name": 'Snickers', "price": 3.40, "stock": 3},
        '003': {"name": 'M&Ms', "price": 2.50, "stock": 8},
        '004': {"name": 'Pepsi', "price": 2.80, "stock": 10},
        '005': {"name": 'Sprite', "price": 2.50, "stock": 15},
        '006': {"name": 'Coke', "price": 2.20, "stock": 20},
        '007': {"name": 'Vimto', "price": 2.80, "stock": 14},
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
    return inventory

def display_inventory():
    for item_id, item_info in load_inventory():
        print(f'Item ID: {item_id}, Item: {item_info[0]}, Price: ${item_info[1]}, Stock: {item_info[2]}')


def get_item_info(item_id):
    if item_id in items:
        item_info = items[item_id]
        return f'Item: {item_info[0]}, Price: ${item_info[1]}, Stock: {item_info[2]}'
    else:
        return 'Item not found.'
    
def update_stock(item_id, quantity):
    if item_id in items:
        item_info = items[item_id]
        if item_info[2] >= quantity:
            item_info[2] -= quantity
            return f'Successfully updated stock for {item_info[0]}: {item_info[2]}'
        else:
            return 'Not enough stock.'
    else:
        return 'Item not found.'
def purchase():
    while True:
        item_id = input('Enter item ID: ')
        quantity = int(input('Enter quantity: '))

        item_info = get_item_info(item_id)
        if item_info == 'Item not found.':
            print('Invalid item ID.')
            continue
        item_price = float(item_info.split(', Price: $')[1].split(',')[0])
        total_cost = item_price * quantity#+
        print(f'Item: {item_info.split(", Price: $")[0]}, Price: ${item_price}, Quantity: {quantity}, Total Cost: ${total_cost}')

        money_inserted = float(input('Enter money inserted: '))
        change = money_inserted - total_cost
        if change < 0:
            print('Insufficient funds.')
            continue

        update_stock(item_id, quantity)
        print(f'Purchase successful. Your change: ${change:.2f}')
        break

update_stock(item_id, quantity)