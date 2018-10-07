import urllib.request

url = "https://uta.pw/shodou/img/3/3.png"
savename = "test.png"

urllib.request.urlretrieve(url, savename)
print("保存しました")