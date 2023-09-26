import json

class Menu():
    def __init__(self):
        self.menu = [
    {"dish": "Margarita", "price": 14.99, "category": "main", "quantity": 0},
    {"dish": "Four Cheese", "price": 15.99, "category": "main", "quantity": 0},
    {"dish": "Hawaiian", "price": 16.99, "category": "main", "quantity": 0},
    {"dish": "Meat Feast", "price": 17.99, "category": "main", "quantity": 0},
    {"dish": "Chicken Tikka", "price": 18.99, "category": "main", "quantity": 0},
    {"dish": "Vegetarian", "price": 19.99, "category": "main", "quantity": 0},
    {"dish": "Special", "price": 20.99, "category": "main", "quantity": 0},

    {"dish": "Chips", "price": 4.99, "category": "side", "quantity": 0},
    {"dish": "Salad", "price": 8.99, "category": "side", "quantity": 0},
    {"dish": "Sauces", "price": 5.99, "category": "side", "quantity": 0},

    {"dish": "Ice cream", "price": 4.99, "category": "dessert", "quantity": 0},
    {"dish": "Chocolate cake", "price": 3.99, "category": "dessert", "quantity": 0},
    {"dish": "Apple pie", "price": 7.99, "category": "dessert", "quantity": 0},

    {"dish": "Coca cola", "price": 19.99, "category": "drink", "quantity": 0},
    {"dish": "Water", "price": 19.99, "category": "drink", "quantity": 0},
    {"dish": "Orange juice", "price": 19.99, "category": "drink", "quantity": 0}
]

    # formatted view of Menu
    # raise exception if empty "Sorry! Menu is empty!"
    def menu_view(self):
        mains = [f"{dish['dish']} | {dish['price']}\n" for dish in self.menu if dish["category"] == "main"]
        sides = [f"{dish['dish']} | {dish['price']}\n" for dish in self.menu if dish["category"] == "side"]
        desserts = [f"{dish['dish']} | {dish['price']}\n" for dish in self.menu if dish["category"] == "dessert"]
        drinks = [f"{dish['dish']} | {dish['price']}\n" for dish in self.menu if dish["category"] == "drink"]
        return f"*** MENU ***\nMAINS:\n{''.join(mains)}\nSIDES:\n{''.join(sides)}\nDESSERTS:\n{''.join(desserts)}\nDRINKS:\n{''.join(drinks)}"
    
    def menu_objects(self):
        return self.menu

