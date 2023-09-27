from menu import Menu

class Basket():
    def __init__(self, menu_import = False):
        # self basket will always extract objects
        # from Menu.menu with higher quantity than 1
        if menu_import == False:
            self.menu_data = Menu()
        else:
            self.menu_data = menu_import

        self.basket = []    # contains MenuItem objects

    def update_basket(self):
        self.basket = [item for item in self.menu_data.menu if item["quantity"] > 0]

    # add menu item to basket by increasing quantity
    def add_basket(self, add_dish_name):
        for item in self.menu_data.menu:
            if item["dish"] == add_dish_name:
                item["quantity"] = item["quantity"] + 1
                break
        # catch error when no such dish in the menu
        else:
            raise Exception("No such dish in the menu!")
        self.update_basket()
    
    # remove menu item from basket by decreasing quantity
    def remove_basket(self, remove_dish_name):
        for item in self.menu_data.menu:
            if item["dish"] == remove_dish_name:
                item["quantity"] = item["quantity"] - 1
                break
        # catch error when no such dish in the menu
        else:
            raise Exception("No such dish in the menu!")
        self.update_basket()
    
    #view formatted view of the basket / will use as receipt
    def view_basket(self):
        if self.basket == []:
            raise Exception ("Basket is empty!")
        self.update_basket()
        in_basket = [f"{dish['dish']} | x {dish['quantity']} | {(dish['quantity'])*(dish['price'])}\n" for dish in self.basket]
        return "YOUR BASKET:\n" + "".join(in_basket) + f"\n\nTOTAL: {self.view_total()}"

    # view total price per basket
    def view_total(self):
        total_sum = [(dish['quantity'] * dish['price']) for dish in self.basket]
        return sum(total_sum)

# test_menu = Menu()
# test_basket = Basket()
# test_basket.add_basket("Margarita")

# print(test_basket.view_basket())