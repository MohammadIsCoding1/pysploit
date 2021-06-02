#----------------------------------------
#authour - AnOnYmOuS
#criedits - in the credit file
#start date - april 29 2021
#release date - still in progress
#----------------------------------------



import datetime
import os, platform
import pyautogui
import os
import requests
import random
import string
import socket
import re
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore, Back, Style


spam=1

print('testing')
banner='''
������W���W�����W�������W������W���W�����������W���W��������W
��TPP��WZ��W���T]��TPPPP]��TPP��W��Q�������TPP��W��QZPP��TPP]
������T]�Z����T]�Z�����W�������T]��Q�������Q����Q��Q�����Q���
��TPPP]���Z��T]���ZPPP��W��TPPP]���Q�������Q����Q��Q�����Q���
��Q����������Q���������T]��Q������������WZ�����T]��Q�����Q���
ZP]��������ZP]���ZPPPPP]�ZP]�����ZPPPPPP]�ZPPPP]�ZP]���ZP]���

'''+"       "+datetime.datetime.now()
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


    if command_input=="show":
        print('Hax/web/ip'+"Description: Find The IP Address Of A Website ")
        print('Hax/copy/web'+"Description: Make A Phishing Website To Get Details")
        print('Hax/email/bomb'+"Description: Spam Someone's Inbox Of Email")
        print('Hax/web/scraping'+"Description: Scrap Any Website")
        print('Hax/pass/attack'+"Description: Do a Dictionary Or Brute Force Attack")
        print('Hax/(content unavalible)'+"Description: ")
        print('Hax/(content unavalible)'+"Description: ")
        print('Hax/(content unavalible)'+"Description: ")
        command_input=str(input("con_hac> "))

    if command_input=="use Hax/pass/attack":
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

                while (host):
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
        command_input=input("con_hac/Hax/web/scraping > ")

        if command_input=="ping":
            try:
                IP=input('IP : ')
                os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                while (host):
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

        while (command_input):
            command_input=str(input("con_hac/Hax/web/scraping > "))

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

        while(command_input):
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

                while (host):
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

        while (command_input):
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

                while (host):
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

        while(command_input):
            command_input=str(input('con_hac/Hax/email/bomb>'))
        
        if command_input=="email_bomb --limit":
            limit=input('Spam Times > ')
            email=input('your email : ')
            password_email=input('your password : ')
            msg=input('what message : ')

            for i in range(limit):
                pass
                
                while True:
                    print('sending email')
                    break
                
                while False:
                    print('done')
                    command_input=str(input('con_hac/Hax/email/bomb>' ))
                    break
        
        
        if command_input=="email_bomb --time_limit":
            time_limit=input('Time : ')
            email=input('your email : ')
            password_email=input('your password : ')
            msg=input('what message : ')
            
            while time:
                pass

            time=sleep(float(time_limit))
            print(time)

        if command_input=="ping":
            try:
                IP=input('IP : ')
                os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

                while (host):
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

            while (host):
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
