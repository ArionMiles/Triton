'''Import requirements'''
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
    #dictionary = json.loads(sample.read())
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
        for i in DICTIONARY:
            '''Repo Owner Info'''
            repoOwner = i['repository']['owner']['login']
            repoOwnerURL = i['repository']['owner']['url']

            '''Repo Info'''
            repoName = i['repository']['name']
            repoURL = i['repository']['url']

            '''Subject'''
            subjectTitle = i['subject']['title']
            subjectURL = i['subject']['url']
            subjectType = i['subject']['type']
            '''Message'''
            messageContent = '\nFrom: [{repoOwner}]({repoOwnerURL}) \
                          \nRepository: [{repoName}]({repoURL})\
                          \nSubject: [{subjectTitle}]({subjectURL})\
                          \nType: {subjectType}' .format(repoOwner = repoOwner, repoOwnerURL=repoOwnerURL,
                                    repoName=repoName, repoURL=repoURL, subjectTitle=subjectTitle, subjectURL=subjectURL,
                                    subjectType=subjectType)
    except IndexError as E:
        print 'IndexError. Reason: "%s"' % str(E)
    except KeyError as E:
        print 'KeyError. Reason: "%s"' % (str(E))

    return messageContent

if __name__ == '__main__':
    notifications()
    #this needs fixing
