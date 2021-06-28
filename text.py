from twilio.rest import Client
account_sid = 'ACb5ee6c357173582ae1c5d14edb65b764'
auth_token = '240609972cbb95ae7f6af684b8527690'
client = Client(account_sid, auth_token)
message = client.messages.create(
    to = '+886908874006',
    from_ = '+19496278330',
    body = 'Hello, I am from your computer'
)
print(message.sid)