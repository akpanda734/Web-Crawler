import requests
import re
from bs4 import BeautifulSoup
url=[r'https://en.wiktionary.org/wiki/Category:English_adjective-forming_suffixes', r'https://en.wiktionary.org/wiki/Category:English_adverb-forming_suffixes', r'https://en.wiktionary.org/wiki/Category:English_noun-forming_suffixes']
for u in url:
	if u!= r'https://en.wiktionary.org/wiki/Category:English_adverb-forming_suffixes':
		r=requests.get(u)
		soup=BeautifulSoup(r.text, 'html.parser')
		price_box=soup.find('div', attrs={'class':'mw-category'})
		l=re.findall('<a href="([^"]+)" title="[^"]+">.*</a>', str(price_box))
		print(l)
	else:
		r=requests.get(u)
		soup=BeautifulSoup(r.text, 'html.parser')
		price_box=soup.find('div', attrs={'lang':'en' 'dir':'ltr' 'class':'mw-cotent-ltr'})
		l=re.findall('<a href="([^"]+)" title="[^"]+">.*</a>', str(price_box))
		print(l)