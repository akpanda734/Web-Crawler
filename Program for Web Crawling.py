import requests
import re
from bs4 import BeautifulSoup
import json
import time
url=[r'https://en.wiktionary.org/wiki/Category:English_adjective-forming_suffixes', r'https://en.wiktionary.org/wiki/Category:English_adverb-forming_suffixes', r'https://en.wiktionary.org/wiki/Category:English_noun-forming_suffixes']
g={}
for u in url:
    if u != r'https://en.wiktionary.org/wiki/Category:English_adverb-forming_suffixes':
        r=requests.get(u)
        soup=BeautifulSoup(r.text, 'html.parser')
        price_box=soup.find('div', attrs={'class':'mw-category'})
        l=re.findall('<a href="([^"]+)" title="[^"]+">.*</a>', str(price_box))
    else:
        r=requests.get(u)
        soup=BeautifulSoup(r.text, 'html.parser')
        price_box=soup.find('div', attrs={'lang':'en'})
        l=re.findall('<a href="([^"]+)" title="[^"]+">.*</a>', str(price_box))
    q=u[u.find('_')+1:]
    g[q]={}
    for u2 in l:
        i=u2.find('-')
        str1=u2[i:]
        if str1=='-%27er':
            str1="-'er"
        u3='https://en.wiktionary.org'+u2
        g[q][str1]=u3
        rm=requests.get(u3)
        soup1=BeautifulSoup(rm.text, 'html.parser')
        #pb=soup1.
f=open('Wiktionarynew.json','w')
json.dump(g,f,indent=2)
print('Now we are taking a break')
print('10 sec break is complete')
print('Yes perfectly complete')
f.close()