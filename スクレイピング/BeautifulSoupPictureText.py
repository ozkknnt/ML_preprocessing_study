import urllib.request
import requests
from bs4 import BeautifulSoup

# Aidemyの演習用Webページを取得する
authority = "http://scraping.aidemy.net"
r = requests.get(authority)
# lxmlでパースする
soup = BeautifulSoup(r.text, "lxml")

# ページ遷移のリンクを探すために<a>要素を取得する
urls = soup.find_all("a")

# ----- スクレイピングしたいurlをurl_listに取得する -----
url_list = []
# url_listにそれぞれのページのURLを追加する
for url in urls:
    url = authority + url.get("href")
    url_list.append(url)

# ----- 写真のタイトルをスクレイピングする -----
# スクレイピングの関数を作成します
def scraping(url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    # ここを解答
    photos = soup.find_all("h3")

    photos_list = []
    # 以下のfor文を完成させてください
    for photo in photos:
        photo = photo.text
        photos_list.append(photo)

    return photos_list

for url in url_list:
    print(scraping(url))