'''Monitor'''
import os
import ConfigParser
import logging
from github import notifications
from telegram.ext import Updater, Job


def get_config():
    token = os.environ['TOKEN']
    chat_id = os.environ['CHAT_ID']
    gittoken = os.environ['GITTOKEN']
    return dict(token=token, chat_id=chat_id, gittoken=gittoken)


def main(config):
    updater = Updater(config['token'])
    j = updater.job_queue

    def newAlert(bot, job):
        '''Polls the GitHub API every 2.5 minutes for new notifications.'''
        output = notifications(config)
        if output:
            bot.sendMessage(chat_id=config['chat_id'], text=output, parse_mode='markdown', \
                disable_web_page_preview=True)

    job_minute = Job(newAlert, 150.0) #Time in seconds
    j.put(job_minute, next_t=0.0)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
    config = get_config()
    main(config)
