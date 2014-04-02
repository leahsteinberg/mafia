import requests


test_account_sid = "ACec58767d0255847dccc2c2834851802a"
test_auth_token = "6caba219015b82c642bef6d56a87dff2"




thirtyfour = '01234567890123456789012345678901234'

payload = {'MessageSid': thirtyfour, 'SmsSid': thirtyfour, 'AccountSid': 'ACec58767d0255847dccc2c2834851802a', 'From': '+18185218419', 'To': '+17472335925', 'Body': 'Heyyy there!', 'NumMedia': '0'}

r = requests.get("http://127.0.0.1:5000/", params = payload)

