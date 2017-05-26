#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-27 07:44:52
# @Author  : Jason Wong (wonglenchong@163.com)
# @Link    : https://github.com/
# @Version : $Id$

# 定义一个求阶乘的函数n! = n * (n-1) * ... * 1
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        value = n * fact(n-1)
    return value

# 定义一个求组合的函数Cn(m) = n!/((n-m)!*m!)
def comb(n, m):
    value = fact(n)//(fact(n-m)* fact(m))
    return value

if __name__ == '__main__':
	print("The factorial of 5 is: {}".format(fact(5)) )
	print("--**--" * 5)
	print("The combination of (5, 2) is :{}".format(comb(5, 2)))