import telegram
from spotifyPi import *

global UPDATE_ID

# grab a update from the telegram bot
def getUpdate():
    # initialize the Telegram bot
    myToken = '118485406:AAGnai5eQX2c2sEtF0_4sP_FFFtlgrHGdiU'
    bot = telegram.Bot(token=myToken)
    UPDATE_ID = bot.getUpdates()[-1].update_id

    updates = bot.getUpdates(offset=UPDATE_ID, timeout=10)
    for update in updates:
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')
        caseCommands(message)
        UPDATE_ID = UPDATE_ID + 1
        print("command was parsed:" + message)

# for update in updates:
    # print(update.message.text)

def caseCommands(command):
    if command == "/music":
        input2 = command.split(" ")[1]
        mpdInit()
        mpdCommands("playPlaylist", "Welcome to the House")
        if input2 == 'play':
            mpdCommands("playSong", None)
        elif input2 == 'pause':
            mpdCommands("pauseSong", None)
        elif input2 == 'playlist':
            playlist = command.split(" ")[2]
            mpdCommands("playPlaylist", playlist)
        mpdTerminate()
    else:
        return


getUpdate()
