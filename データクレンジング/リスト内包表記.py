# minute_data...単位は分
minute_data = [30, 155, 180, 74, 11, 60, 82]

# 計測時間(分)を[時, 分]に換算する関数を作成して下さい
hm_split = lambda x: [x // 60, x % 60]

# リスト内包表記を用いて所定の配列を作成して下さい
hm_data = [hm_split(x) for x in minute_data]

# 出力して下さい
print(hm_data)