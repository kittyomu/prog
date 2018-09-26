from bs4 import BeautifulSoup
import urllib.request
import time
import re
#ランダムでwikiに接続する

#接続回数
limit = 1000


for i in range(limit):
  #おまかせ表示のhtmlを取得
  time.sleep(3)

  req = urllib.request.Request('https://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:%E3%81%8A%E3%81%BE%E3%81%8B%E3%81%9B%E8%A1%A8%E7%A4%BA')
  response = urllib.request.urlopen(req)
  html = response.read()
  soup = BeautifulSoup(html, "lxml")

  title_tag = soup.title
  title = title_tag.string#タイトルのみを抽出
  title = re.sub(" - Wikipedia","",title)

  print(title)

  f = open('text.txt', 'a') # 書き込みモードで開く
  f.write(title+"\n") # 引数の文字列をファイルに書き込む
  f.close() # ファイルを閉じる