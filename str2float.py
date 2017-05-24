#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一个将str转换为float的函数，如 '123.456' --> 123.456

from functools import reduce

def str2float(str):
	s_split = str_split(str)
	s_int = str2int(s_split[0])
	s_float = str2point(s_split[1])
	return s_int + s_float

# 把字符串拆分为整数和小数部分，分别进行转换
def str_split(s):
	if isinstance(s, str) and '.' in s:
		s_split = s.split('.')
		# print(s_split)
		return s_split
	else:
		pass

def str2int(s):
	def mul(x, y):
		return x * 10 + y
	return reduce(mul, map(char2num, s))

def str2point(s):
	def divi(x, y):
		return x / 10 + y
	return reduce(divi, map(char2num, reversed(s)))

# 把字符转换为数字
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


if __name__ == '__main__':
	str_enter = input("Please a float number like string: ")
	str2float(str_enter)
	print(type(str2float(str_enter)))