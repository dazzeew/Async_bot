from config import def_url
from bs4 import BeautifulSoup
import requests
from aiogram import types
import time

from config import TOKEN



def url(text,id_pars):
	model = ''
	for i in range(len(text)):
		if text[i] == ' ':
			model += '+'
		else: 
			model += text[i]
	new_url = def_url + id_pars + model + '&how=r'
	return new_url

async def Parcer(url):
	dictname = dict()
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	name = soup.find_all('a', class_="dark_link")
	price = soup.find_all('span', class_="price_value")
	availability = soup.find_all('div', class_="item-stock")
	for i in range(len(price)):
		dictname[name[i].text] = [price[i], availability[i]]
	return dictname 




def send_telegram(text: str):
    url = "https://api.telegram.org/bot"
    channel_id = "@testbot_mic"
    url += TOKEN
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

