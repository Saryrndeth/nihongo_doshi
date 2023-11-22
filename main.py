import random


word = {
    "聞く": "きく",
    "及ぶ": "およぶ",
    "行く": "いく",
    "買う": "かう",
    "待つ": "まつ",
    "乗る": "のる",
    "死ぬ": "しぬ",
    "遊び": "あそび",
    "読む": "よむ",
    "話す": "はなす",
    "見る": "みる",
    "食べる": "たべる",
    "来る": "くる",
}
corr = []
while True:
    if len(corr) == len(word):
        print("全て正解です")
        break
    key = random.choice([i for i in word.keys() if i not in corr])
    print(key)
    answer = input("日本語で何と言いますか？")
    if answer == word[key]:
        corr.append(key)
        print("正解です")
    else:
        print("不正解です")
        print("正解は", word[key], "です")
    print()