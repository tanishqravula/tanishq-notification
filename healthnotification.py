import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC43ec2a5124b04a86b9f13c4c55f6aa03"
auth_token = "5cebdd9c91ee848ac117aa2e44fec581"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Family Medical",
  from_="+12765229583",
  to="+917702337176"
)

print(message.sid)
