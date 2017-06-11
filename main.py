'''Monitor'''
import os
import ConfigParser
import logging
from telegram.ext import Updater, Job
from github import notifications

# Loading environment variables
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

UPDATER = Updater(TOKEN)
j = UPDATER.job_queue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

DISPACTHER = UPDATER.dispatcher

def newAlert(bot, job):
    '''[DEVELOPMENT] Polls the GitHub API every 10 seconds for new notifications.'''
    print 'Polling every 10 seconds'
    output = notifications()
    if output:
    	bot.sendMessage(chat_id=CHAT_ID, text=output, parse_mode='markdown')

JOB_MINUTE = Job(newAlert, 10.0)
j.put(JOB_MINUTE, next_t=0.0)

UPDATER.start_polling()
UPDATER.idle()
