# coding:utf8
from __future__ import division

SLEEP_TIME = 2


# 测试
def run():
    """
    测试
    :return:
    """
    # 空格和tab
    print('a')
    print('The quick brown fox', 'jumps over', 'the lazy dog')
    print('hello world')
    print(300)
    print(200 + 300)
    # input的内容需要加双引号
    name = input()
    print('hello,', name)
    print("aaa")
    print("a'a'a")
    print('a"a"a')
    print(3.14)
    print('I\'m learning\nPython.')
    print('''aaadasfaf
    fdaa
    ffdaf
    ''')

    # bool
    print(True)
    print(3 > 2)
    print(False)
    print(3 > 4)

    # and or not
    man_age = 10
    age = 18
    age = input()
    age = int(age)
    if age >= 18:
        print('adult')
    else:
        print('teenager')
    print(10 / 3)
    print(10 // 3)
    print(10 % 3)


def test(self):
    pass


if __name__ == '__main__':
    run()
