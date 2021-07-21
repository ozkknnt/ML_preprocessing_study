# 時間データhour, 分データminute
hour = [0, 2, 3, 1, 0, 1, 1]
minute = [30, 35, 0, 14, 11, 0, 22]

# 時, 分を引数に、分に換算する関数を作成して下さい
conv_minute = lambda x,y: x*60+y

# リスト内包表記を用いて所定の配列を作成してください
result = [conv_minute(x,y) for x,y in zip(hour,minute)]

# 出力して下さい
print(result)
