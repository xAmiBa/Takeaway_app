> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.

### class Menu() - CHILD CLASS
-  creates menu list of dictionaries, each representin a dish ex:
{"dish": "Chips", "price": 4.99, "category": "side", "quantity": 0}
-  menu_view() -> list of dishes and prices split in categories

---
> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered. `twilio-python`

### class Confirmation() - CHILD CLASS
- public argument: 10 digit phone number
- send_text() -> sends text with Twilio API confirming the order
---
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.

> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total.
### class Basket() - PARENT CLASS
- add_basket() -> add dictionary to the basket list
- remove_basket() -> remove dictionary from the basket list
- view_basket() -> view dish, item price, quantity and total price
- view_total() -> view total basket price
- update_basket() -> extract all dictionaries with langer quantity than 1
- view_receipt() -> view basket with total price, date and time of order
- time_now() -> time when order has been made
- self.basket -> list of dictionaries