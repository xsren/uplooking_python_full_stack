# coding:utf8
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
except Exception as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        # logging.exception(e)
        print(e)

main()
print('END')

