#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 程序实现的功能：判断输入的数字序列，能否构成等差数列
# 等差数列：1 2 3 4 5 6 7，后一个元素与前一个元素的差相等

# 把列表中元素转换为int型
def str2int(list):
	for i in range(len(list)):
		list[i] = int(list[i])

# 用户输入的数字个数必须小于等于nums，否则要求重新输入。
nums = int(input("Please enter a number: "))	# 
while True:
	print("Please randomly enter {} int numbers:\n".format(nums))
	num_input = input(" ")
	# 用空格把输入的字符串分割为列表
	num_list = num_input.split(' ')
	if len(num_list) > nums:
		print("Wrong input, please try again!")
	else:
		break

str2int(num_list)	# 把列表中元素转换为int型

# num_list = sorted(num_list)	# 排序，返回一个新list
num_list.sort()		# 就地排序，不会返回新list
# print(num_list)

result = 1
val = num_list[1] - num_list[0]
for i in range(1, len(num_list)-1):
	# val1 = num_list[0]
	if num_list[i+1] - num_list[i] != val:
		result = 0
		break
	else:
		continue

if result == 0:
	print('False')
else:
	print('True')
