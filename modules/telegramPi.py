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
    print("reached here")
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
        voice("The final exam was mostly in C not C not")
    else:
        return


getUpdate()
