items = {
    '001' : ['Lays Tomato Ketchup', 2.90, "stock": 5]
    '002' : ['Snickers', 3.40, "stock": 3]
    '003' : ['M&Ms', 2.50, "stock": 8]
    '004' : ['Pepsi', 2.80, "stock": 10]
    '005' : ['Sprite', 2.50, "stock": 15]
    '006' : ['Coke', 2.20, "stock": 20]
    '007' : ['Vimto', 2.80, "stock": 14]
    '008' : ['Cheetos', 3.20, "stock": 7]
    '009' : ['Chips Ahoy', 2.70, "stock": 12]
    '010' : ['Doritos', 2.50, "stock": 18]
    '011' : ['Stix', 3.90, "stock": 10]
    '012' : ['Water', 1.50, "stock": 6]
    '013' : ['Oman Pofaki Chips', 2.30, "stock": 16]
    '014' : ['Mars', 3.00, "stock": 11]
    '015' : ['Skittles', 2.75, "stock": 9]
    '016' : ['Bounty', 2.50, "stock": 4]
    '017' : ['Sour Punk', 3.50, "stock": 13]
    '018' : ['Loacker Wafer Chocolate', 3.20, "stock": 5]
    '019' : ['Reese Peanut Butter Cups', 2.80, "stock": 19]
    '020' : ['Gummy Bears', 3.00, "stock": 17]
    '021' : ['Strawberry Milk', 2.75, "stock": 9]
    '022' : ['Chocolate Milk', 2.50, "stock": 4]
    '023' : ['Banana Milk', 3.50, "stock": 13]
    '024' : ['Milk', 3.20, "stock": 5]
    '025' : ['Boba', 2.80, "stock": 19]
}

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
    
    item_price = float(item_info.split(', Price: $')[1])
    total_cost = item_price * quantity
    
    print(f'Item: {item_info.split(", Price: $")[0]}, Price: ${item_price}, Quantity: {quantity}, Total Cost: ${total_cost}')
    
    money_inserted = float(input('Enter money inserted: '))
    change = money_inserted - total_cost
    
    if change < 0:
        print('Insufficient funds.')
        continue
    
    update_stock(item_id, quantity)