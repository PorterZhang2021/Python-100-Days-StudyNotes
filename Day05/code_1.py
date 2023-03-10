"""
    寻找水仙花数
    水仙花数也被成为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数
    它是一个3位数，该数字每个位上数字的立方之和正好等于它本身
"""

# 解决水仙花数问题 -> 每个位上数字的立方之和等于其本身
# 验证问题
# 获取到每一位数
# 每一位数乘立方
# 判断数与其立方情况是否相同

# 循环找数
for num in range(100, 1000):
    # 个位
    low = num % 10
    # 中位
    mid = num // 10 % 10
    # 百位
    high = num // 100
    # 判断数与其立方情况是否相同
    if num == low ** 3 + mid ** 3 + high ** 3:
        # 输出结果
        print(num)
