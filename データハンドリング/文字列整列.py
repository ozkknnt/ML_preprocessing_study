dic = {
    "CEO" : {"Aidemy" : "Ishikawa Akihiko", "Apple" : "Tim Cook", "Facebook" : "Mark Zuckerbarg" },
    "location" : {"Aidemy" : "Japan", "Apple" : "America", "Facebook" : "America"},
    "founded_year" : {"Aidemy" : 2014, "Apple" : 1976, "Facebook" : 2004}
}

# str.format()関数のオプションを指定することによって、文字幅を揃えてください。
for key in dic:
    print("{0:<15} Aidemy : {1[Aidemy]:^20} Apple : {1[Apple]:^20} Facebook : {1[Facebook]:^20}".format(key, dic[key]))