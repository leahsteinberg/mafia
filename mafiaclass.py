from twilio.rest import TwilioRestClient
import twilio
import random
import math


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

        def __str__(self):
            return self.name


    def __init__(self):
        self.state = 'join'
        self.player_list = []
        self.min_players = 2
        self.account = "ac8713d29f391c6ccdc9b9942d98a407df"
        self.token = "d36c9a371567932584ad625db360f3be"
        self.client = TwilioRestClient(self.account, self.token)
        self.player_count = 0
        self.to_kill = ''


    def send_text(self, number, text_string):
        print "***MSG: ", text_string, "TO: ", number
        try:
            message = self.client.sms.messages.create(to=number, from_="+17472335925", body=text_string)
        except twilio.TwilioRestException as e:
            print e


    def send_group(self, group_str, announcement):
        if group_str == 'mafia':
            group = [player for player in self.player_list if player.mafia]
        elif group_str == 'innocents':
            group = [player for player in self.player_list if not player.mafia]
        else:
            group = self.player_list
        print "**TO GRP: ", group_str, " MSG: ", announcement
        for person in group:
            try:
                message = self.client.sms.messages.create(to=person.number, from_="+17472335925", body=announcement)
            except twilio.TwilioRestException as e:
                print e

    def tally_votes(self, group_str):
        if group_str == 'mafia':
            mafia_list = [player for player in self.player_list if (player.mafia and player.alive)]
            votes = set()
            for mafioso in mafia_list:
                if mafioso.ballot == '':
                    return False
                else:
                    votes.add(mafioso.ballot)
            if len(votes) != 1:
                self.send_group('mafia', "You must reach consensus before someone is killed.")
                return False
            else:
                self.to_kill = votes.pop()
                return True
        elif group_str == 'all':
            print "IN DAYTIME TALLY VOTES"
            votes = []
            alive_people = [player for player in self.player_list if player.alive]
            print "still alive, in tally vote: ", alive_people
            for player in alive_people:
                if player.ballot == '':
                    print "someone didnt vote"
                    return False
                else:
                    votes.append(player.ballot)
            print votes
            minimum_votes = math.ceil(self.get_number_alive() / 2.0)
            print "minimum votes is: ", minimum_votes
            for accused in votes:
                print "accused is: ", accused, "votes.count(accused) is: ", votes.count(accused)
                if votes.count(accused) >= minimum_votes:
                    self.to_kill = accused
                    print "set to kill: ", self.to_kill
                    return True
                    # TODO: send something to tell them to keep voting
            return False

    def get_number_alive(self):
        alive = [p for p in self.player_list if p.alive]
        return len(alive)

    def get_mafia_names(self):
        mafia_names = [player.name for player in self.player_list if player.mafia]
        return mafia_names

    def mafia_wins(self):
        self.send_group('all', 'mafia wins.')
        mafia_string = " ".join(self.get_mafia_names())
        self.send_group('all', "here's who was in the mafia: " + mafia_string)
        self.state = 'end'


    def innocents_win(self):
        self.send_group('all', 'Mafia defeated')
        self.state = 'end'

    def check_end_condition(self):
        mafiosos = [player for player in self.player_list if (player.mafia and player.alive)]
        num_mafiosos = len(mafiosos)
        print "num mafiosos: ", num_mafiosos
        innocents = [player for player in self.player_list if (not player.mafia and player.alive)]
        num_innocents = len(innocents)
        print "num_innocents: ", num_innocents
        if num_innocents > 0 and num_mafiosos > 0:
            return False
        elif num_innocents == 0 and num_mafiosos > 0:
            self.mafia_wins()
            return True
        elif num_mafiosos == 0 and num_innocents > 0:
            self.innocents_win()
            return True
        else:
            return False

    def begin_day(self):
        self.kill_player()
        self.send_group('all', self.to_kill.capitalize() + " was killed last night.")
        self.to_kill = ""
        if self.check_end_condition():
            return
        self.clear_ballots()
        self.send_group('all', "Good morning but someone else has died. Time to accuse the possible mafiosos.")
        self.state = "day"

    def get_player(self, number):
        return [player for player in self.player_list if player.number == number][0]


    def day(self, text_list, number):
        this_player = self.get_player(number)
        if this_player.alive:
            self.send_group('all', this_player.name.capitalize() + " says: " + " ".join(text_list))
            if 'kill' in text_list:
                to_kill = text_list[1]
                if to_kill.lower() in [player.name for player in self.player_list if player.alive]:
                    if this_player.ballot != '':
                        self.send_text(this_player.number,
                                       "You have changed your vote from" + this_player.ballot.capitalize() + " to " + to_kill.capitalize())
                    this_player.ballot = to_kill
                else:
                    self.send_text(this_player.number,
                                   "Not a valid name of someone in to kill: " + to_kill.capitalize())
                if self.tally_votes('all'):
                    print "we want to kill someone during the day"
                    self.begin_night()
                    self.state = 'night'


    def kill_player(self):
        if self.to_kill != '':
            player = [player for player in self.player_list if player.name == self.to_kill][0]
            print "in kill player: ", player.name
            player.alive = False


    def mafia_night(self, text_list, mafioso):
        self.send_group('mafia', mafioso.name.capitalize() + " says: " + " ".join(text_list))
        if 'kill' in text_list:
            to_kill = text_list[1]
            if to_kill.lower() in [player.name for player in self.player_list if not player.mafia and player.alive]:
                if mafioso.ballot != '':
                    self.send_text(mafioso.number,
                                   "you have changed your voted from " + mafioso.ballot + " to " + to_kill)
                mafioso.ballot = to_kill
            else:
                self.send_text(mafioso.number, "not a valid name of someone to kill: " + to_kill)
            if self.tally_votes('mafia'):
                self.begin_day()


    def night(self, text_list, number):
        player = [player for player in self.player_list if player.number == number]
        if player[0].mafia and player[0].alive:
            self.mafia_night(text_list, player[0])
            pass
        else:
            self.send_text(number, "go back to sleep...")


    def operator(self, text_list, number):
        print "in operator, state is: ", self.state
        if self.state == 'join':
            self.join(text_list, number)
        elif self.state == 'night':
            alive = [p.name for p in self.player_list if p.alive]
            new_string = " ".join(alive)
            print "still alive: ", new_string
            self.night(text_list, number)
        elif self.state == 'day':
            alive = [p.name for p in self.player_list if p.alive]
            new_string = " ".join(alive)
            print "still alive: ", new_string
            self.day(text_list, number)
        elif self.state == 'end':
            print "the game is already over"
        else:
            print "error"

    def assign_groups(self):
        random.shuffle(self.player_list)
        total_players = self.player_count
        number_mafia = self.player_count / 3
        if number_mafia == 0:
            number_mafia = 1
        for i, player in enumerate(self.player_list):
            if i < number_mafia:
                player.mafia = True
                print player.name, " is in the mafia."
        self.send_group('mafia', "looks like you're in the mafia!")
        self.send_group('innocents', "what mafia????")

    def help_message(self, who_to_send):
        help_string = "Here's a bunch of introductory instructions."
        if who_to_send == 'all':
            self.send_group('all', help_string)
        else:
            self.send_text(who_to_send.number, help_string)


    def prune(self):
        self.player_list = [player for player in self.player_list if player.name != '']


    def clear_ballots(self):
        print "in clear ballots **"
        for player in self.player_list:
            player.ballot = ''


    def begin_night(self):
        self.kill_player()
        if self.to_kill != '':
            self.send_group('all', "The group has executed: " + self.to_kill)
        self.to_kill = ""
        if self.check_end_condition():
            return
        self.clear_ballots()
        self.send_group('all', "the night has begun.")
        self.send_group('mafia', "During the night, you can converse in secret.")
        self.send_group('mafia', "Text 'kill' and a valid name to cast your vote.")
        to_kill = [player for player in self.player_list if player.mafia == False and player.alive == True]
        kill_string = ''
        for potential_victim in to_kill:
            kill_string += potential_victim.name.capitalize() + "\n"
        self.send_group('mafia', "Here is who you may kill: " + kill_string)
        #self.state = 'night'
        #print "in begin night"


    def start_game(self):
        #send instructions (help)
        self.prune()
        self.help_message('all')
        self.assign_groups()
        self.begin_night()
        self.state = 'night'


    def join(self, word_list, number):
        text_string = ''
        if self.player_count >= self.min_players and 'begin' in word_list:
            self.start_game()
        else:
            if 'begin' in word_list:
                text_string = 'Not enough players yet'
            else:
                if not number in [player.number for player in self.player_list]:
                    text_string = "Welcome, what's your name?"
                    self.player_list.append(self.Player(number))
                else:
                    name = word_list[0]
                    if not name in [player.name for player in self.player_list]:
                        this_player = [player for player in self.player_list if player.number == number]
                        this_player[0].add_name(name)
                        self.player_count += 1
                        text_string = "Welcome to the game, " + name.capitalize() + "."
                        if self.player_count >= self.min_players:
                            self.send_group('all',
                                            "Sufficient players have joined the game, text 'begin' if everyone's here.")
                    else:
                        text_string = "We already have someone named that, pick a different name."
                self.send_text(number, text_string)


game_object = Mafia()
