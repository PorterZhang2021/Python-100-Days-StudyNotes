str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))

# 获得字符串 首字母大写 的拷贝
print(str1.capitalize())

# 获得字符串 每个单词 首字母大写的拷贝
print(str1.title())

# 获得字符串变大写后的拷贝
print(str1.upper())

# 从字符串中查找子串所在的位置 给出起始
print(str1.find('or'))
# 没有返回 -1
print(str1.find('shit'))

# 与find类似
print(str1.index('or'))
# 找不到子串引发异常
# print(str1.index('shit'))

# 检查字符串是否以指定的字符串开头
# 区分大小写
print(str1.startswith('He'))
print(str1.startswith('hel'))

# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())

# 检查字符串是否以字母构成
print(str2.isalpha())

# 检查字符串是否以数字和字母构成
print(str2.isalnum())

str3 = '     jackfrud@126.com'
print(str3)

# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
