from basket import *
from menu import *
from confirmation import *

print("------- WELCOME TO AMINA'S RESTAURANT -------\n")
menu_print = Menu()
basket = Basket()

menu = "[1] SHOW MENU \n[2] SHOW MY BASKET\n[3] ORDER\n[4] DELETE FROM BASKET\n[5] CHECKOUT"
while True:
    print(menu)
    user_choice = input("What would you like to do: ")
    
    match user_choice:
        case "1":
            print(f"\n{menu_print.menu_view()}")
            
        case "2":
            try:
                print(f"\n{basket.view_basket()}")

            except Exception as err:
                print("An exception occurred:", err)

        case 3:
            pass
        case 4:
            pass

    