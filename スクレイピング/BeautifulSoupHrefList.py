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
# url_listにそれぞれのページのURLを追加してください
for url in urls:
    url = authority + url.get("href")
    url_list.append(url)

# リストを出力
print(url_list)