import json
from pip._vendor import requests


def retrieve_messages(channelid):
    headers = {
        'authorization': '#' 
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    json_input = json.dumps(jsonn, indent=2)
    print(json_input)
    with open('json_data.json', 'w') as outfile:
        outfile.write(json_input)

retrieve_messages('753692831918456903')