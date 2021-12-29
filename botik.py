from telegram.ext import Updater, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup
from time import sleep

def on_message(update, context):
	global n, url, filteredAneks, page, soup, filteredAneks, allAneks
	chat = update.effective_chat
	text = update.message.text
	while True:
		if text.lower() == 'пост':
			try:
				context.bot.send_message(chat_id=-1001285371511, text=filteredAneks[n])
				n += 1
				time.sleep(7200)
			except:
				n = 0
				page = requests.get(url, verify=False)
				soup = BeautifulSoup(page.text, "html.parser")
				filteredAneks = []
				allAneks = soup.find_all('div', class_='text', limit=12)

				for data in allAneks:
					if data.find('br'):
						while data.find('br'):
							data.find('br').replace_with("\n")
						filteredAneks.append(data.text)
					else:
						filteredAneks.append(data.text)
				context.bot.send_message(chat_id=-1001285371511, text=filteredAneks[n])
				n += 1
				time.sleep(7200)
		else:
			context.bot.send_message(chat_id=chat.id, text="Не знаю такой команды")

n = 0
url = 'https://www.anekdot.ru/release/anekdot/day/'
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.text, "html.parser")
filteredAneks = []
allAneks = soup.find_all('div', class_='text', limit=12)

for data in allAneks:
	if data.find('br'):
		while data.find('br'):
			data.find('br').replace_with("\n")
		filteredAneks.append(data.text)
	else:
		filteredAneks.append(data.text)



token = str(open("token.txt", "r").read())

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, on_message))

print("Бот запущен. Нажмите Ctrl+C для завершения")

updater.start_polling()
updater.idle()