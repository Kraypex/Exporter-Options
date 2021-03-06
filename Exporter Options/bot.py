import json
import requests
import colorama
import time
import sys, os
import glob
import math
import tweepy
import platform
from PIL import Image
from time import sleep
from math import ceil, sqrt
from typing import Union

from colorama import Fore

colorama.init(autoreset=True)

x = platform.system()
if x == 'Windows':
    import pyfiglet
    ascii_banner = pyfiglet.figlet_format("EXPORTER OPTIONS", font = "slant")
    print(Fore.CYAN + ascii_banner + Fore.RESET)
    time.sleep(2)
    print('Loading...')
    os.system("cls")
    os.system(
    "TITLE Exporter Options")
    os.system('cls' if os.name=='nt' else 'clear')

r = requests.get('https://benbot.app/api/v1/status')
rr = r.json()
version = rr['currentFortniteVersion']

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

def LocalChunksLoader():
    with open('datas/PakChunks.json', 'r') as aes:
        aes = json.load(aes)
    for i in aes['allPakFiles']:
        if i.startswith('FortniteGame/Content/Paks/'):
            path = i
            pathname = (path.split('FortniteGame/Content/Paks/')[-1])
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}]" + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Loaded: " + Fore.GREEN + pathname)

def NewOutfitAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/T-AthenaSoldiers'): 
            path = i
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getoutfit = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getoutfit,(20,5),mask=getoutfit)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')

def NewBackblingAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Backpack/'):
            path = i
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Backpack/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getbackbling = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getbackbling,(20,5),mask=getbackbling)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')

def NewPickaxeAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/'):
            path = i
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getpickaxe = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getpickaxe,(20,5),mask=getpickaxe)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')

def NewGliderAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Glider/'):
            path = i
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Glider/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getglider = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getglider,(20,5),mask=getglider)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')

def NewEmoteAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith('FortniteGame/Content/UI/Foundation/Textures/Icons/Emotes/'):
            if i.endswith('-L.uasset'):
                path = i
                print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/Icons/Emotes/')[-1])
                open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
                getemote = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
                blackimg = Image.open(f'datas/blackimg.png')
                blackimg.paste(getemote,(20,5),mask=getemote)
                blackimg.save(f'images/{pathname}.png')
                os.remove(f'datas/cache/{pathname}.png')
            else:
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)

def NewEmojiAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith('FortniteGame/Content/2dAssets/Emoji/Season18/'):
            path = i
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split('FortniteGame/Content/2dAssets/Emoji/Season18/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getemoji = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getemoji,(20,5),mask=getemoji)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')             

def NewBundleAssets():
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/T-AthenaBundles'):
            path = i
            print(Fore.YELLOW + f" [{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getbundle = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getbundle,(20,5),mask=getbundle)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')


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
                open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
                getweapon = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
                blackimg = Image.open(f'datas/blackimg.png')
                blackimg.paste(getweapon,(20,5),mask=getweapon)
                blackimg.save(f'images/{pathname}.png')
                os.remove(f'datas/cache/{pathname}.png')
            else:
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)

def large_merger( datas: Union[list, None] = None, save_as: str = 'merged.jpg'):
    if not datas:
        datas = [Image.open(i) for i in glob.glob('images/*.png')]

    row_n = len(datas)
        
    rowslen = ceil(sqrt(row_n))
    columnslen = round(sqrt(row_n))

    mode = "RGB"

    rows = rowslen * 1024 # X VALUE
    columns = columnslen * 1024 # Y VALUE
    image = Image.new(mode, (rows, columns))

    i = 0

    for card in datas:
        image.paste(
            card,
            ((0 + ((i % rowslen) * card.width)),
                (0 + ((i // rowslen) * card.height)))
        )

        i += 1

    if save_as and len(save_as) > 4:
        image.save(f"merged/{save_as}")
        image.show()

    return image

def compress():
    foo = Image.open(f"merged/merged.jpg")
    x, y = foo.size
    x2, y2 = math.floor(x/2), math.floor(y/2)
    foo = foo.resize((x2,y2),Image.ANTIALIAS)
    foo.save(f"merged/merged.jpg",quality=65)

def tweet():
    with open("twitterkeys.json", "r+") as token:
        tokens = json.load(token)
    consumer_key = tokens['data']['API_key']
    consumer_secret_key = tokens['data']['API_Secret_Key']
    access_token = tokens['data']['Access_Token']
    access_token_secret = tokens['data']['Access_Token_Secret']
    if consumer_key == "" or consumer_secret_key == "" or access_token == "" or access_token_secret == "" :
        print(Fore.RED + "Please check your token's in your twitterkeys.json file! Token's are missing!")
        time.sleep(5)
        exit()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Upload image
    media = api.media_upload("merged/merged.jpg")
 
    # Post tweet with image
    tweet = "New Cosmetics! #Fortnite"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

print(f'What do you want to generate?\n' + Fore.CYAN + f'(1) Generate New Outfits\n(2) Generate New Backblings\n(3) Generate New Pickaxes\n(4) Generate New Gliders\n(5) Generate New Emotes and New Emojis\n(6) Generate New Bundles\n(7) Generate New Weapons\n(8) Generate New Consumables\n' + Fore.LIGHTBLUE_EX + f'(9) Generate All New Assets\n' + Fore.LIGHTRED_EX + f'(10) Delete all images in images folder' + Fore.WHITE)
ask = (input("->>> "))
if ask == '1':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewOutfitAssets()
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()
if ask == '2':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewBackblingAssets()
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()
if ask == '3':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewPickaxeAssets()
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()
if ask == '4':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewGliderAssets()
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()
if ask == '5':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewEmoteAssets()
    NewEmojiAssets()
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()    
if ask == '6':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewBundleAssets()
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()    
if ask == '7':
    start = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Inizialing...")
    LocalChunksLoader()
    NewWeaponAssets()
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()
if ask == '8':
    start = time.time()
    consumable = input('What is the folder name which contains consumable images? Ex: FortniteGame/Content/Athena/Items/Consumables/{consumablename}/. Enter only name not path!\n->>> ')
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/'):
            path = i
            print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getcon = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getcon,(20,5),mask=getcon)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')
            end = time.time()
            print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")
            sleep(5)
            sys.exit()
        else:
            print(Fore.RED + "Couldn't find any consumables in the json file or you maybe entered a wrong name...")
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
    NewEmojiAssets()
    NewBundleAssets()
    NewWeaponAssets()
    consumable = input('What is the folder name which contains consumable images? Ex: FortniteGame/Content/Athena/Items/Consumables/{consumablename}/. Enter only name not path!\n->>> ')
    with open('datas/assets.json', 'r') as Icons:
        Icons = json.load(Icons)
    for i in Icons:
        if i.startswith(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/'):
            path = i
            print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
            image = requests.get(f'https://benbot.app/api/v1/exportAsset?path={path}')
            pathname = (path.split(f'FortniteGame/Content/Athena/Items/Consumables/{consumable}/')[-1])
            open(f'datas/cache/{pathname}.png', 'wb+').write(image.content)
            getcon = Image.open(f'datas/cache/{pathname}.png').resize((1024,1024))
            blackimg = Image.open(f'datas/blackimg.png')
            blackimg.paste(getcon,(20,5),mask=getcon)
            blackimg.save(f'images/{pathname}.png')
            os.remove(f'datas/cache/{pathname}.png')
    else:
        print(Fore.RED + "Couldn't find any consumables in the json file or you maybe entered a wrong name...")
    large_merger()
    compress()
    tweet()
    end = time.time()
    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)} seconds.")
    sleep(5)
    sys.exit()
if ask == '10':
    delete_files = glob.glob('images/*')
    for file in delete_files:
        os.remove(file)
    print(Fore.GREEN + f'\nSuccessfully deleted all images in images folder\n')
    sleep(5)
else:
    print(Fore.RED + f'Invalid input...')
