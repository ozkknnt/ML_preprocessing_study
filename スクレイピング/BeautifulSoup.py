import requests
from bs4 import  BeautifulSoup

# Aidemyの演習用Webページを取得
r = requests.get("http://scraping.aidemy.net/")

# lxmlでパースしてください
soup = BeautifulSoup(r.text, "lxml")

# h3タグの要素を取り出してください
photos = soup.find_all("h3")

print(photos)