from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml
from emoji import e
import mafia

app = Flask(__name__)

player_counts = {}
game_state = ['joining', 'beginning', 'night', 'dawn', 'day']
game_state = 'joining'
beginning_players = []


@app.route("/", methods=['GET', 'POST'])
def mafia_game():
  if game_state == 'joining':
    if request.values.get('From', None) not in players_counts:
      player_counts[request.values.get('From', None)] = 0
      new_number = mafia.player_join(request)
    elif player_counts[request.values.get('From', None)] > 0:
      player_init(request)
      send_group('townsfolk', 'can_begin')
  #send message saying that if any of them respond with
	  # a certain phrase, the game will begin, but until then more 
	  #people may join.
    if "begin" in request.values.get('Body', None):
      game_state = 'begin'
  return None
    




  # from_number = request.values.get('From', None)
  # they_sent = request.values.get('Body', None)
  # message = ''
  # if they_sent in e.keys():
  #   message += e[they_sent] + "  "
  # if from_number in callers:
  #   message += callers[from_number]
  # else:
  #   message += u" \U0001F31F"
  # resp = twilio.twiml.Response()
  # resp.message(message)
  # return str(resp)

if __name__ == '__main__':
  app.run(debug=True)

#account_sid = "AC8713d29f391c6ccdc9b9942d98a407df"
#auth_token = "d36c9a371567932584ad625db360f3be"
#client = TwilioRestClient(account_sid, auth_token)
#message = client.messages.create(to ="+18185218419", from_= "+17472335925", body= "hiiiii leah")
