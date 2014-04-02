import random
import twilio
from twilio.rest import TwilioRestClient

player_counts = []
fake_list = [0, 1, 2, 3, 4, 5, 6]
groups = {'townsfolk': [], 'mafiosos': [], 'innocents': []}
account = "AC8713d29f391c6ccdc9b9942d98a407df"
token = "d36c9a371567932584ad625db360f3be"
client = TwilioRestClient(account, token)
print "client is: ", client

game_options = ['joining', 'beginning', 'night', 'dawn', 'day']
game_state = 'joining'
accept_switch = False
GROUP_MIN = 2

def joining_logic(text_list, number):
  global accept_switch
  print "this is player counts: ", player_counts
  if accept_switch == True and 'begin' in text_list:
    return trigger_beginning()
  if not number in player_counts:
    return player_join(text_list, number)
  else:
    name_msg = player_init(text_list, number)
    if len(groups['townsfolk']) >= GROUP_MIN:
      name_msg += "Once all the players have joined, start with 'begin'."
      accept_switch = True
      # should text everyone saying they can trigger beginning
      # also text saying the game has begun
      return name_msg



# if accept_switch and text_list[0] == "begin":
#       trigger_beginning()
#     elif not this_number in player_counts.keys():
#       join_msg = player_join(text_list, this_number)
#       resp = twilio.twiml.Response()
#       resp.message(join_msg)
#       print "TEXT1: ", str(resp), '**'
#       return str(resp)
#     elif this_number in player_counts.keys():
#       name = player_init(text_list, this_number)
#       name_msg = "I'm gonna say your name is: " + name
#       if len(player_counts.keys())>0:
# 	name_msg += ". once all players have joined, respond with 'begin' to start the game."
#       resp = twilio.twiml.Response()
#       resp.message(name_msg)
#       accept_switch = True
#       print "TEXT2: ", str(resp)
#       return str(resp)








def send_group(group_str, announcement):
  print "client is: ", client
  for person in groups[group_str]:
    print "sending to: ", person.number, " this: ", announcement
    try:
      message = client.sms.messages.create(to=person.number, from_="+17472335925", body=announcement)
    except twilio.TwilioRestException as e:
      print e



def player_join(message_list, number):
  #global player_counts
  #new_number = message.values.get('From', None)
  player_counts.append(number)
  return "welcome, whats your name"


class Player:
  def __init__(self, number, name):
    self.mafia = False
    self.alive = True
    self.number = number
    self.name = name

def player_init(message_list, number):
  print "in player init"
  name = 'no name'
  for word in message_list:
    if word not in ['hi', 'i', 'am', "i'm", 'im']:
      name = word
      break
  new_player = Player(number, name)
  groups['townsfolk'].append(new_player)
  return "It looks like your name is: "+ name+ ". "

def trigger_beginning():
  assign_groups()
  
  return "The game will now begin."

def clean_text(text):
  text = text.lower()
  text_list = text.split()
  return text_list
  

def assign_groups():
  random.shuffle(groups['townsfolk'])
  total_players = len(groups['townsfolk'])
  number_mafia = total_players/3
  for i, citizen in enumerate(groups['townsfolk']):
    if i<number_mafia:
      groups['mafiosos'].append(citizen)
    else:
      groups['innocents'].append(citizen)
  send_group('mafiosos', "looks like you're in the mafia!")
  send_group('innocents', "what mafia????")







# round: night
#   EVERYONE:
#   say it's night time to everyone:

#   MAFIA:
#   introduce the mafiosos to their secret room:
#   mafiosos have a secret "room" to discuss who they wanna kill
#   once they reach consensus, tell them who they have decided.
#   they can send things to discuss, and when they want to kill someone

#   TOWNSPEOPLE
#   // during night time,, need somethign so all townspeople 
#    are writing something to eachother..?? what would be funny but also keep them
#    // quiet?
#    // need fakey night time thing

#   dawn:

#     send out who got killed

# Day:
#   send good morning to everyone
#   say who died the previous night
#   send the person who died a skull thing
#   discussion
#   then everyone votes
#   if half the players vote to kill a mafioso, that person is eliminated.
