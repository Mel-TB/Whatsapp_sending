import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=os.environ.get('FROM_NUMBER'),
  body='Don\'t forget, you have an meeting in 2 days',
  to=os.environ.get('TO_NUMBER')
)

print(message.sid)


