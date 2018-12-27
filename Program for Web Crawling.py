import requests
import re
from bs4 import BeautifulSoup
import json
import time
url=[r'https://en.wiktionary.org/wiki/Category:English_adjective-forming_suffixes', r'https://en.wiktionary.org/wiki/Category:English_adverb-forming_suffixes', r'https://en.wiktionary.org/wiki/Category:English_noun-forming_suffixes',r'https://en.wiktionary.org/wiki/Category:English_prefixes']
g={}
f=0
for u in url:
    if u != r'https://en.wiktionary.org/wiki/Category:English_adverb-forming_suffixes' and u != r'https://en.wiktionary.org/wiki/Category:English_prefixes':
        r=requests.get(u)
        soup=BeautifulSoup(r.text, 'html.parser')
        price_box=soup.find('div', attrs={'class':'mw-category'})
        l=re.findall('<a href="([^"]+)" title="[^"]+">.*</a>', str(price_box))
    elif u==r'https://en.wiktionary.org/wiki/Category:English_prefixes':
        r=requests.get(u)
        f=1
        soup=BeautifulSoup(r.text, 'html.parser')
        price_box=soup.find('div', attrs={'class':'mw-category'})
        l=re.findall('<a href="([^"]+)" title="[^"]+">.*</a>', str(price_box))
        del(l[0])
    else:
        r=requests.get(u)
        soup=BeautifulSoup(r.text, 'html.parser')
        price_box=soup.find('div', attrs={'id':'mw-pages'})
        l=re.findall('<a href="([^"]+)" title="[^"]+">.*</a>', str(price_box))
    q=u[u.find('_')+1:]
    g[q]={}
    for u2 in l:
        i=u2.find('-')
        if f!=1:
            str1=u2[i:]
            if str1=='-%27er':
                str1="-'er"
        else:
            j=u2.rfind('/')+1
            str1=u2[j:i+1]
        u3='https://en.wiktionary.org'+u2
        rm=requests.get(u3)
        time.sleep(0.01)
        soup1=BeautifulSoup(rm.text, 'html.parser')
        a=soup1.find('span', attrs={'class':'mw-headline', 'id':'English'})
        if a:
            k=a.parent.parent
            m=k.find('ol')
            str2=re.sub('\t','    ',  str(m.get_text())) 
            g[q][str1]=re.sub('\n','                          ',str2)
        else:
            g[q][str1]=r'[Null]'
f=open('Wiktionary007.json','w')
json.dump(g,f,indent=3)
f.close()