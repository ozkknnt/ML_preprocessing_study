dic = {
    "CEO" : {"Aidemy" : "Ishikawa Akihiko", "Apple" : "Tim Cook", "Facebook" : "Mark Zuckerberg" },
    "location" : {"Aidemy" : "日本", "Apple" : "アメリカ", "Facebook" : "アメリカ"},
    "founded_year" : {"Aidemy" : 2014, "Apple" : 1976, "Facebook" : 2004}
}

# 変数 dic の中身を（例）のような形式で出力してください。 
for key in dic:
    print("{0} Aidemy : {1[Aidemy]} Apple : {1[Apple]} Facebook : {1[Facebook]}".format(key, dic[key]))


#CEO Aidemy : Ishikawa Akihiko Apple : Tim Cook Facebook : Mark Zuckerberg
#location Aidemy : 日本 Apple : アメリカ Facebook : アメリカ
#founded_year Aidemy : 2014 Apple : 1976 Facebook : 2004