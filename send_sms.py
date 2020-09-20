# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC705f999c86a965d4f4a8db2f4f7fea8b'
auth_token = '8ab513bff8bc70208ffe809ce1a3a20d'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Put Message Here',
         from_='+17163174817',
         to='+17158282001'
     )

print(message.sid)
