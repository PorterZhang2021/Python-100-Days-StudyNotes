fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

# 列表切片
fruits2 = fruits[1:4]
print(fruits2)

# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)

# 逆向复制
fruits4 = fruits[-3:-1]
print(fruits4)

# 可以通过反向切片来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)
