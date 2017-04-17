import requests
import json
import ConfigParser
# Read settings from creds.ini
config = ConfigParser.RawConfigParser()
config.read('creds.ini')
#user = config.get('GITHUB', 'username')
#projectName = config.get('GITHUB', 'projectName')
GitToken = config.get('GITHUB', 'GitToken')
headers = {'Authorization' : GitToken}

BASEURL = "https://api.github.com/notifications"
'''messageTitle = None
messageBody = None
messageContent = None
'''
def issue():
    r = requests.get(url=BASEURL, headers=headers)
    dictionary = json.loads(r.text)
    try:
        for i in dictionary:
            #global messageTitle
            messageTitle = i['title']
        for i in dictionary:
            #global messageBody
            messageBody = i['body']
        if messageTitle and messageBody is None:
            messageContent = "Nothing to show."
        else:
            #global messageContent
            messageContent = messageTitle + messageBody
    except IndexError as e:
        print 'IndexError. Reason: "%s"' % str(e)
    except KeyError as e:
        print 'KeyError. Reason: "%s"' % (str(e))
    #output = str(r.text)

    return messageContent
#issue()

if __name__ == '__main__':
    issue()
