# CHILD CLASSES:
> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.

### class Menu()
-  creates menu list of dictionaries
-  menu_view() -> list of dishes and prices in categories
---
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.

### class Basket()
- add_basket() -> add Menu() object to the list, choose quantity, if object exists change quantity
- remove_basket() -> remove Menu() object from the list
- view_basket() -> view dish, item price, quantity and total price
- view_total() -> view total basket price
- self.basket -> list of Menu() objects

---
> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total.

### class Receipt()
-  view_receipt() -> formatted receipt with Basket.view_basket() and Basket.view_total()

---
> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered. `twilio-python`

### class Confirmation()
- send_text()

# PARENT CLASS
### class Restaurant()
-  new_order() -> Menu.menu_view(), Basket.add_basket()
-  view_order -> Basket.view_basket(), Basket.view_total()
-  modify_order() -> Basket.add_basket(), Basket.remove_basket()
-  checkout() -> Receipt.view_receipt(), start timer
-  sms_confirmation() -> twilio API send text with estimated time
- SHOULD I MAKE IT SEPARATE CLASS? ^^^^^^^^ YES

Fair warning: protect Twilio API Key from public GitHub repository

## TO CONSIDER:
- connect receipt class with basket class
- no need for mocking integration tests