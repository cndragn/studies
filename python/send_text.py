from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC165be7ff82545c34270a64b3ac0d5f0f"
# Your Auth Token from twilio.com/console
auth_token  = "881bddfcf3a5343aeeb4717f67b*****"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13054324789", 
    from_="+16173156470",
    body="Hello from Python!")

print(message.sid)
