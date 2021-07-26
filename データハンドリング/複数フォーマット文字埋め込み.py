dic = {
    "Aidemy" : "Ishikawa Akihiko",
    "Apple" : "Tim Cook",
    "Alphabet" : "Larry Page",
    "Microsoft" : "Satya Nadella",
    "Facebook" : "Mark Zuckerbarg"
}
template = "企業名：{}, CEO：{}"

# 変数dicの中身を（例）のような書式で出力してください。
# （例）： 企業名：Aidemy, CEO：Ishikawa Akihiko
for key in dic:
    print(template.format(key, dic[key]))
