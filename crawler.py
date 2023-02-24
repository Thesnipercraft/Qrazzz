import requests
import time
from bs4 import BeautifulSoup
from queue import Queue

q = Queue()

header =  {
	'User-Agent': 'QrazzzBot'
}

q.put("https://google.com/")

visited = set()

def crawl(url):
    try:
        response = requests.get(url, headers=header)
    except Exception as e:
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all("a")
        urls = []
        for link in links:
            href = link.get("href")
            if href and (href.startswith("http") or href.startswith("https")):
            	visited.add(href) 
            	q.put(href)
            	urls.append(href)
        return urls
            	

    else:
        return []

while not q.empty():
	url = q.get()
	crawl = crawl(url)
	for c in crawl:
		print(c)
