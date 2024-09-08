class MenuItem:
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details

    def info(self): #method/function to display menu information
        return f"{self.name}: ${self.price} ({self.details})"

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9
        return round(total_price)

menu_items = [
    MenuItem('Sandwich', 5, '330kcal'),
    MenuItem('Chocolate Cake', 4, '450kcal'),
    MenuItem('Cream Puff', 2, '180kcal'),
    MenuItem('Coffee', 3, '180mL'),
    MenuItem('Orange Juice', 2, '350mL'),
    MenuItem('Espresso', 3, '30mL')
]

print('Menu:')
for index, item in enumerate(menu_items, start=1):
    print(f"{index}. {item.info()}")

print('--------------------')


menu_order = int(input('Enter menu item number: ')) - 1
selected_menu = menu_items[menu_order]


count = int(input("How many meals would you like to purchase? (10% off for 3 or more): "))

result = selected_menu.get_total_price(count)


print(f"Your total is ${result}")