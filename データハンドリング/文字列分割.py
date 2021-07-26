url = "http://blog.aidemy.net" 

# 変数 url を区切り文字をドット（`"."`）として、 str.split() 関数によって分割し、変数 split_url に代入してください。
split_url = url.split(".")

# split_url を出力してください。
print(split_url)

# 分割した split_url から、最後に格納されている文字列を取り出して出力してください。
print(split_url[-1])
