import requests
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import datetime
import time
import schedule


token = "<Your bot token>"
chat_id = 'Your ID'

bomdod = tong = peshin = asr = shom = xufton = 0
weekday = 0

def data():

    oy = datetime.today()
    
    global bomdod, tong, peshin, asr, shom, xufton
    global weekday
    
    URL = 'https://islom.uz/vaqtlar/1/' + str(oy.month)
    page = urllib.request.urlopen(URL)
    soup = BeautifulSoup(page, 'html.parser')

    table = soup.find('table', class_ = 'table table-bordered prayer_table')


    hafta = datetime.today().weekday()

    if hafta == 4:
        today = table.find('tr', class_ = 'juma bugun')
    else:
        today = table.find('tr', class_ = 'p_day bugun')
    


    times = []
    for item in today:
        for i in item:
            if i != '\n':
                times.append(i)



    week = {'Душанба': 'Dushanba', 'Сешанба': 'Seshanba', 'Чоршанба': 'Chorshanba', 'Пайшанба': 'Payshanba', 'Жума': 'Juma', 'Шанба': 'Shanba', 'Якшанба': 'Yakshanba'}

    day = times[2]
    times = times[3:]

    if day in week:
        weekday = week[day]
    weekday = "Dushanba"

    bomdod, tong, peshin, asr, shom, xufton = times

### BOMDOD
def bom():
    data()
    global token, chat_id
    
    text = "Bugun Sana: " + str(datetime.today().strftime('%Y-%m-%d'))+ ', ' + weekday + "\nSoat: "+ bomdod+ "\n\nBOMDOD NAMOZI vaqti bo'ldi!!! \n\nSoat "+ tong+" gacha davom etadi"
    print(text)
    
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage"+"?chat_id=" + chat_id + "&text="+ text
    results = requests.get(url_req)
    return results.json()


### PESHIN
def pesh():
    data()
    global token, chat_id
    
    text = "Bugun Sana: " + str(datetime.today().strftime('%Y-%m-%d'))+ ', ' + weekday + "\nSoat: "+ peshin+ "\n\nPESHIN NAMOZI vaqti bo'ldi!!! \n\nSoat "+ asr+" gacha davom etadi"
    
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage"+"?chat_id=" + chat_id + "&text="+ text
    results = requests.get(url_req)
    return results.json()


def ars():
    data()
    global token, chat_id
    
    text = "Bugun Sana: " + str(datetime.today().strftime('%Y-%m-%d'))+ ', ' + weekday + "\nSoat: "+ asr+ "\n\nASR NAMOZI vaqti bo'ldi!!! \n\nSoat "+ shom+" gacha davom etadi"
    
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage"+"?chat_id=" + chat_id + "&text="+ text
    results = requests.get(url_req)
    return results.json()

def sh():
    data()
    global token, chat_id
    
    text = "Bugun Sana: " + str(datetime.today().strftime('%Y-%m-%d'))+ ', ' + weekday + "\nSoat: "+ shom+ "\n\nSHOM NAMOZI vaqti bo'ldi!!! \n\nYarim soat davom etadi"
    
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage"+"?chat_id=" + chat_id + "&text="+ text
    results = requests.get(url_req)
    return results.json()

def xuf():
    data()
    global token, chat_id
    
    text = "Bugun Sana: " + str(datetime.today().strftime('%Y-%m-%d'))+ ', ' + weekday + "\nSoat: "+ xufton+ "\n\nXUFTON NAMOZI vaqti bo'ldi!!! \n\nSoat "+ bomdod+" gacha davom etadi"
    
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage"+"?chat_id=" + chat_id + "&text="+ text
    results = requests.get(url_req)
    return results.json()

data()

schedule.every().day.at("00:01").do(data)

schedule.every().day.at(bomdod).do(bom)
schedule.every().day.at(peshin).do(pesh)
schedule.every().day.at(asr).do(ars)
schedule.every().day.at(shom).do(sh)
schedule.every().day.at(xufton).do(xuf)


while True:
    schedule.run_pending()
    time.sleep(1)
