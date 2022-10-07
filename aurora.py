from random import random
import time
import string
import json
github = "INSERT_GITHUB_REPO"
import subprocess
from pprint import pprint
from urllib import response
fake_card = '{}{}{}{}'.format(*__import__('random').sample(range(1,9),4))
chnames = open("cardholdernames", "r")
content_list = chnames.readlines()
cardnames = [x[:-1] for x in content_list]
chsurnames = open("cardholdernames", "r")
content_list1 = chsurnames.readlines()
cardsurnames = [x[:-1] for x in content_list]
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)
from termcolor import colored, cprint
txt_file = open("names", "r")
content_list = txt_file.readlines()
new_lst = [x[:-1] for x in content_list]
def confirm():
    goback = input("Would you like to go back to the start? [y] [n]: ")
    if goback == "y":
        print("Returning...")
        time.sleep(1)
        loopback()
    else:
        exit()
def loopback():
    
    from cmath import exp
    from asyncio.windows_events import NULL
    from inspect import Traceback
    import os
    from discord_webhook import DiscordWebhook
    import random
    import socket
    import struct
    import sys
    from pythonping import ping
    ip_gen = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
    os.system('cls||clear')
    cprint("""
 ▄▄▄       █    ██  ██▀███   ▒█████   ██▀███   ▄▄▄      
▒████▄     ██  ▓██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒▒████▄    
▒██  ▀█▄  ▓██  ▒██░▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  
░██▄▄▄▄██ ▓▓█  ░██░▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ 
 ▓█   ▓██▒▒▒█████▓ ░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░
  ▒   ▒▒ ░░░▒░ ░ ░   ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░
  ░   ▒    ░░░ ░ ░   ░░   ░ ░ ░ ░ ▒    ░░   ░   ░   ▒   
      ░  ░   ░        ░         ░  ░     ░           ░  ░
""", "magenta")
    cprint("""
[1] - IP Pinger
[2] - IP Generator
[3] - Hostname IP Resolver
[4] - Fake Info Generator
[5] - Discord Webhook Spammer
[6] - Fake Bank Details Generator
[7] - About/Info""", "magenta")
    main = input("> ")

    if main == "1":
        ip_ping = input("Enter IP or Hostname: ")
        try :
            ping(ip_ping, verbose=True)
            ping(ip_ping, verbose=True)
            input("Press anything to continue.")
            os.system('cls||clear')
            loopback()
        except:
            print("Invalid or offline IP.")
            confirm()
            os.system('cls||clear')
    elif main == "2":
        gen_log = 0
        try:
            amount_to_gen = int(input("How many ips you wanna gen? (max 30): "))
        except:
            print("Enter a valid integer.")
            confirm()
            os.system('cls||clear')
        if amount_to_gen>=30:
            print("ERROR: Max 30 at one time.")
            input("Press ENTER to continue.")
            os.system('cls||clear')
            loopback()
        while True:
            if gen_log==amount_to_gen:
                break
            print('{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4)))
            gen_log += 1
        input("Press ENTER to continue.")
        os.system('cls||clear')
        loopback()
    elif main == "3":
        URL_RESOLVER = input("What host to resolve: ")
        try:
            print(f"{URL_RESOLVER}'s IP is {socket.gethostbyname(URL_RESOLVER)}") #uses socket plugin to find hostnames IP
            input("Press ENTER to continue.")
            os.system('cls||clear')
            loopback()
        except:
            print("Not a valid URL.")
            input("Press ENTER to continue.")
            os.system('cls||clear')
            loopback()
    elif main == "4":
        amount_info_genned = 0
        passwordlen = random.randint(4,13)
        try:
            amount_info_to_gen = int(input("How many Fake User:Pass to gen? (max 30): "))
            print(fake_card)
        except:
            print("Amount must be a valid integer.")
            confirm()
            os.system('cls||clear')
        if amount_info_to_gen>=30:
            print("ERROR: Max 30 at one time.")
            input("Press ENTER to continue.")
            os.system('cls||clear')
            loopback()
        while True:
            if amount_info_to_gen==amount_info_genned:
                break
        
            print(''.join(random.choice(new_lst)) + str(random.randint(0,99)) + ":" + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(passwordlen)))
            amount_info_genned += 1
        input("Press ENTER to continue.")
        os.system('cls||clear')
    elif main == "5":
        
        ask_webhook = input("Enter the webhook you want to spam: ")
        ask_spam = input("What you want to spam?: ")
        ask_cooldown = input("Do you want a cooldown on spam? [y] [n]: ")
        if ask_cooldown == "y":
            try:
                cooldown_howmuch = int(input("How much delay? [In seconds]: "))
            except:
                print("Amount must be a valid integer.")
        elif ask_cooldown == "n":
            print("Starting with no cooldown...")
            cooldown_howmuch=0
        else:
            print("Please use 'y' or 'n' [CASE SENSITIVE]")
            input("Press ENTER to continue.")
            os.system('cls||clear')
            loopback()
        try:
            webhook = DiscordWebhook(url=ask_webhook, content=ask_spam)
            while True:
                response = webhook.execute()
                time.sleep(cooldown_howmuch)
            
        except:
            print("Not valid webhook URL.")
            input()
    elif main == "6":
        print("Generator will generate a *FAKE* Card number, CVV, Cardholder name and Expiry date")
        time.sleep(1)
        input("Press ENTER to Generate account.")
        print("GENERATING.....")
        time.sleep(1)
        os.system('cls||clear')
        time.sleep(0.6)
        print("CARDNUM=",'{}{}{}{}'.format(*__import__('random').sample(range(1,9),4)),'{}{}{}{}'.format(*__import__('random').sample(range(1,9),4)),'{}{}{}{}'.format(*__import__('random').sample(range(1,9),4)),'{}{}{}{}'.format(*__import__('random').sample(range(1,9),4)))
        print("CVV=",''.join(["{}".format(random.randint(0, 9)) for num in range(0, 3)]))
        print("CARDHOLDERNAME= "+''.join(random.choice(cardnames)) + " " + ''.join(random.choice(cardsurnames))) #names
        expire = str(random.randint(22,27))
        expire2 = str(random.randint(1,12))
        if len(expire2) == 1:
         expire2="0" + expire2
         expire3 = "[" + expire2 + "/" + expire + "]"
         print("EXPIRY= "+expire3)
        else:
            expire3 = "[" + expire2 + "/" + expire + "]"
            print(expire3)
        time.sleep(1)
        input("Press ENTER to go back to the menu.")
        os.system('cls||clear')
        loopback()
    elif main == "7":
        print(f"AURORA is fully open-sourced and can be found at {github}")
        time.sleep(1)
        print("If you want to change the names on the generator[s], the files that they open are also included.\nKeep the format the same when changing,\nNAME\nNAME\nNAME")
        time.sleep(1)
        print("If something doesn't work or you need help, please open an issue on the github repository")
        input("Press ENTER to continue.")
        os.system('cls||clear')
        loopback()
    else: #if menu input isnt matching 1,2,3... will go back to the start
        print("Unknown input.")
        input("Press ENTER to continue.")
        os.system('cls||clear')
        loopback()
loopback()

    
    
    
        
    
    

    