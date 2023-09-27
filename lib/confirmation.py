from twilio.rest import Client
from config import *

class Confirmation:
    def __init__(self, phone_number):
        if len(str(phone_number)) < 10:
            raise Exception("The number is too short!")
        if type(phone_number) != int:
            raise Exception("This is not a number!")
        self.phone_number = "+44"+ str(phone_number) #fomrat XX XXXX XXXX (no 0 at the beginning)

    def send_txt(self):
        account_sid = twilio_api_key
        auth_token = twilio_auth_token
        client = Client(account_sid, auth_token)
    
        message = client.messages.create(
            to=self.phone_number,
            from_="+447360496023", # twilio test number
            body="Thank you for your order!\nWe will deliver it within 60 minutes!")

# sms_test = Confirmation("7900479648")