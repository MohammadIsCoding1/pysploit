#----------------------------------------
#authour - AnOnYmOuS
#criedits - in the credit file
#start date - april 29 2021
#release date - still in progress
#----------------------------------------

import nmap
import datetime
import os, platform
import pyautogui
import os
import requests
import random
import string
import socket
import re
import threading
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore, Back, Style


spam=1

print('testing')
banner='''
██████╗░██╗░░░██╗░██████╗██████╗░██╗░░░░░░█████╗░██╗████████╗
██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝
██████╔╝░╚████╔╝░╚█████╗░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░
██╔═══╝░░░╚██╔╝░░░╚═══██╗██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░
██║░░░░░░░░██║░░░██████╔╝██║░░░░░███████╗╚█████╔╝██║░░░██║░░░
╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░
                    ____________________________
  ------------------|   Payload: 1             |]
                   [|          Hax: 10         |]
                   [|__________________________|------------------
'''+"       "+str(datetime.datetime.now())
print(banner)

command_input=input("con_hac> ")

if command_input=="webrunhttp":
    website_choise=input('Website : ')

    for_requests=requests.get(website_choise)
    print(for_requests)

    while (for_requests):
        for_requests=requests.get(website_choise)
        print(for_requests)

        while (for_requests):
            spam += 1
            print('*[Sending Requests To] '+website_choise +': '+str(spam))

if command_input=="quit":
    sure=input('are you sure you wanna exit [y]or[n] : ')
    if sure=='y':
        exit()

    if sure=='n':
        command_input=str(input("con_hac> "))


if command_input=="powershell":
  pyautogui.hotkey('win', 'r')
  sleep(0.3)

  pyautogui.write('powershell')
  sleep(0.3)

  pyautogui.hotkey('enter')
  sleep(0.3)

  pyautogui.alert("POWERSHELL OPENED")

  command_input=input("con_hac> ")


if command_input=="cmd":

  pyautogui.hotkey('win', 'r')
  sleep(0.3)

  pyautogui.write('cmd')
  sleep(0.3)

  pyautogui.hotkey('enter')
  sleep(1.5)

  pyautogui.alert("CMD OPENED")

  command_input=input("con_hac> ")

if command_input=="cmd":
  pyautogui.hotkey('win', 'r')
  pyautogui.write('cmd')

  command_input=input("con_hac> ")

if command_input=="f_email":
  a = random.choice(string.ascii_letters)
  b = random.choice(string.ascii_letters)
  c = random.choice(string.ascii_letters)
  d = random.choice(string.ascii_letters)
  e = random.choice(string.ascii_letters)
  f = random.choice(string.ascii_letters)
  g = random.choice(string.ascii_letters)
  h = random.choice(string.ascii_letters)
  i = random.choice(string.ascii_letters)
  print(a+b+c+d+e+f+g+h+i+'@gmail.com')

  command_input=input("con_hac> ")

if command_input=="f_password":
  a = random.choice(string.ascii_letters)
  b = random.choice(string.ascii_letters)
  c = random.choice(string.ascii_letters)
  d = random.choice(string.ascii_letters)
  e = random.choice(string.ascii_letters)
  f = random.choice(string.ascii_letters)
  g = random.choice(string.ascii_letters)
  h = random.choice(string.ascii_letters)
  i = random.choice(string.ascii_letters)
  print(a+b+c+d+e+f+g+h+i)

  command_input=input("con_hac> ")

if command_input=="clr":
    os.system('cls')

    command_input=input("con_hac> ")

if command_input=="//ip":
  os.system('ipconfig')

  command_input=input("con_hac> ")

if command_input=="help":
  help=open('help.txt', 'r')
  print(help.read())

  command_input=str(input("con_hac> "))

if command_input=="licence":
    licence=open('licence.txt', 'r')
    print(licence.read())

    command_input=str(input("con_hac> "))

while (command_input==command_input):
    command_input=input("con_hac> ")
    if command_input=="powershell":
      pyautogui.hotkey('win', 'r')
      sleep(0.3)

      pyautogui.write('powershell')
      sleep(0.3)

      pyautogui.hotkey('enter')
      sleep(0.3)

      pyautogui.alert("POWERSHELL OPENED")

      command_input=input("con_hac> ")


    if command_input=="cmd":

      pyautogui.hotkey('win', 'r')
      sleep(0.3)

      pyautogui.write('cmd')
      sleep(0.3)

      pyautogui.hotkey('enter')
      sleep(1.5)

      pyautogui.alert("CMD OPENED")

      command_input=input("con_hac> ")

    if command_input=="cmd":
      pyautogui.hotkey('win', 'r')
      pyautogui.write('cmd')

      command_input=input("con_hac> ")

    if command_input=="f_email":
      a = random.choice(string.ascii_letters)
      b = random.choice(string.ascii_letters)
      c = random.choice(string.ascii_letters)
      d = random.choice(string.ascii_letters)
      e = random.choice(string.ascii_letters)
      f = random.choice(string.ascii_letters)
      g = random.choice(string.ascii_letters)
      h = random.choice(string.ascii_letters)
      i = random.choice(string.ascii_letters)
      print(a+b+c+d+e+f+g+h+i+'@gmail.com')

      command_input=input("con_hac> ")

    if command_input=="f_password":
      a = random.choice(string.ascii_letters)
      b = random.choice(string.ascii_letters)
      c = random.choice(string.ascii_letters)
      d = random.choice(string.ascii_letters)
      e = random.choice(string.ascii_letters)
      f = random.choice(string.ascii_letters)
      g = random.choice(string.ascii_letters)
      h = random.choice(string.ascii_letters)
      i = random.choice(string.ascii_letters)
      print(a+b+c+d+e+f+g+h+i)

      command_input=input("con_hac> ")

    if command_input=="clr":
        os.system('clear')

        command_input=input("con_hac> ")

    if command_input=="//ip":
      os.system('ip addr')

      command_input=input("con_hac> ")

    if command_input=="help":
      help=open('help.txt', 'r')
      print(help.read())

      command_input=str(input("con_hac> "))

    if command_input=="licence":
        licence=open('licence.txt', 'r')
        print(licence.read())

        command_input=str(input("con_hac> "))

    if command_input=="webrunhttp":
        website_choise=input('Website : ')

        for_requests=requests.get(website_choise)
        print(for_requests)

        while (for_requests):
            for_requests=requests.get(website_choise)
            print(for_requests)

            while (for_requests):
                spam+=1
                print('*[Sending Requests To] '+website_choise +' '+spam)

    if command_input=="show payload":
        print('Payload/send/web_script')

    if command_input=="use Payload/send/web_script":
        command_input=input('con_hac/Payload/send/web_script> ')

        while True:
            command_input=input('con_hac/Payload/send/web_script> ')
            if command_input=="xss vuln":
                target=raw_input('Url > ')

                payload="<script>alert(XSS);<script>"

                req=requests.post(target + payload)

                if payload in req.text:
                    print("XSS vulnerability discovered!")
                    print("attacking payload : "+payload)
                    command_input=str(input('con_hac/Payload/send/web_script> '))
                else:
                    print("secure")
                    command_input=str(input('con_hac/Payload/send/web_script> '))
            
                if command_input=="ping":
                    try:
                        IP=input('IP : ')
                        os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                        while (host):
                            os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    
                    except:
                        command_input=str(input('con_hac/Payload/send/web_script> '))

                if command_input=="ping --limit":
                    try:
                        limit=input('The Limit : ')
                        IP=input('IP : ')

                        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                        print(ping)

                        while (ping):
                            ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                            print(ping)
                            sleep(float(limit))
                    
                    except:
                        command_input=str(input('con_hac/Payload/send/web_script> '))
                
                if command_input=="clr":
                    os.system('clear')

                    command_input=str(input('con_hac/Payload/send/web_script> '))
                
                if command_input=="return":
                    command_input=str(input('con_hac/Payload/send/web_script> '))
                
                if command_input=="//ip":
                    os.system('ip addr')
                    command_input=str(input('con_hac/Payload/send/web_script> '))

    if command_input=="show hax":
        print('Hax/web/ip | Run It : use Hax/web/ip'+"\n"+"Description: Find The IP Address Of A Website\n")
        print('Hax/copy/web | Run It : use Hax/copy/web'+"\n"+"Description: Make A Phishing Website To Get Details\n")
        print('Hax/email/bomb | Run It: use Hax/email/bomb'+"\n"+"Description: Spam Someone's Inbox Of Email\n")
        print('Hax/web/scraping | Run It: use Hax/web/scraping'+"\n"+"Description: Scrap Any Website\n")
        print('Hax/pass/attack | Run It: use Hax/pass/attack'+"\n"+"Description: Do a Dictionary Or Brute Force Attack\n")
        print('Hax/network/scan | Run It: use Hax/network/scan'+"\n"+"Description: Port Scanner\n")
        print('Hax/make/server | Run It: use Hax/make/server'+"\n"+"Description: Make a server choose port\n")
        print('Hax/make/fil | Run It: use Hax/make/file_text'+"\n"+"Description: Make any file type\n")
        print('Hax/make/dir | Run It: use Hax/make/directory'+"\n"+"Description: make a directory\n")
        print('Hax/network/find-vuln | Run It: Hax/network/find-vuln'+"\n"+"Description: find vulns in a network")
        command_input=str(input("con_hac> "))
    
    if command_input=="use Hax/make/dir":

        while True:
            command_input==str(input('con_hac/Hax/make/dir > '))

            if command_input=="make dir":
                dir_name=input('directory_name : ')
                os.system('mkdir '+dir_name)

                command_input==str(input('con_hac/Hax/make/dir> '))
            
            if command_input=="ping --limit":
                try:
                    limit=input('The Limit : ')
                    IP=input('IP : ')

                    ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    print(ping)

                    while (ping):
                        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                        print(ping)
                        sleep(float(limit))
                
                except:
                    command_input==str(input('con_hac/Hax/make/dir> '))
            
            if command_input=="clr":
                os.system('clear')

                command_input==str(input('con_hac/Hax/make/dir> '))
            
            if command_input=="return":
                command_input==str(input('con_hac/Hax/make/dir> '))
            
            if command_input=="//ip":
                os.system('ip addr')
                command_input==str(input('con_hac/Hax/make/dir> '))

    if command_input=="use Hax/network/scan":
        pass
        
    if command_input=="use Hax/pass/attack":
        command_input=str(input("con_hac/Hax/pass/attack> "))

        while True:
            command_input=str(input("con_hac/Hax/pass/attack> "))

            if command_input=="brute_all":
                exec(open('pysploit_brut.py').read())

            if command_input=="dict_attack":
                print("""
                1. md5
                2. sha256
                3. sha512
                4. sha1
                5. sha2""")

                dict_choise=input('> ')

                if dict_choise=='1':
                    exec(open('pysploit_dictionary_md5.py'))
                    command_input=str(input("con_hac/Hax/pass/attack> "))

                if dict_choise=='2':
                    exec(open('pysploit_dictionary_256.py'))
                    command_input=str(input("con_hac/Hax/pass/attack> "))

                if dict_choise=='3':
                    exec(open('pysploit_dictionary_sha512.py'))
                    command_input=str(input("con_hac/Hax/pass/attack> "))

                if dict_choise=='4':
                    exec(open('pysploit_dictionary_sha1.py'))
                    command_input=str(input("con_hac/Hax/pass/attack> "))

                if dict_choise=='5':
                    exec(open('pysploit_dictionary_sha2.py'))
                    command_input=str(input("con_hac/Hax/pass/attack> "))

                if command_input=="ping":
                    try:
                        IP=input('IP : ')
                        os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                        while True:
                            os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    
                    except:
                        command_input=str(input("con_hac/Hax/pass/attack> "))

                if command_input=="ping --limit":
                    try:
                        limit=input('The Limit : ')
                        IP=input('IP : ')

                        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                        print(ping)

                        while (ping):
                            ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                            print(ping)
                            sleep(float(limit))
                    
                    except:
                        command_input=str(input("con_hac/Hax/pass/attack> "))
                
                if command_input=="clr":
                    os.system('clear')

                    command_input=str(input("con_hac/Hax/pass/attack> "))
                
                if command_input=="return":
                    command_input=str(input("con_hac> "))
                
                if command_input=="//ip":
                    os.system('ip addr')

                    command_input=str(input("con_hac/Hax/pass/attack> "))

    if command_input=="use Hax/web/scraping":
        command_input=str(input("con_hac/Hax/web/scraping > "))


        while True:
            command_input=str(input("con_hac/Hax/web/scraping > "))
            
            if command_input=="ping":
                try:
                    IP=input('IP : ')
                    os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                    while True:
                        os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
            
                except:
                    command_input=str(input("con_hac/Hax/web/scraping > "))

            if command_input=="ping --limit":
                try:
                    limit=input('The Limit : ')
                    IP=input('IP : ')

                    ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    print(ping)

                    while (ping):
                        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                        print(ping)
                        sleep(float(limit))
            
                except:
                    command_input=str(input("con_hac/Hax/web/scraping > "))
        
            if command_input=="clr":
                os.system('clear')

                command_input=str(input("con_hac/Hax/web/scraping > "))
        
            if command_input=="return":
                command_input=str(input("con_hac> "))

            if command_input=="//ip":
                os.system('ip addr')

                command_input=str(input("con_hac/Hax/pass/attack> "))

            if command_input=="quickscr":
                website=input('Website > ')

                data=requests.get(website)

                phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
                emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

                print(phones, emails)

                command_input=command_input=str(input("con_hac/Hax/web/scraping > "))

            if command_input=="lotscrp":

                website=input('Website > ')
                data=requests.get(website)

                soup=BeautifulSoup(data.text, 'html.parser')

                data=[]
                for tr in soup.find_all('tr'):
                    values=[td.text for td in tr.find_all('td')]
                    data.append(values)
                print(data)

                command_input=str(input("con_hac/Hax/web/scraping > "))


    if command_input=="use Hax/web/ip":
        command_input=input("con_hac/Hax/web/ip> ")

        while True:
            command_input=str(input("con_hac/Hax/web/ip> "))

            if command_input=="webgeturl":
                url=input('Website > ')
                print(socket.gethostbyname(url))

                command_input=str(input("con_hac/Hax/web/ip> "))

            if command_input=="webgeturl rapid":
                try:
                    url=input('Website > ')
                    print(socket.gethostbyname(url))

                    while (url):
                        url=input('Website > ')
                        print(socket.gethostbyname(url))

                except:
                    command_input=str(input("con_hac/Hax/web/ip> "))


            if command_input=="ping":
                try:
                    IP=input('IP : ')
                    os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                    while True:
                        os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    
                except:
                    command_input=str(input("con_hac/Hax/web/ip> "))

            if command_input=="ping --limit":
                try:
                    limit=input('The Limit : ')
                    IP=input('IP : ')

                    ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    print(ping)

                    while (ping):
                        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                        print(ping)
                        sleep(float(limit))
                
                except:
                    command_input=str(input("con_hac/Hax/web/ip> "))
            
            if command_input=="clr":
                os.system('clear')

                command_input=str(input("con_hac/Hax/web/ip> "))
            
            if command_input=="return":
                command_input=str(input("con_hac> "))
            
            if command_input=="//ip":
                os.system('ip addr')

                command_input=str(input("con_hac/Hax/web/ip> "))


    if command_input=="use Hax/copy/web":
        command_input=str(input("con_hac/Hax/copy/web> "))

        while True:
            command_input=str(input("con_hac/Hax/copy/web> "))

            if command_input=="sendwebfile":
                url = input('Webpage to grab source from: ')
                html_output_name = input('Name for html file: ')

                req = requests.get(url, 'html.parser')

                with open(html_output_name, 'w') as f:
                    f.write()
                    f.close()

                print('now you have a copy of a web')
                command_input=str(input("con_hac/Hax/copy/web> "))

            
            if command_input=="ping":
                try:
                    IP=input('IP : ')
                    os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                    while True:
                        os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                
                except:
                    command_input=str(input("con_hac/Hax/copy/web> "))

            if command_input=="ping --limit":
                try:
                    limit=input('The Limit : ')
                    IP=input('IP : ')

                    ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    print(ping)

                    while (ping):
                        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                        print(ping)
                        sleep(float(limit))
                
                except:
                    command_input=str(input("con_hac/Hax/copy/web> "))
            
            if command_input=="clr":
                os.system('clear')

                command_input=str(input("con_hac/Hax/copy/web> "))
            
            if command_input=="return":
                command_input=str(input("con_hac> "))
            
            if command_input=="//ip":
                os.system('ip addr')

                command_input=str(input("con_hac/Hax/copy/web> "))
        
    if command_input=="use Hax/email/bomb":
        command_input=str(input('con_hac/Hax/email/bomb>'))

        while True:
            command_input=str(input('con_hac/Hax/email/bomb>'))
        
            if command_input=="email_bomb --limit":
                limit=input('Spam Times > ')
                email=input('your email : ')
                password_email=input('your password : ')
                msg=input('what message : ')

                for i in range(limit):
                    pass
            
            
            if command_input=="email_bomb --time_limit":
                time_limit=input('Time : ')
                email=input('your email : ')
                password_email=input('your password : ')
                msg=input('what message : ')
                

                while True:
                    sleep(time_limit)
                    break

            if command_input=="ping":
                try:
                    IP=input('IP : ')
                    os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                    while True:
                        os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                
                except:
                    command_input=str(input('con_hac/Hax/email/bomb> '))

            if command_input=="ping --limit":
                try:
                    limit=input('The Limit : ')
                    IP=input('IP : ')

                    ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                    print(ping)

                    while (ping):
                        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                        print(ping)
                        sleep(float(limit))
                
                except:
                    command_input=str(input('con_hac/Hax/email/bomb> '))
            
            if command_input=="clr":
                os.system('clear')

                command_input=str(input('con_hac/Hax/email/bomb> '))
            
            if command_input=="return":
                command_input=str(input("con_hac> "))
        

    if command_input=="ping":
        try:
            IP=input('IP : ')
            os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

            while True:
                os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
        
        except:
            command_input=str(input("con_hac> "))

    if command_input=="ping --limit":
        try:
            limit=input('The Limit : ')
            IP=input('IP : ')

            ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
            print(ping)

            while (ping):
                ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
                print(ping)
                sleep(float(limit))
        
        except:
            command_input=str(input("con_hac> "))

    if command_input=="info":
        w=open('info.txt', 'r')
        print(w.read())

        command_input=str(input("con_hac> "))

    if command_input=="nmap--dd":
        os.system('echo https://nmap.org/download.html')

        command_input=str(input("con_hac> "))

    if command_input=="wireshark--dd":
        os.system('echo https://www.wireshark.org/download.html')

        command_input=str(input("con_hac> "))

    if command_input=="banner":
        print(banner)

        command_input=str(input("con_hac> "))
    
    if command_input=="quit":
        print('Abording')
        exit()
    
    if command_input=="credits":
        print('''
        ==============================================================================
        ==============================================================================
        ==============================================================================''')
        print("https://github.com/MohammadIsCoding1/")
        print("https://www.youtube.com/channel/UC_tN73NX_750otcFUpqtaNw")
        print('''
        ==============================================================================
        ==============================================================================
        ==============================================================================''')
        command_input=str(input("con_hac> "))
    
    if command_input=="tp_10_cod_lan":
        print('''
        1.Pysploit
        2.Javascipt
        3.Java
        4.C
        5.SQL
        6.C#
        7.Go
        8.R
        9.swift
        10.php
        ''')
        command_input=str(input("con_hac> "))
    
    if command_input=="tips":
        tip='try typing show hax or show payload'
        tip1='did you know that this was made with python 100%'
        tip2='did you know that this was made by a 12 year old'
        tip3=''

        choose_tip=random.choice(tip, tip1, tip2, top3)
        print(choose_tip)
        command_input=str(input("con_hac> "))
    
    if command_input=="":
        pass
