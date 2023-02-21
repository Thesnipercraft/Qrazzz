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

url_queue.add_url("https://example.com/")
def crawl(url):
    try:
        response = requests.get(url, headers=header)
    except Exception as e:
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href and (href.startswith("http") or href.startswith("https")):
                url_queue.add_url(href)
                print(href)
                
    else:
        return


while True:
	id = url_queue.get_id()
	url_queue.delete_url(id)
	url = url_queue.get_url(id)
	crawl(url)
	time.sleep(0.1)
