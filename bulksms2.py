import africastalking

#initialize the sdk
username = "#"
api_key = "#"
africastalking.initialize(username,api_key)

def recipients():
    #list of recipients numbers
    recipients = ["+254746256084"]
    return recipients 

def message():
    #message to be sent 
    message = "huncho in this bitch"
    return message

def init_sms():
    #initialize the service, in our case, SMS
    sms = africastalking.SMS
    return sms 

#USE THE SERVICE
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

#sms.send("Bulk SMS sending, testing phase 2. From PaulWababu", recipients, callback=on_finish)

recipients = recipients()
message = message()

init_sms().send(message, recipients, callback=on_finish)
