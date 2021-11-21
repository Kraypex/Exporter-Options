import json
import colorama
import requests
from time import sleep
import sys

from colorama import Fore

colorama.init(autoreset=True)

r = requests.get('https://benbot.app/api/v1/aes')
rr = r.json()
version = rr['version']

print(Fore.GREEN + f"Loaded {version}...\n")

def update():
    assets = requests.get('https://benbot.app/api/v1/files/added').json()
    aes = requests.get('https://benbot.app/api/v1/status').json()
    with open('datas/assets.json', 'w') as file:
        json.dump(assets, file, indent=2)
    with open('datas/Pakchunks.json', 'w') as file:
        json.dump(aes, file, indent=2)

ask = input('Do you want to update the json files?\n(1) Yes\n(2) No\n->>> ')
if ask == '1':
    assets = requests.get('https://benbot.app/api/v1/files/added').json()
    aes = requests.get('https://benbot.app/api/v1/status').json()
    with open('datas/assets.json', 'w') as file:
        json.dump(assets, file, indent=2)
    with open('datas/Pakchunks.json', 'w') as file:
        json.dump(aes, file, indent=2)
        print(Fore.GREEN + f'\nUpdated successfully\n')
        sleep(1)
if ask == '2':
    pass                                         
