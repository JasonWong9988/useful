#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 以下程序实现的功能，将'ABC'转化为'CBA'

# Plan 1 将str转换为list，把list反向排序后再转为str
# str1 = 'ABC'
# lst_tmp1 = list(str1)
# lst_tmp2 = []
# for i in lst_tmp1[:]:
# 	lst_tmp2.append(lst_tmp1.pop())

# str2 = ''
# for i in lst_tmp2:
# 	str2 += i
# print(str2)

# Plan 2 利用str的切片，取出最后一个元素，然后切片不包含最后一个元素，再去最后一个元素加起来。
# str_input = input("Please input a string: ")
# slice_max = len(str_input)
# str_output = ''
# for i in str_input:
# 	str_output += str_input[:slice_max][-1]
# 	slice_max -= 1

# print("The reversed string of {0} is {1}".format(str_input, str_output))

# Plan 3 直接从右边开始取str的每一个元素，然后重新组合
str_input = input("Please input a string: ")
index = len(str_input)-1
str_output = ''
while index >= 0:
	str_output += str_input[index]
	index -= 1
print("The reversed string of {0} is {1}".format(str_input, str_output))

# 查找1-1000内的所有回数(正反看都相同，如'12321'、'999')

# def is_palindrome(num):
# 	if str(num) == abc2cba(str(num)):
# 		return True
# 	else:
# 		return False

# def abc2cba(str):
# 	ltmp1 = list(str)
# 	ltmp2 = []
# 	for i in range(len(ltmp1)):
# 		ltmp2.append(ltmp1.pop())
# 	str2 = ''
# 	for str in ltmp2:
# 		str2 += str
# 	return str2

# pali_list = filter(is_palindrome, range(1, 1000))
# for i in pali_list:
# 	if i > 500:
# 		break
# 	else:
# 		print(i, end = ' ')

