import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://ja.wikipedia.org/wiki/%E7%A5%9E%E3%81%AE%E4%B8%80%E8%A6%A7').read()

soup = BeautifulSoup(html, 'lxml')
tables = soup.findAll('table', class_='multicol')

for table in tables:
    for li in table.findAll('li'):
        a = li.find('a')
        print("%s's url is %s" % (a.text, a.attrs['href']))