# time_data...[年, 月, 日, 時, 分]
time_data = [
    [2006, 11, 26,  2, 40],
    [2009,  1, 16, 23, 35],
    [2014,  5,  4, 14, 26],
    [2017,  8,  9,  7,  5],
    [2017,  4,  1, 22, 15]
]
# "時"をキーとしてソートし、配列にして下さい
sorted_time_data = sorted(time_data,key=lambda x:x[3])

# ソートした配列を出力して下さい
print(sorted_time_data)