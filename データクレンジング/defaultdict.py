from collections import defaultdict

# 文字列 description
description = \
"Artificial intelligence (AI, also machine intelligence, MI) is " + \
"intelligence exhibited by machines, rather than " + \
"humans or other animals (natural intelligence, NI)."

# defaultdict を定義して下さい
char_freq = defaultdict(int)

# 文字の出現回数を記録して下さい
for i in description:
    char_freq[i] += 1
    
    
# value の降順にソートし、上位10要素を出力して下さい
print(sorted(char_freq.items(),key=lambda x: x[1],reverse = True)[:10])