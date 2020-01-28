import sys

import numpy
import nltk
import requests
from bs4 import BeautifulSoup as bs
import lxml

url = "https://www.newsweek.com/bernie-sanders-vows-reverse-every-single-thing-trump-has-done-immigration-he-surges-first-1484297"

user_agent_details = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
user_agents = {'User-Agent': user_agent_details}

response = requests.get(url, headers=user_agents)

soup = bs(response.content, "lxml")

webpage_body = soup.find_all(text=True)

output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	# there may be more elements you don't want, such as "style", etc.
]

for t in webpage_body:
	if t.parent.name not in blacklist:
		output += '{} '.format(t) 

print(output)