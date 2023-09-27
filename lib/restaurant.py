from basket import *
from menu import *
from confirmation import *

print("------- WELCOME TO AMINA'S RESTAURANT -------\n")
menu = Menu()
basket = Basket()

menu_print = "[1] SHOW MENU \n[2] SHOW MY BASKET\n[3] ORDER\n[4] DELETE FROM BASKET\n[5] CHECKOUT"
while True:
    print(menu_print)
    user_choice = input("What would you like to do: ")
    
    match user_choice:
        case "1":
            try:
                print(f"\n{menu.menu_view()}")
            except Exception as error:
                print("Ups! ", error)
            
        case "2":
            try:
                print("\n-----------------------------")
                print(f"{basket.view_basket()}")
                print("-----------------------------\n")
            except Exception as error:
                print("Ups! ", error)

        case "3":
            try:
                user_order_dish = input("What would you like to order? [name of the dish from the menu]: ")
                basket.add_basket(user_order_dish)
                print("\n-----------------------------")
                print("Thank you! The item has been added to your basket.")
                print(f"{basket.view_basket()}")
                print("-----------------------------\n")
            except Exception as error:
                print("Ups!", error)
        case "4":
            try:
                print("\n-----------------------------")
                user_remove_dish = input("What would you like to delete? [name of the dish from the basket]: ")
                basket.remove_basket(user_remove_dish)
                print("Thank you! The item has been deleted from your basket.")
                print(f"{basket.view_basket()}")
                print("-----------------------------\n")
            except Exception as error:
                print("Ups!", error)
        case "5":
            try:
                checkout_choice = input("Are you sure you would like to checkout? [Y/N]: ")
                if checkout_choice == "Y":
                    print("\n-----------------------------")
                    print(basket.view_receipt())
                    print("-----------------------------\n")
                    number_choice = input("Please enter 10 digit phone number to recieve order confirmation: ")
                    confirmation = Confirmation(number_choice)
                    confirmation.send_txt()
                    break
                else:
                    pass
            except Exception as error:
                print("Ups!", error)

print("Thank you for ordering with Amina's restaurant!\nYour order will be with you shortly!")
    