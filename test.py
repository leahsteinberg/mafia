# ON HEROKU:

# request.values is:  CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([('MessageSid', u'SM614f1398d69aa2fedc01e66b84fc6534'), ('ToCountry', u'US'), ('ApiVersion', u'2010-04-01'), ('ToState', u'CA'), ('ToCity', u'LOS ANGELES'), ('FromZip', u'91042'), ('NumMedia', u'0'), ('To', u'+17472335925'), ('ToZip', u''), ('SmsSid', u'SM614f1398d69aa2fedc01e66b84fc6534'), ('Body', u'Hi'), ('SmsStatus', u'received'), ('SmsMessageSid', u'SM614f1398d69aa2fedc01e66b84fc6534'), ('FromState', u'CA'), ('FromCity', u'LOS ANGELES'), ('FromCountry', u'US'), ('AccountSid', u'AC8713d29f391c6ccdc9b9942d98a407df'), ('From', u'+18185218419')])])


# ON LOCAL HOST:

#   request.values is:  CombinedMultiDict([ImmutableMultiDict([('Body', u'Heyyy there!'), ('MessageSid', u'01234567890123456789012345678901234'), ('From', u'+18185218419'), ('To', u'+17472335925'), ('NumMedia', u'0'), ('AccountSid', u'ACec58767d0255847dccc2c2834851802a'), ('SmsSid', u'01234567890123456789012345678901234')]), ImmutableMultiDict([])])
#   request.values.keys() ['Body', 'MessageSid', 'From', 'To', 'NumMedia', 'AccountSid', 'SmsSid']




import requests, time


test_account_sid = "ACec58767d0255847dccc2c2834851802a"
test_auth_token = "6caba219015b82c642bef6d56a87dff2"

player1 = ['+18185218419', 'Leah']
player2 = ['+18181234567', 'Jane']
player3 = ['+18185551234', 'Ruby']
player4 = ['+12345678909', 'Jill']
player5 = ['+12324134453', 'Betsi']
player6 = ['+23498534355', 'Cynthia']


def send_message(from_number, text_message):
    thirtyfour = '01234567890123456789012345678901234'
    payload = {'MessageSid': thirtyfour, 'SmsSid': thirtyfour, 'AccountSid': 'ACec58767d0255847dccc2c2834851802a',
               'From': from_number, 'To': '+17472335925', 'Body': text_message, 'NumMedia': '0'}
    r = requests.get("http://127.0.0.1:5000/", params=payload)
    time.sleep(2)


send_message(player1[0], 'hi')
send_message(player2[0], 'hi')
send_message(player3[0], 'hi')
send_message(player4[0], 'hi')
send_message(player5[0], 'hi')
send_message(player6[0], 'hi')
send_message(player1[0], player1[1])
send_message(player2[0], player2[1])
send_message(player3[0], player3[1])
send_message(player4[0], player4[1])
send_message(player5[0], player5[1])
send_message(player6[0], player6[1])



#game begins
send_message(player1[0], 'begin')

#mafia deliberates
"""send_message(player1[0], "let's shoot ruby")
send_message(player2[0], "yeah, let's shoot ruby")
send_message(player1[0], "we should murder ruby")
send_message(player1[0], "i agree")

"""
# mafia votes
send_message(player1[0], 'kill jill')
send_message(player2[0], 'I thought we were going after ruby??')
send_message(player1[0], 'kill ruby')
send_message(player2[0], 'kill ruby')
time.sleep(1)
send_message(player1[0], 'kill jane')
send_message(player2[0], 'kill jane')
send_message(player3[0], 'kill jane')
send_message(player4[0], 'kill jane')
send_message(player5[0], 'kill jane')
send_message(player6[0], 'kill jane')
time.sleep(1)

send_message(player1[0], 'kill jill')

send_message(player1[0], "kill Cynthia")
send_message(player5[0], 'kill Leah')
send_message(player3[0], "i am dead but speaking!")
send_message(player6[0], 'kill Leah')

thirtyfour = '01234567890123456789012345678901234'
payload = {'MessageSid': thirtyfour, 'SmsSid': thirtyfour, 'AccountSid': 'ACec58767d0255847dccc2c2834851802a',
               'From': '+18185218419', 'To': '+17472335925', 'Body': '', 'NumMedia': '0'}
r = requests.get("http://127.0.0.1:5000/restart", params=payload)

#send_message(player1[0], 'kill jane')

# time.sleep(2)
#send_message(player2[0], 'kill jane')

# time.sleep(2)
# send_message(player2[0], 'kill jane')
