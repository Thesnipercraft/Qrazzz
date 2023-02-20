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
                q.put(href)
                print(href)
    else:
        return