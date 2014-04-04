# SMS Mafia
## Text message-based game of [Mafia] (http://en.wikipedia.org/wiki/Mafia)
This game lets you play the game 'mafia' against at least 6 friends over text message. Players text 1-747-233-5925 to join. Like any small group, once everyone shows up, a small cadre of organized crime emerges. In my game, this game is randomly assigned.During the night, the mafia members can text the number to deliberate (in secret)about which of the other players they want to kill, and cast their votes. Once the mafia reaches a consensus, it's morning and one less innocent citizen remains. During the day time, everyone accuses potential mafia members and casts votes about who to execute. Once there's either only mafia or only innocents left, the game has been won.

Uses a Flask server running on Heroku, as well as the Twilio API.

#### To Do:
* Implement some intense emoji support.
* Allow for multiple games to be played at the same time. The games are already encapsulated in classes, so it will be easy to separate out the games, I just need a way to communicate this to the players.
* Render messages (except for secret Mafia messages) in HTML so there's a way to watch the game online.
