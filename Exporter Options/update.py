import json
import colorama
import requests
from time import sleep

from colorama import Fore

colorama.init(autoreset=True)

r = requests.get('https://benbot.app/api/v1/aes')
rr = r.json()
version = rr['version']

print(Fore.LIGHTBLUE_EX + f"Loading {version}...")
sleep(0.4)
print(Fore.GREEN + f"Successfully loaded" + Fore.YELLOW + f" [{version}]\n")

print(Fore.BLUE + 'Do you want to update the json files?\n' + Fore.GREEN + '(1) Yes\n' + Fore.RED + '(2) No' + Fore.WHITE)
ask = (input('->>> '))
if ask == '1':
    assets = requests.get('https://benbot.app/api/v1/files/added').json()
    aes = requests.get('https://benbot.app/api/v1/status').json()
    with open('datas/assets.json', 'w') as file:
        json.dump(assets, file, indent=2)
    with open('datas/Pakchunks.json', 'w') as file:
        json.dump(aes, file, indent=2)
        print(Fore.GREEN + f'\nUpdated successfully\n')
        sleep(0)
if ask == '2':
    print(Fore.RED + f'Not updating the json files\n')
    pass
