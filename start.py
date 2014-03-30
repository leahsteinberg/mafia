from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
callers = {"+18185218419": "leahrose"}


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
  from_number = request.values.get('From', None)
  if from_number in callers:
    message = callers[from_number] + u" \U0001F31F"
  else:
    message = u" \U0001F31F"
  resp = twilio.twiml.Response()
  resp.message(message)
  return str(resp)

if __name__ == '__main__':
  app.run(debug=True)

#account_sid = "AC8713d29f391c6ccdc9b9942d98a407df"
#auth_token = "d36c9a371567932584ad625db360f3be"
#client = TwilioRestClient(account_sid, auth_token)
#message = client.messages.create(to ="+18185218419", from_= "+17472335925", body= "hiiiii leah")
