from twilio.rest import Client
from config import *
from datetime import datetime, timedelta

class Confirmation:
    def __init__(self, phone_number):
        if len(str(phone_number)) < 10:
            raise Exception("The number is too short!")
        self.phone_number = "+44"+ str(phone_number) #fomratXX XXXX XXXX (no 0 at the beginning)

    def delivery_time(self):
        return (datetime.now() + timedelta(minutes = 60)).strftime("%H:%M") 
    
    def message_body(self):
        return f"Thank you for your order!\nWe will deliver before {self.delivery_time()}!"
        
    def send_txt(self):
        try:
            account_sid = twilio_api_key
            auth_token = twilio_auth_token
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to=self.phone_number,
                from_="+447360496023", # twilio test number
                body=self.message_body()
            )
            return True

        except: 
            print("Error! Message has not been send!")
            return False