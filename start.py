from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect, render_template, session
import twilio.twiml
from emoji import e

import mafia
#from mafia import player_counts, player_join, player_init, clean_text, trigger_beginning

app = Flask(__name__)

game_object = mafia.Mafia()

game_objects = []

session['game_objects'] = game_objects
session['game_counter'] = 0

@app.route("/new_game")
def new_game():

    g_o = mafia.Mafia()
    session['game_counter'] += 1
    session['game_objects'],append({session['game_counter']: g_o })

    return render_template('new_game.html', game_id = session['game_counter'] )


@app.route("/", methods=['GET', 'POST'])
def mafia_game():
    #TODO if someone types help -> they get a help function
    #global mafia.accept_switch
    #global mafia.game_state
    print "~~~~~~~ new incoming text~~~~~~~~~"
    #response_message = "error, I think"
    this_number = request.values.get('From', None)
    text_list = clean_text(request.values.get('Body', None))


    game_object.operator(text_list, this_number)
    #print "in end of flask function"
    # if mafia.game_state == 'joining':
    #   response_message = mafia.joining_logic(text_list, this_number)
    # if mafia.game_state == 'beginning':
    # resp = twilio.twiml.Response()
    # resp.message(response_message)
    # print "TEXT FROM SERVER: ", str(resp)
    return "place holder text message"

@app.route("/restart")
def restart_game():
    game_object.start_game()
    return "place holder text message"



def clean_text(text):
    text = text.lower()
    text_list = text.split()
    return text_list



if __name__ == '__main__':
    app.run(debug=True)

