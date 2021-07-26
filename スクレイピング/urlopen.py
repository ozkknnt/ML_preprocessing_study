from urllib.request import urlopen

f = urlopen("http://scraping.aidemy.net/")

# HTMLコードを先頭から50文字取得してください
print(f.read(50))