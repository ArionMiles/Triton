'''Monitor'''
import os
import ConfigParser
import logging
#from boto.s3.connection import S3Connection
from telegram.ext import Updater, Job
from github import notifications
# Read settings from creds.ini
#CONFIG = ConfigParser.RawConfigParser()
#CONFIG.read('creds.ini')
TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

UPDATER = Updater(TOKEN)
j = UPDATER.job_queue

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

DISPACTHER = UPDATER.dispatcher

def newAlert(bot, job):
    '''Polls the GitHub API every 2.5 minutes for new notifications.'''
    print 'Polling every 10 seconds'
    output = notifications()
    if output:
    	bot.sendMessage(chat_id=CHAT_ID, text=output, parse_mode='markdown')

JOB_MINUTE = Job(newAlert, 10.0)
j.put(JOB_MINUTE, next_t=0.0)

UPDATER.start_polling()
UPDATER.idle()
