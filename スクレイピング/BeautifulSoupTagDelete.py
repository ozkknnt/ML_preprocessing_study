import requests
from bs4 import  BeautifulSoup

# Aidemyの演習用Webページを取得
r = requests.get("http://scraping.aidemy.net/")
# lxmlでパースする
soup = BeautifulSoup(r.text, "lxml")

# <h3>タグの要素を取り出してください
photos = soup.find_all("h3")

# <h3>タグを取り除いて写真名を取り出します
for photo in photos:
    print(photo.text)