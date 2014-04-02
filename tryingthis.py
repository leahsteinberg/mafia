from twilio.rest import TwilioRestClient

account = "AC8713d29f391c6ccdc9b9942d98a407df"
token = "d36c9a371567932584ad625db360f3be"
client = TwilioRestClient(account, token)



print "client is: ", client
announcement = "hey!"
message = client.sms.messages.create(to='+18185218419', from_="+17472335925", body=announcement)
