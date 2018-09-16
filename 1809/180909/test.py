import requests as web
import bs4
import csv

# キーワードを使って検索する
list_keywd = ['生物','一覧']
resp = web.get('https://www.google.co.jp/search?num=100&q=' + '　'.join(list_keywd))
resp.raise_for_status()

# 取得したHTMLをパースする
soup = bs4.BeautifulSoup(resp.text, "html.parser")
# 検索結果のタイトルとリンクを取得
link_elem01 = soup.select('.r > a')
# 検索結果の説明部分を取得
link_elem02 = soup.select('.s > .st')

if(len(link_elem02) <= len(link_elem01)):
    leng = len(link_elem02)
else:
    leng = len(link_elem01)    

# CSVファイルを書き込み用にオープンして整形して書き出す
with open('g_output.csv','w',newline='',encoding='utf8') as outcsv:
    csvwriter = csv.writer(outcsv)
    csvwriter.writerow(['タイトル・説明','URL'])
    for i in range(leng):
        # リンクのみを取得し、余分な部分を削除する
        url_text = link_elem01[i].get('href').replace('/url?q=','')
        # タイトルのテキスト部分のみ取得
        title_text = link_elem01[i].get_text()
        # 説明のテキスト部分のみを取得/余分な改行コードは削除する
        t01 = link_elem02[i].get_text()
        t02 = t01.replace('\n','')
        disc_text = t02.replace('\r','')
        csvwriter.writerow([title_text + disc_text,url_text])
    outcsv.close()