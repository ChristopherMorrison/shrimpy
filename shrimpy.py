from slackclient import SlackClient
import os
import time

sc = SlackClient('xoxb-bot_key_goes_here')


def clear():
    os.system('clear')

def shrimped():
    os.system("figlet 'SHRIMPED BABY'")

def getUsers():
    return sc.api_call('users.list')['members']

def getJessica():
    return [x for x in getUsers() if 'jess' in x['real_name'].lower()]

clear()
while 1:
    connected = sc.rtm_connect();
    while not connected:
        connected = sc.rtm_connect();
        print('connecting')
    Jess = getJessica()[0]
    while 1:
        time.sleep(2)
        messages = sc.rtm_read()
        for message in messages:
            if message['type'] == 'message' and message['user'] == Jess['id']:
                sc.api_call("reactions.add", channel=message['channel'], name="shrimp",  timestamp=message['ts'])
                shrimped()
