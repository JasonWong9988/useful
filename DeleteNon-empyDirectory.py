#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-25 07:44:35
# @Author  : Jason Wong (wonglenchong@163.com)
# @Link    : https://github.com/JasonWong9988/useful
# @Version : $Id$

import os, shutil

def delNon_emptyDir(dir_):
	if os.path.isdir(dir_): # 判断dir_是否是一个目录
		file_list = os.listdir(dir_) # 获取目录中的所有文件或文件夹
		for file in file_list:
			temp_dir = os.path.join(dir_, file)
			if os.path.isfile(temp_dir):
				try:
					if temp_dir[-4:].lower() in ['.int', '.sys', '.dll', '.adt']:
						continue
					else:
						os.remove(temp_dir)
				except os.error:
					autoRun.exception("remove %s error" % temp_dir)
			if os.path.isdir(temp_dir):
				shutil.rmtree(temp_dir)
	else:
		raise FileNotFoundError("系统找不到指定的路径：%s" % dir_)

dir_ = "D:\KuGou"
delNon_emptyDir(dir_)