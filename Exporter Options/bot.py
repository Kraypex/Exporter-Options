import json
import requests
import colorama
import time
from time import sleep
import sys
import shutil
from PIL import Image

from colorama import Fore
from requests import get

colorama.init(autoreset=True)

def LocalChunksLoader():
    with open('datas/PakChunks.json', 'r') as aes:
        aes = json.load(aes)
    for i in aes['allPakFiles']:
        if i.startswith('FortniteGame/Content/Paks/'):
            path = i
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}]" + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Loaded: " + Fore.GREEN + path)

def NewOutfitAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/'):
                if i.endswith('Bundle.uasset'):
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)
                else:    
                    path = i
                    print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                    image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                    pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/')[-1])
                    open(f'images/{pathname}.png', 'wb+').write(image.content)

def NewBackblingAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Backpack/'):
                path = i
                print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Backpack/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

def NewPickaxeAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/'):
                path = i
                print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

def NewGliderAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Glider/'):
                path = i
                print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Glider/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

def NewEmoteAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Emotes/'):
                path = i
                print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Emotes/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

def NewBundleAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/'):
                if i.endswith('Bundle.uasset'):
                    path = i
                    print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                    image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                    pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/')[-1])
                    open(f'images/{pathname}.png', 'wb+').write(image.content)
                else:
                    path = i
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)    

def NewWeaponAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Plugins/GameFeatures/CorruptionGameplay/Content/Gameplay/Icons/'):
                if i.endswith('-L.uasset'):
                    path = i
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                    image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                    pathname = (path.split('FortniteGame/Plugins/GameFeatures/CorruptionGameplay/Content/Gameplay/Icons/')[-1])
                    open(f'images/{pathname}.png', 'wb+').write(image.content)
                else:
                    path = i
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)

def NewComsuableAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/Athena/Items/Consumables/PlaysetGrenade/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/Athena/Items/Consumables/PlaysetGrenade/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)                                    

ask = input(f'What do you want to generate?\n(1) Generate New Outfits\n(2) Generate New Backblings\n(3) Generate New Pickaxes\n(4) Generate New Gliders\n(5) Generate New Emotes\n(6) Generate New Bundles\n(7) Generate New Weapons\n(8) Generate New Consumables\n(9) Generate All New Assets\n->>> ')
if ask == '1':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewOutfitAssets()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
    sleep(5)
    sys.exit()
if ask == '2':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewBackblingAssets()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
    sleep(5)
    sys.exit()
if ask == '3':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewPickaxeAssets()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
    sleep(5)
    sys.exit()
if ask == '4':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewGliderAssets()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
    sleep(5)
    sys.exit()
if ask == '5':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewEmoteAssets()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
    sleep(5)
    sys.exit()
if ask == '6':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewBundleAssets()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
    sleep(5)
    sys.exit()    
if ask == '7':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewWeaponAssets()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
    sleep(5)
    sys.exit()
if ask == '8':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    consumable = input('What is the folder name which contains consumable images?\n->>> ')
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)
                end = time.time()
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
                sleep(5)
                sys.exit()                  
if ask == '9':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewOutfitAssets()
    NewBackblingAssets()
    NewPickaxeAssets()
    NewGliderAssets()
    NewEmoteAssets()
    NewBundleAssets()
    NewWeaponAssets()
    consumable = input('What is the folder name which contains consumable images?\n->>> ')
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
        for i in Icons:
            if i.startswith(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)
                end = time.time()
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
                sleep(5)
                sys.exit()     
