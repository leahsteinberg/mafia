class Mafia:

  class Player:
    def __init__(self, number):
      self.mafia = False
      self.alive = True
      self.number = number
      self.name = ''
      self.ballot = ''

    def add_name(self, name):
      self.name = name



  def __init__(self):
    self.state = 'join'
    self.player_list = []
    self.min_players = 2
    self.account = "ac8713d29f391c6ccdc9b9942d98a407df"
    self.token = "d36c9a371567932584ad625db360f3be"
    self.client = TwilioRestClient(account, token)
    self.player_count = 0
    
  def send_group(self, group_str, announcement):
    if group_str == 'mafia':
      group = [player for player in self.player_list if player.mafia == True]
    else:
      group = player_list
    for person in group:
      try:
	message = client.sms.messages.create(to=person.number, from_="+17472335925", body=announcement)
      except twilio.twiliorestexception as e:
	print e




	
  def operator(self, text_list, number):
    if self.state == 'join':
      join(text_list, number)
    elif self.state == 'night':
      pass
    elif self.state == 'day':
      pass
    else:
      print "error"

      
  def assign_groups():
    random.shuffle(self.player_list)
    total_players = self.player_count
    number_mafia = self.player_count/3
    for i, player in enumerate(self.player_list):
      if i<number_mafia:
	player.mafia = True
    # TODO more introductory stuff
    self.send_group('mafiosos', "looks like you're in the mafia!")
    self.send_group('innocents', "what mafia????")



  def prune(self):
    pass

  def start_game(self):
    #send instructions (help)
    self.prune()
    self.instructions('all')
    self.assign_groups()

    #assign players and inform them

    #change game state to night
    # beginning of night stuff needs to be called -> transitional method()



  def join(self, word_list, number):
    text_string = ''
    if self.player_count >= self.min_players and 'begin' in word_list:
      self.start_game()
    else:
      if 'begin' in word_list:
	text_string = 'not enough players yet'
      else:
	if not number in [player.number for player in self.player_list]:
	  text_string = "welcome, what's your name?"
	  self.player_list.append(Player(number))
	else:
	  name = word_list[0]
	  if not name in [player.name for player in self.player_list]:
	    this_player = [player for player in self.player_list if player.number == number]
	    this_player.add_name(name)
	    self.player_count +=1
	    text_string = "Welcome to the game, " + name + "."
	    if self.player_count >= self.min_players:
		self.send_group('all', "Sufficient players have joined the game, you may text 'begin' if everyone's here.")# potential issue
	  else:
	    text_string = "we already have someone named that, pick a different name."
	self.send_text(number, text_string)

	
