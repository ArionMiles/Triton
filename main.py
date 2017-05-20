'''BOT FILE'''
import ConfigParser
import logging
from telegram.ext import Updater, Job
from github import notifications
# Read settings from creds.ini
CONFIG = ConfigParser.RawConfigParser()
CONFIG.read('creds.ini')
TOKEN = CONFIG.get('BOT', 'TOKEN')
CHAT_ID = CONFIG.get('BOT', 'CHAT_ID')
APP_NAME = CONFIG.get('BOT', 'APP_NAME')
#PORT = int(os.environ.get('PORT', '5000'))
UPDATER = Updater(TOKEN)
j = UPDATER.job_queue

# Setting Webhook
'''
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook(APP_NAME + TOKEN)
'''

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

DISPACTHER = UPDATER.dispatcher

# Real stuff
'''def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm a GitHub Issue Tracker!")
'''

def newAlert(bot, job):
    '''Run loop'''
    print "Printing every 10 seconds"
    output = notifications()
    if output is None:
        return
    else:
        print output
        #bot.sendMessage(chat_id=CHAT_ID, text=output, parse_mode='markdown')

JOB_MINUTE = Job(newAlert, 10.0)
j.put(JOB_MINUTE, next_t=0.0)

UPDATER.start_polling()
UPDATER.idle()
