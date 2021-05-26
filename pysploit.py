#----------------------------------------
#authour - The United Hacker
#criedits - in the credit file
#start date - april 29 2021
#release date - still in progress
#----------------------------------------




import pyautogui
import os
import requests
import random
import string
import socket
import re
from bs4 import BeautifulSoup
from time import sleep
import os, platform

spam=1


The_United_Hacker='''
███╗░░░███╗██╗░░░██╗  ██╗░░██╗░█████╗░██╗░░██╗
████╗░████║╚██╗░██╔╝  ██║░░██║██╔══██╗╚██╗██╔╝
██╔████╔██║░╚████╔╝░  ███████║███████║░╚███╔╝░
██║╚██╔╝██║░░╚██╔╝░░  ██╔══██║██╔══██║░██╔██╗░
██║░╚═╝░██║░░░██║░░░  ██║░░██║██║░░██║██╔╝╚██╗
╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
'''
print(The_United_Hacker)

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

    if command_input=="quit":
        sure=input('are you sure you wanna exit [y]or[n] : ')
        if sure=='y':
            exit()

        if sure=='n':
            command_input=str(input("con_hac> "))

    if command_input=="show":
        print('Hax/web/ip')
        print('Hax/phishing/web')
        print('Hax/email/bomb')
        print('Hax/username/web')
        print('Hax/web/scraping')
        print('Hax/(content unavalible)')
        print('Hax/(content unavalible)')
        print('Hax/(content unavalible)')
        print('Hax/(content unavalible)')
        command_input=str(input("con_hac> "))

    if command_input=="use Hax/web/scraping":
        command_exploit=input("con_hac/Hax/web/ip > ")

        while (command_exploit):
            command_exploit=input("con_hac/Hax/web/ip > ")

        if command_exploit=="quickscr":
            website=input('Website > ')

            data=requests.get(website)

            phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
            emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

            print(phones, emails)

            command_exploit=input("con_hac/Hax/web/ip > ")

        if command_exploit=="lotscrp":

            website=input('Website > ')
            data=requests.get(website)

            soup=BeautifulSoup(data.text, 'html.parser')

            data=[]
            for tr in soup.find_all('tr'):
                values=[td.text for td in tr.find_all('td')]
                data.append(values)
            print(data)

            command_exploit=input("con_hac/Hax/web/ip > ")


    if command_input=="use Hax/web/ip":
        command_exploit=input("con_hac/Hax/web/ip> ")

        while(command_exploit):
            command_exploit=str(input("con_hac/Hax/web/ip> "))

        if command_exploit=="webgeturl":
            url=input('Website > ')
            print(socket.gethostbyname(url))

            command_exploit=str(input("con_hac/Hax/web/ip> "))

        if command_exploit=="webgeturl rapid":
            url=input('Website > ')
            print(socket.gethostbyname(url))

            while (url):
                url=input('Website > ')
                print(socket.gethostbyname(url))


        if command_exploit=="return":
            command_input=str(input("con_hac> "))

        if command_exploit=="quit":
            sure=input('are you sure you wanna exit [y]or[n] : ')

            if sure=='y':
                exit()

            if sure=='n':
                command_input=str(input("con_hac> "))

        if command_exploit=="clr":
            os.system('cls')

            command_exploit=str(input("con_hac/Hax/web/ip> "))

        if command_exploit=="//ip":
            os.system('ipconfig')

            command_exploit=str(input("con_hac/Hax/web/ip> "))

    if command_input=="Hax/username/web":

        command_exploit==input("con_hac/Hax/username/web")

        if command_exploit=="webuserget":
                    username=input('The username > ')

                    print('https://www.youtube.com/channel/'+username)
                    print('https://www.chess.com/member/'+username)
                    print('https://'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)
                    print('https://www.'+username)

                    command_exploit==str(input("con_hac/Hax/username/web"))

    if command_input=="use Hax/phishing/web":
        command_exploit=str(input("con_hac/Hax/phishing/web> "))

        while (command_exploit):
            command_exploit=str(input("con_hac/Hax/phishing/web> "))

        if command_exploit=="sendwebfile":
            url = input('Webpage to grab source from: ')
            html_output_name = input('Name for html file: ')

            req = requests.get(url, 'html.parser')

            with open(html_output_name, 'w') as f:
                f.write()
                f.close()

            print('go and execute the html file then public it, then wait fot your victim and also send em this link')
            command_exploit=str(input("con_hac/Hax/phishing/web> "))

        if command_exploit=="clr":
            os.system('cls')

            command_exploit=str(input("con_hac/Hax/phishing/web> "))

        if command_exploit=="return":
            command_input=str(input("con_hac> "))

        if command_exploit=="//ip":
            os.system('ipconfig')

            command_input=str(input("con_hac> "))

        if command_input=="clr":
            os.system('cls')

            command_input=str(input("con_hac> "))

        print('go to the web then make it public then give it to the victim and wait for the output')

    if command_input=="use Hax/email/bomb":
        pass

    if command_input=="ping":
        IP=input('IP : ')
        os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

        while (host):
            os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)

    if command_input=="ping --limit":
        limit=input('The Limit : ')
        IP=input('IP : ')

        ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
        print(ping)

        while (ping):
            ping=os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + IP)
            print(ping)
            sleep(float(limit))

    if command_input=="info":
        w=open('info.txt', 'r')
        print(w.read())

        command_exploit=str(input("con_hac> "))

    if command_input=="":

        command_exploit=str(input("con_hac> "))

    if command_input=="nmap--dd":
        os.system('echo https://nmap.org/download.html')

        command_exploit=str(input("con_hac> "))

    if command_input=="wireshark--dd":
        os.system('echo https://www.wireshark.org/download.html')

        command_exploit=str(input("con_hac> "))

    if command_input=="":
        pass
