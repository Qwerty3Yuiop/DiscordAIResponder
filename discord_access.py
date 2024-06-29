import json
import requests
import os
import re


class DiscordChannel:
    headers = None
    channel = None

    def __init__(self, channel):
        self.headers = {"Authorization" : os.environ["DISCORD_AUTH_KEY"]}
        self.channel = f"https://discord.com/api/v9/channels/{channel}/messages"

    def searchHistory(self, num:int=1) -> list:
        messageList = []
        r = requests.get(self.channel, headers=self.headers)
        jsonn = json.loads(r.text)
        for count, entry in enumerate(jsonn):
            if count == num:
                break
            messageList.append(entry)
        return messageList
    
    def sendMsg(self, message):
        payload = {"content" : message}
        res = requests.post(self.channel, payload, headers=self.headers)
        return res.__str__()
