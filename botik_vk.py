import requests
import vk_api
from bs4 import BeautifulSoup
from time import sleep

print('Бот запущен. Нажмите Ctrl+C, чтобы завершить.')
with open('data.txt', 'r') as f:
	[login, password] = data.split(' ')
vk_session = vk_api.VkApi(data[0], data[1])
vk_session.auth()
vk = vk_session.get_api()

url = 'https://anekdotovstreet.com/svegie-anekdoty/'

while True:
	page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}, verify=False)

	soup = BeautifulSoup(page.text, 'html.parser')
	highRatedAneks = []
	allAneks = soup.find_all('div', class_='anekdot-text')

	for data in allAneks:
		if not data.find('i', class_='fa fa-star-o'):
			highRatedAneks.append(data.find('p').text)
			if len(highRatedAneks) > 11: break

	for anek in highRatedAneks:
		vk.wall.post(message=anek, owner_id=-209093833)
		sleep(7200)
