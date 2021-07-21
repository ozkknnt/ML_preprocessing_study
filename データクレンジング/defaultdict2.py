from collections import defaultdict

# まとめたいデータ price...(名前, 値段)
price = [
    ("apple", 50),
    ("banana", 120),
    ("grape", 500),
    ("apple", 70),
    ("lemon", 150),
    ("grape", 1000)
]
# defaultdict を定義して下さい
fruites_list = defaultdict(list)

# 説明文の例と同様にvalue の要素に値段を追加して下さい
for key,value in price:
    fruites_list[key].append(value)

# 各value の平均値を計算し、配列にして出力して下さい
print([sum(x) / len(x) for x in fruites_list.values()])