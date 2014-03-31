
from twilio.rest import TwilioRestClient
townsfolk = []
mafiosos = []
innocents = []
player_counts = {}
groups = {"townsfolk": townsfolk, "mafiosos": mafiosos, "innocents": innocents}
account = "C8713d29f391c6ccdc9b9942d98a407df"
token = "36c9a371567932584ad625db360f3be"
client = TwilioRestClient(account, token)



def send_group(group_str, announcement):
  for person in groups[group_str]:
    message = client.sms.messages.create(to=person.number, from_="+17472335925",
	                                     body=announcement)


def player_join(message):
  new_number = message.values.get('From', None)
  print new_number
  player_counts[new_number] = 0
  print "hiii"
  print player_counts[new_number]
  print "hiii2"
  return "welcome, whats your name"


#   response = twilio.twiml.Response()
#   response.message("Welcome to this little town. Respond with your name.")
  return new_number

def player_init(message):
  text = message.values.get('Body', None)
  for word in text.lower().split():
    if word not in ['hi', 'i', 'am', "i'm", 'im']:
      name = word
      break
  player = Player(name, message.values.get('From', None))
  townsfolk.append(player)
  return player

class Player():
  def __init__(name, number):
    self.mafia = False
    self.alive = True
    self.number = number
    self.name = name
    self.cookie = None


    #initialization:


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
