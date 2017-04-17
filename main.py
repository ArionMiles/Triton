from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json
import ConfigParser
from github import issue
import logging

# Read settings from creds.ini
config = ConfigParser.RawConfigParser()
config.read('creds.ini')
TOKEN = config.get('BOT', 'TOKEN')
CHAT_ID = config.get('BOT', 'CHAT_ID')
#API_ENDPOINT = "https://api.telegram.org/bot%s/sendMessage" % (TOKEN) 
APP_NAME = config.get('BOT', 'APP_NAME')
#PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)

# Setting Webhook
'''
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook(APP_NAME + TOKEN)
'''
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

dispatcher = updater.dispatcher

# Real stuff
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm a GitHub Issue Tracker!")

def newIssue(bot, update):
	#output = 'FUCK IS THIS SHIT?!'
  output = issue()
  bot.sendMessage(chat_id=update.message.chat_id, text=output)

def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't get that.")


# Handlers
start_handler = CommandHandler('start', start)
newIssue_handler = CommandHandler('issue', newIssue)
unknown_handler = MessageHandler(Filters.command, unknown)
unknown_message = MessageHandler(Filters.text, unknown)

# Dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(newIssue_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(unknown_message)

updater.start_polling()
updater.idle()

#if __name__ == '__main__':
    # service.py executed as script
    # do something
#    newIssue()
