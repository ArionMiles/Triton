'''Import requirements'''
import os
import json

import ConfigParser

import requests

# Read settings from creds.ini
CONFIG = ConfigParser.RawConfigParser()
CONFIG.read('creds.ini')
GITTOKEN = CONFIG.get('GITHUB', 'GitToken')
HEADERS = {'Authorization' : GITTOKEN}

BASEURL = "https://api.github.com/notifications"
R = requests.get(url=BASEURL, headers=HEADERS)
#with open('sample.json') as sample:
#    DICTIONARY = json.loads(sample.read())
DICTIONARY = json.loads(R.text)
def notifications():
    '''Main part'''
    try:
        if DICTIONARY: #Simple check to see response isn't empty
            messageContent = notifications2()
            return messageContent
    except IndexError as E:
        print str(E)
def notifications2():
    '''Check GitHub for Notifications'''
    try:
        if not os.path.isfile("notification_id.txt"):
            notif_id=[]

        else:
            with open("notification_id.txt", "r") as f:
                notif_id = f.read()
                notif_id = notif_id.split('\n')
                notif_id = list(filter(None, notif_id))

        for i in DICTIONARY:
            if str(i['id']) not in notif_id:
                '''Repo Owner Info'''
                notif_id = str(i['id'])
                repoOwner = i['repository']['owner']['login']
                repoOwnerURL = i['repository']['owner']['html_url']

                '''Repo Info'''
                repoName = i['repository']['name']
                repoURL = i['repository']['html_url']
                '''Subject'''
                subjectTitle = i['subject']['title']
                subjectURL = i['subject']['latest_comment_url']
                subjectType = i['subject']['type']

                '''Message'''
                messageContent = '\nFrom: [{repoOwner}]({repoOwnerURL}) \
                      \nRepository: [{repoName}]({repoURL})\
                      \nSubject: [{subjectTitle}]({subjectURL})\
                      \nType: {subjectType}' .format(repoOwner = repoOwner, repoOwnerURL=repoOwnerURL,
                                repoName=repoName, repoURL=repoURL, subjectTitle=subjectTitle, subjectURL=subjectURL,
                                subjectType=subjectType)
                f = open('notification_id.txt', 'a')
                f.write (notif_id + '\n')
            else:
                messageContent = None
                #return messageContent

    except IndexError as E:
        print 'IndexError. Reason: %s' % str(E)
    except KeyError as E:
        print 'KeyError. Reason: %s' % (str(E))

    return messageContent
#notifications()
#if __name__ == '__main__':
#    notifications()
    #this needs fixing
