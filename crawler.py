import requests

from connector import UrlQueue
from connector import DataStore
from bs4 import BeautifulSoup  

url_queue = UrlQueue(host="host", user="user", password="pass", database="database")
data_store = DataStore(host="host", user="user", password="pass", database="database")



header = {
	'User-Agent': 'QrazzzBot',
	'From': 'your email'
}


start_url = "https://google.com/"

def crawl(url):
	try:
		response = requests.get(url, headers=header)
	except requests.exceptions.RequestException:
		print("Error code 1")

	if response.status_code == 200:
		print(response.text)
	else:
		pass



crawl(start_url)