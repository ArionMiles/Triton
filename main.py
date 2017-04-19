from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
import requests
import json
import ConfigParser
from github import notifications
import time
import schedule
import logging

# Read settings from creds.ini
config = ConfigParser.RawConfigParser()
config.read('creds.ini')
TOKEN = config.get('BOT', 'TOKEN')
CHAT_ID = config.get('BOT', 'CHAT_ID')
APP_NAME = config.get('BOT', 'APP_NAME')
#PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
j = updater.job_queue

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

def newAlert(bot, job):
    print "Printing every 1 minute."
    output = notifications()
    if output is None:
        return
    else:
        bot.sendMessage(chat_id=CHAT_ID, text=output, parse_mode='markdown')

job_minute = Job(newAlert, 60.0)
j.put(job_minute, next_t=0.0)

updater.start_polling()
updater.idle()
