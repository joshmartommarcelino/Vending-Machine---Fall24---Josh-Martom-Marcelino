#THIS PROTOTYPE WAS GENERATED FROM GEMINI
class VendingMachine:
    """
    A simple vending machine simulation.
    """

    def __init__(self):
        """
        Initializes the vending machine with a sample inventory.
        """
        self.inventory = {
            "1": {"name": "Cola", "price": 1.50, "stock": 5},
            "2": {"name": "Orange Juice", "price": 1.20, "stock": 3},
            "3": {"name": "Chips", "price": 1.00, "stock": 8},
            "4": {"name": "Chocolate", "price": 0.80, "stock": 10},
        }

    def display_menu(self):
        """
        Displays the available items in the vending machine.
        """
        print("** Vending Machine Menu **")
        for item_code, item_info in self.inventory.items():
            print(f"{item_code}: {item_info['name']} - ${item_info['price']}")

    def select_item(self):
        """
        Allows the user to select an item from the menu.
        """
        while True:
            try:
                item_code = input("Enter item code (or 'q' to quit): ")
                if item_code.lower() == 'q':
                    return None
                item_code = int(item_code)
                if item_code not in self.inventory:
                    print("Invalid item code. Please try again.")
                else:
                    return item_code
            except ValueError:
                print("Invalid input. Please enter a valid item code or 'q'.")

    def insert_money(self):
        """
        Allows the user to insert money.
        """
        money_inserted = 0
        while True:
            try:
                amount = float(input("Insert money ($): "))
                if amount > 0:
                    money_inserted += amount
                else:
                    print("Invalid amount. Please insert a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

            another_coin = input("Insert another coin? (y/n): ")
            if another_coin.lower() != 'y':
                break
        return money_inserted

    def dispense_item(self, item_code):
        """
        Dispense the selected item if enough stock is available.
        """
        if self.inventory[item_code]["stock"] > 0:
            self.inventory[item_code]["stock"] -= 1
            print(f"Dispensing: {self.inventory[item_code]['name']}")
            return True
        else:
            print("Sorry, this item is out of stock.")
            return False

    def calculate_change(self, money_inserted, item_price):
        """
        Calculates and returns the change.
        """
        change = round(money_inserted - item_price, 2)
        if change > 0:
            print(f"Your change is: ${change}")
        return change

    def run(self):
        """
        Runs the vending machine simulation.
        """
        while True:
            self.display_menu()
            item_code = self.select_item()
            if item_code is None:
                break

            item_info = self.inventory[item_code]
            item_price = item_info["price"]

            money_inserted = self.insert_money()

            if money_inserted >= item_price:
                if self.dispense_item(item_code):
                    self.calculate_change(money_inserted, item_price)
            else:
                print("Insufficient funds. Please insert more money.")

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()