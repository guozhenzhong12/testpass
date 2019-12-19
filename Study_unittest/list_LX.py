
hero_0 = {}
hero_0.setdefault("射手", []).append("鲁班")
hero_0.setdefault("射手", []).append("元芳")
hero_0.setdefault("射手", []).append("黄忠")

print(hero_0)

for A, B in hero_0.items():
    print("\nKey: " + A)
    print("Value: " + str(B))                              # 字典中的值为一个列表遍历字典中的键和值

hero_0.setdefault("战士", []).append("老夫子")
hero_0.setdefault("战士", []).append("亚瑟")
hero_0.setdefault("战士", []).append("吕布")
print(hero_0)
for A, B in hero_0.items():
    print("\nKey: " + A)
    print("Value: " + str(B))

hero_0.setdefault("法师", []).append("张良")
hero_0.setdefault("法师", []).append("妲己")
hero_0.setdefault("法师", []).append("嬴政")
for A, B in hero_0.items():
    print("\nKey: " + A)
    print("Value: " + str(B))

