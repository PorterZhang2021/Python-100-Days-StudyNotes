"""
约瑟夫环问题
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，
直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，
问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    # 起始的30个人
    persons = [True] * 30
    # 计数器，索引，数字
    counter, index, number = 0, 0, 0
    # 人数大于15就进行循环
    while counter < 15:
        # 如果有人为True
        if persons[index]:
            # 数字加1
            number += 1
            # 如果为9
            if number == 9:
                # 这个人被淘汰
                persons[index] = False
                # 减少一个人
                counter += 1
                # 报数归0
                number = 0
        # 索引为1
        index += 1
        # 索引按30为一个圈
        index %= 30
    # 输出基督徒与非基督徒
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()
