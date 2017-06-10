'''Monitor'''
import ConfigParser
import logging
from telegram.ext import Updater, Job
from github import notifications
# Read settings from creds.ini
CONFIG = ConfigParser.RawConfigParser()
CONFIG.read('creds.ini')
TOKEN = CONFIG.get('BOT', 'TOKEN')
CHAT_ID = CONFIG.get('BOT', 'CHAT_ID')

UPDATER = Updater(TOKEN)
j = UPDATER.job_queue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

DISPACTHER = UPDATER.dispatcher

def newAlert(bot, job):
    '''Polls the GitHub API every 2.5 minutes for new notifications.'''
    output = notifications()
    if output is None:
        return
    else:
        bot.sendMessage(chat_id=CHAT_ID, text=output, parse_mode='markdown')

JOB_MINUTE = Job(newAlert, 150.0)
j.put(JOB_MINUTE, next_t=0.0)

UPDATER.start_polling()
UPDATER.idle()
