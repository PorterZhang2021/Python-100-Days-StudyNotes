"""

赋值运算符和复合赋值运算符

"""

a = 10
b = 3
# 相当于: a = a + b
a += b
# 相当于: a = a * (a + 2)
a *= a + 2
# 算一下这里会输出什么
print(a)
