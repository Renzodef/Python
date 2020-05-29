# Python's version used: 3.8.3 64 bit
# Need to sign up in the Twilio web page:
# https://www.twilio.com/
# Then create a new project and redeem
# the ACCOUNT SID and the AUTH TOKEN by creating a new Python project from there
import os  # standard library
from twilio.rest import Client  # pip install twilio

# Client creation
# Client(ACCOUNT SID, AUTH TOKEN)
# Take the two values from the web site after registration
client = Client('ACCOUNT SID', 'AUTH TOKEN')

# Twilio's number
from_whatsapp_number = 'whatsapp:+14155238886'
# Personal phone number we want to send the message
# This number should be linked by the sandbox
# by following the guides when creating a new project in the web page
# Need to change your_Number with the personal linked number
to_whatsapp_number = 'whatsapp:+your_number'

# Sending the message
client.messages.create(body='Hello World!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)