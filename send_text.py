from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC45e4ad8468dfcff9c1523bb6c6669e94"
auth_token  = "c93bb585760e697b108c10106883a27d"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="SMOKE SOMETHIN', BITCH",
    to="+18477678112",    # Replace with your phone number
    from_="+18478071786") # Replace with your Twilio number
print message.sid
