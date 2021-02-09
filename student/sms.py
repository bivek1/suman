from twilio.rest import Client

account_sid = 'AC5256ed3c1f0dadefa20d4047424809ae' # Found on Twilio Console Dashboard
auth_token = '0784f317c7e31c5d1f1b6721bd63ec9b' # Found on Twilio Console Dashboard

 # Phone number you used to verify your Twilio account
TwilioNumber = '+15405072533' # Phone number given to you by Twilio

def sendSms(number, message):
    client = Client(account_sid, auth_token)
    myPhone = '+977'+number
    client.messages.create(
    to=myPhone,
    from_=TwilioNumber,
    body= message)
    
    
