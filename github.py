'''Interacts with the GitHub API'''
import os
import json
import textwrap
import requests

BASEURL = "https://api.github.com/notifications"

def get_unique_ids():
    try:
        with open("updated_at.txt", "r") as record:
            unique_id = record.read().split('\n')
            unique_id = list(filter(None, unique_id))
    except Exception:
        unique_id = []

    return unique_id


def build_notification_message(notification, config):
    repo = notification['repository']
    repoName = repo['name']
    repoURL = repo['html_url']
    #repoOwner = repo['owner']['login']
    #repoOwnerURL = repo['owner']['html_url']

    subjectTitle = notification['subject']['title']
    subjectURL = notification['subject']['latest_comment_url']

    html_req = requests.get(url=subjectURL, headers={'Authorization' : config['gittoken']})
    subject_resp = json.loads(html_req.text)
    subjectURL2 = subject_resp['html_url']
    subjectType = notification['subject']['type']

    senderName = subject_resp['user']['login']
    senderName_URL = subject_resp['user']['html_url']
    comment = subject_resp['body']

    message_template = textwrap.dedent("""
    From: [{senderName}]({senderName_URL})
    Repository: [{repoName}]({repoURL})
    Subject: [{subjectTitle}]({subjectURL})
    Body: {comment}
    Type: {subjectType}
    """)

    messageContent = message_template.format(senderName=senderName, senderName_URL=senderName_URL,
                                             repoName=repoName, repoURL=repoURL, 
                                             subjectTitle=subjectTitle, subjectURL=subjectURL2,
                                             comment=comment, subjectType=subjectType)
    return messageContent


def notifications(config):
    """Check GitHub for Notifications"""
    req = requests.get(url=BASEURL, headers={'Authorization' : config['gittoken']})
    notifications = json.loads(req.text)
    unique_id = get_unique_ids()

    messageContent = None
    for notification in notifications:
        if str(notification['updated_at']) not in unique_id:
            unique_id = str(notification['updated_at'])
            messageContent = build_notification_message(notification, config)
            with open('updated_at.txt', 'a') as record:
                record.write (unique_id + '\n')

    return messageContent

if __name__ == '__main__':
    config = os.environ['GITTOKEN']
    notifications(config)
