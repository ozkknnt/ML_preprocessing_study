from urllib.request import urlopen

f = urlopen("http://scraping.aidemy.net/")

# エンコード方式をHTTPMessage型で取得してください
encoding = f.info().get_content_charset(failobj="utf-8")
print(encoding)