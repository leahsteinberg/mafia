from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml
from emoji import e
from mafia import player_counts, player_join, player_init, clean_text, trigger_beginning
app = Flask(__name__)


game_state = ['joining', 'beginning', 'night', 'dawn', 'day']
game_state = 'joining'


@app.route("/", methods=['GET', 'POST'])
def mafia_game():
  this_number = request.values.get('From', None)
  text_list = clean_text(request.values.get('Body', None))
  if game_state == 'joining':
    print request.values.get('From', None)
    print player_counts.keys()
    if this_number in player_counts.keys() and len(player_counts.keys()) > 0 and text_list[0] == 'begin':
      print "got begin"
      game_state = "beginning"
      trigger_beginning()
      return
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
      if len(player_counts.keys())>0:
	
	name_msg += ". once all players have joined, respond with 'begin' to start the game"
      resp = twilio.twiml.Response()
      resp.message(name_msg)
      return str(resp)



    


if __name__ == '__main__':
  app.run(debug=True)

