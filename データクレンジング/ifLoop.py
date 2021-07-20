# minute_data...単位は分
minute_data = [30, 155, 180, 74, 11, 60, 82]

# リスト内包表記を用いて所定の配列を作成して下さい
hjust = [x for x in minute_data if x % 60 == 0 ]

# 出力して下さい
print(hjust)
