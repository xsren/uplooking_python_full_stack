#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

# import mycompany
# from mycompany.web import  www
# from mycompany.test import  www as www_test
# mycompany.web.www.do()
# mycompany.web.www.do()
# mycompany.web.www.do()
# www.do()
import sys

def test_1():
    args = sys.argv
    print(args)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()