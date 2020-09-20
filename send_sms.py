#READ ME JUUUUUDDDDGGGGEESSSS
#The auth_token may not be valid. Please message 508-685-0814 if this error is occuring. 

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC705f999c86a965d4f4a8db2f4f7fea8b'
auth_token = '8756cbaaba1036256d0679cbc751d300'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Put Message Here',
         from_='+17163174817',
         to='+17158282001'
     )

print(message.sid)
