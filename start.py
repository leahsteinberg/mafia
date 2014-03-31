from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml
from emoji import e
from mafia import player_counts, player_join, player_init
app = Flask(__name__)


game_state = ['joining', 'beginning', 'night', 'dawn', 'day']
game_state = 'joining'


@app.route("/", methods=['GET', 'POST'])
def mafia_game():
  this_number = request.values.get('From', None)
  if game_state == 'joining':
    print request.values.get('From', None)
    print player_counts.keys()
    if not this_number in player_counts.keys():
      print "in thisss"
      join_msg = player_join(request)
      print join_msg
      resp = twilio.twiml.Response()
      resp.message(join_msg)
      return str(resp)
    elif this_number in player_counts.keys(): 
      "in thatttt"
      name = player_init(request, this_number)
      print "did player init"
      name_msg = "I'm gonna say your name is: " + name
      resp = twilio.twiml.Response()
      resp.message(name_msg)
      return str(resp)


      #if(len(mafia.player_counts.keys()>0:


    # elif player_counts[request.values.get('From', None)] > 0:
    #   player_init(request)
    #   send_group('townsfolk', 'can_begin')
  # #send message saying that if any of them respond with
	  # # a certain phrase, the game will begin, but until then more 
	  # #people may join.
    # if "begin" in request.values.get('Body', None):
    #   game_state = 'begin'
  # return None
    




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
