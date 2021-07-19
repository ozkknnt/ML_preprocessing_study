# reモジュールのインポート
import re

# 時間データが入っている文字列time_data
time_data = "2017/4/1_22:15"

# time_dataを分割して、listを作成して下さい。
data = re.split("[/ _ :]",time_data)

# "月"の部分を出力して下さい。
print(data[1])

# "時"の部分を出力して下さい。
print(data[3])