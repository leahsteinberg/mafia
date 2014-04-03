from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml
from emoji import e
import mafiaclass, mafia
#from mafia import player_counts, player_join, player_init, clean_text, trigger_beginning

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def mafia_game():
    #TODO if someone types help -> they get a help function
    #global mafia.accept_switch
    #global mafia.game_state
    print "~~~~~~~ new incoming text~~~~~~~~~"
    #response_message = "error, I think"
    this_number = request.values.get('From', None)
    text_list = mafia.clean_text(request.values.get('Body', None))
    mafiaclass.game_object.operator(text_list, this_number)
    #print "in end of flask function"
    # if mafia.game_state == 'joining':
    #   response_message = mafia.joining_logic(text_list, this_number)
    # if mafia.game_state == 'beginning':

    # resp = twilio.twiml.Response()
    # resp.message(response_message)
    # print "TEXT FROM SERVER: ", str(resp)
    return "place holder text message"


if __name__ == '__main__':
    app.run(debug=True)

