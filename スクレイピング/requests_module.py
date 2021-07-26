import requests

# `requests`モジュールで指定したURLのResponseオブジェクトを取得します
r = requests.get('http://scraping.aidemy.net/')

# str型にデコードしたレスポンスを出力してください
print(r.text)