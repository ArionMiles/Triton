import requests
import json
import ConfigParser
# Read settings from creds.ini
config = ConfigParser.RawConfigParser()
config.read('creds.ini')
GitToken = config.get('GITHUB', 'GitToken')
headers = {'Authorization' : GitToken}

BASEURL = "https://api.github.com/notifications"
r = requests.get(url=BASEURL, headers=headers)
#with open('sample.json') as sample:
    #dictionary = json.loads(sample.read())
dictionary = json.loads(r.text)
def notifications2():
    try:
        if dictionary: #Simple check to see response isn't empty
            #Do a loop here
            messageContent = notifications()
            return messageContent
        else:
            return None
        '''if 'id' not in dictionary[0]: #Simple check to see if a key exists in the response
            #Do a loop here
            messageContent = "Empty response!"
            return messageContent
        else:
            messageContent = notifications()
            return messageContent'''
    except IndexError as e:
        print str(e)
def notifications():
    '''Check GitHub for Notifications'''
    '''r = requests.get(url=BASEURL, headers=headers)
    #with open('sample.json') as sample:
    #    dictionary = json.loads(sample.read())
    dictionary = json.loads(r.text)'''
    try:
        for i in dictionary:
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
            '''if messageTitle and messageBody is None:
                messageContent = "Nothing to show."
            else:'''
            messageContent = '\nFrom: [{repoOwner}]({repoOwnerURL}) \
                          \nRepository: [{repoName}]({repoURL})\
                          \nSubject: [{subjectTitle}]({subjectURL})\
                          \nType: {subjectType}' .format(repoOwner = repoOwner, repoOwnerURL=repoOwnerURL,
                                    repoName=repoName, repoURL=repoURL, subjectTitle=subjectTitle, subjectURL=subjectURL,
                                    subjectType=subjectType)    
            #print (messageContent)
    except IndexError as e:
        print 'IndexError. Reason: "%s"' % str(e)
    except KeyError as e:
        print 'KeyError. Reason: "%s"' % (str(e))

    return messageContent

if __name__ == '__main__':
    notifications()
    #this needs fixing