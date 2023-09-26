from menu import Menu
import json

class Basket():
    def __init__(self):
        # self basket will always extract objects
        # from Menu.menu with higher quantity than 1
        self.menu_data = Menu()
        self.basket = []    # contains MenuItem objects

    def update_basket(self):
        self.basket = [item for item in self.menu_data.menu if item["quantity"] > 0]

    # add MenuItem object from the Menu.menu by adding 1 quantity
    def add_basket(self, add_dish_name):
        for item in self.menu_data.menu:
            if item["dish"] == add_dish_name:
                item["quantity"] = item["quantity"] + 1
        self.update_basket()
        #TODO error message is dish not in menu
    
    # remove MenuItem object from the by lowering quantity
    def remove_basket(self, remove_dish_name):
        for item in self.menu_data.menu:
            if item["dish"] == remove_dish_name:
                item["quantity"] = item["quantity"] - 1
        self.update_basket()
        #TODO error message is dish not in menu
    
    def view_basket(self):
        # view basket object list with:
        # "YOUR BASKET:\nPizza1 | x 1 | 14.99\nTOTAL: 14.99"
            # name
            # quantity
            # total price per object
            # total per basket
            # raise exception when empty
        self.update_basket()
        in_basket = [f"{dish['dish']} | x {dish['quantity']} | {(dish['quantity'])*(dish['price'])}\n" for dish in self.basket]
        print("YOUR BASKET:\n", " ".join(in_basket), f"\n\nTOTAL: {self.view_total()}")
        return "YOUR BASKET:\n", in_basket, f"\n\nTOTAL: {self.view_total()}"

    # view total price per basket
    def view_total(self):
        total_sum = [(dish['quantity'] * dish['price']) for dish in self.basket]
        return sum(total_sum)


test_menu = Menu()
test_basket = Basket()
test_basket.add_basket("Margarita")

test_basket.view_basket()
# for item in test_menu
# test_menu.MenuItem_category()