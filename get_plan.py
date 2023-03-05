import requests
import urllib.parse
import re

header = {
	'User-Agent': 'QrazzzBot',
	'From': 'your mail'
}



def get_just_domain(url):
	no_just_domain = urllib.parse.urlparse(url)
	just_domain = no_just_domain.scheme + '://' + no_just_domain.netloc
	return just_domain

def add_robots(url):
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.path == '':
        new_path = '/'
    elif not parsed_url.path.endswith('/'):
        new_path = parsed_url.path + '/'
    else:
        new_path = parsed_url.path
    new_url = urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, new_path, '', '', ''))
    return urllib.parse.urljoin(new_url, 'robots.txt')

def get_robots(url):
	response = requests.get(url, headers=header)
	return(response.text)

def get_sitemap_url(robots):
	robots_txt = robots

	sitemap_regex = r"Sitemap:\s*(.*)"

	match = re.search(sitemap_regex, robots_txt)

	if match:
	    sitemap_url = match.group(1)
	    return sitemap_url
	else:
	    return


def get_sitemap(sitemap_url):
	response = requests.get(sitemap_url, headers=header)
	if response.status_code == 200:
		return response.text
	else:
		return



print(get_sitemap(get_sitemap_url(get_robots(add_robots(get_just_domain("https://google.com/robots.txt"))))))
