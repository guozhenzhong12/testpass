# 2019-12-2
# Murray

name1 = ['张良', '元芳', '老夫子', '孙悟空', '荆轲']
name1.insert(0, "李白")    # 利润表开头添加元素 “李白'
print(name1)               # 打印names列表信息
for name in name1:            # 遍历names列表中元素，添加到变量name中
    if name == "张良":
        print(name + '是一个法师')      # 当name变量等于张良时，打印：张良是一个法师
    elif name == "元芳":
        print(name + '是一个射手')       # 当name变量是元芳时，打印：元芳时一个射手
    elif name == '老夫子':
        print(name + "是一个战士")        # 当变量是老夫子时：打印：老夫子是一个战士
    else:
        print(name + "是一个刺客")         # 当变量是其他元素时，打印：当前元素是一个刺客
print("他们都是王者荣耀中的英雄")


hero1 = ('李白', '老夫子', '元芳', '张良', '租八戒')   # 创建一个元祖
for hero in hero1:                                    # 遍历元祖hero1中的元素存到变量hero中
    if hero == '李白':
        print(hero + '是刺客')
    elif hero == '老夫子':
        print(hero + '是战士')
    elif hero == '元芳':
        print(hero + '是射手')
    elif hero == '张良':
        print(hero + '实法师')
    else:
        print(hero + '是坦克')                        # 根据变量hero的值打印内容
print("他们都是英雄")

hero2 = {
    "射手": "鲁班",
    "法师": "张良",
    "刺客": "李白",
    "战士": "吕布",
    "坦克": "猪八戒"
}                                                      # 新建一个字典

print(hero2['射手'])
print(hero2['战士'])                                   # 根据键打印键值

hero2["辅助"] = "蔡文姬"                               # 字典添加新的键和键值
print(hero2)

hero2["射手"] = "元芳"                                 # 修改字典hero2 中射手的值
print(hero2)

del hero2['坦克']                                      # 删除hero2 中键：坦克，其值也被永久删除
print(hero2)

for hero in hero2:
    print(hero.title())                               # 遍历字典hero2 中所有的键且首字母大写

for key, value in hero2.items():
    print('\nKey: ' + key)
    print('Value: ' + value)                          # 遍历字典hero2 中所有的键和键值

for A,B in hero2.items():
    print("\nKey: " + A)
    print("Value: " + B)                              # 遍历字典hero2中所有的键和值


her = {}

her.a