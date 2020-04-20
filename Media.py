import os
from twilio.rest import Client
#ID AND PASSWORD NEED TO BE ACCESSED FROM TWILIO ACCOUNT
ID="AC7cd11ad6fc1857d9b1982c04f766c2b8"
PASS = "6798b197b8e3e940d63a17fd84ac2add"
client = Client(ID,PASS)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919835633445'

client.messages.create(body='Hello', media_url='https://intense-stream-64362.herokuapp.com/static/images/rishav.jpg',from_ = from_whatsapp_number ,to= to_whatsapp_number)