'''Interacts with the GitHub API'''
import os

import json

import ConfigParser

import requests

#from boto.s3.connection import S3Connection

# Read settings from creds.ini
#CONFIG = ConfigParser.RawConfigParser()
#CONFIG.read('creds.ini')
GITTOKEN = os.environ['GitToken']
HEADERS = {'Authorization' : GITTOKEN}
BASEURL = "https://api.github.com/notifications"

def notifications():
    '''Check GitHub for Notifications'''
    req = requests.get(url=BASEURL, headers=HEADERS)
    array = json.loads(req.text)
    if array:
        try:
            if not os.path.isfile("updated_at.txt"):
                unique_id=[]

            else:
                with open("updated_at.txt", "r") as record:
                    unique_id = record.read()
                    unique_id = unique_id.split('\n')
                    unique_id = list(filter(None, unique_id))

            for i in array:
                if str(i['updated_at']) not in unique_id:
                    #Repo Owner Info
                    unique_id = str(i['updated_at'])
                    repoOwner = i['repository']['owner']['login']
                    repoOwnerURL = i['repository']['owner']['html_url']

                    #Repo Info
                    repoName = i['repository']['name']
                    repoURL = i['repository']['html_url']
                   
                    #Subject
                    subjectTitle = i['subject']['title']
                    subjectURL = i['subject']['latest_comment_url']
                    html_req = requests.get(url=subjectURL, headers=HEADERS)
                    reqdict = json.loads(html_req.text)
                    subjectURL2 = reqdict['html_url']
                    subjectType = i['subject']['type']

                    #Message Content
                    messageContent = '\nFrom: [{repoOwner}]({repoOwnerURL}) \
                      \nRepository: [{repoName}]({repoURL})\
                      \nSubject: [{subjectTitle}]({subjectURL})\
                      \nType: {subjectType}' .format(repoOwner = repoOwner, repoOwnerURL=repoOwnerURL,
                        repoName=repoName, repoURL=repoURL, subjectTitle=subjectTitle, subjectURL=subjectURL2,
                        subjectType=subjectType)
                    record = open('updated_at.txt', 'a')
                    record.write (unique_id + '\n')
                else:
                    messageContent = None

        except IndexError as E:
            print 'IndexError. Reason: %s' % str(E)
        except KeyError as E:
            print 'KeyError. Reason: %s' % (str(E))

        return messageContent

if __name__ == '__main__':
    notifications()
