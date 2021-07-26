# Aidemyの演習用Webページ: http://scraping.aidemy.net/から、デコードする前のHTMLコードを500文字取得し、適切にデコードして出力してください
from urllib.request import urlopen

f = urlopen("http://scraping.aidemy.net/")

encoding = f.info().get_content_charset(failobj="utf-8")

webtext = f.read(500).decode(encoding)

# 500文字取得し、デコードして出力してください
print(webtext)