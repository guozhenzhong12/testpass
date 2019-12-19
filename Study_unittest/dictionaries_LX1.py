Tom = {
    "family_name": "king",
    "given_name": "lisa",
    "age": "20",
    "city": "Beijing",
}

Murray = {
    "family_name": "open",
    "given_name": "lisa",
    "age": "18",
    "city": "shenzheng",
}

Tim = {
    "family_name": "plum",
    "given_name": "lisa",
    "age": "20",
    "city": "shanghai"
}
names = [Tom, Murray, Tim]
for name in names:
    print(name)

favorite_places = {
    "tom": ["北京", "香港", "上海"],
    "murray": ["青岛", "成都", "威海"],
    "tim": ["东京", "曼谷", "巴黎"],
}

for A, B in favorite_places.items():
    print("\n" + A.title() + "喜欢的地方是： ")
    print(str(B))

country = {
    "北京": {
        "country": "中国",
        "population": "2170.7万",
        "fact": "故宫",
    },
    "东京": {
        "country": "日本",
        "population": "1350万",
        "fact": "银座",
    },
    "巴黎": {
        "country": "法国",
        "population": "224万",
        "fact": "浪漫之都",
    },
}

print(country)
for A in country:
    if A == "北京":
        print("\n" + A)
        print(country.get("北京").get("country"))



