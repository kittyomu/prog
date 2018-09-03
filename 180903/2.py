import sys,os
import re
import urllib.request as urlreq
from bs4 import BeautifulSoup
import requests
import time

# 一時的に保存するページのリスト
linkData = []

keyword = "インターネット" 
max = 200

# 検索結果から各ページのリンク先をmaxページ分だけ取得
for num in range(0,max,20):
    res = requests.get("https://www.irasutoya.com/search?q="+keyword+"*"+"&max-results=20&start="+str(num)+"&by-date=false*")
    soup = BeautifulSoup(res.text, "lxml")
    time.sleep(0.1)

    # Linkの箇所をselect
    links = soup.select("a[href]")
    for a in links:
        # Linkタグのhref属性の箇所を抜き出す
        href = a.attrs['href']
        # 画像データに対応するページのリンク先のみをリストに格納
        if re.search(r"irasutoya.*blog-post.*html$",href):
            if not href in linkData:
                linkData.append(href)

# 各ページから画像データのリンクを取得して、画像を保存
for link in linkData:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "lxml")
    #print(soup)
    # 記事中の画像データを抜き出す
    # class separator -> a の抜き出し
    links = soup.select(".separator > a")
    for a in links:
        # hrefのデータを取得
        imageLink = a.get('href')
        #print(imageLink)
        # ファイル名の取得
        filename = re.search(r"http.*\/(.*png|.*jpg)$",imageLink)
        print(filename)
        # 画像をダウンロードする
        if filename != None:
            urlreq.urlretrieve(imageLink,"down/"+filename.group(1))
        else:
            print("not match")
        # デバッグ用にダウンロード先Linkを表示
        print(imageLink)
        time.sleep(1)
