# -*- coding: utf-8 -*-

# argv参数变量是在执行命令时输入参数
# 输入参数和代码定义个数需要保持一致，不能多，不能少
# argv第一个默认是script，即脚本的名称

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third

# 附加练习3
# 其他的从用户输入参数的方法，在运行中输入

fourth = raw_input(">")
fifth = raw_input(">")
sixth = raw_input(">")

print "The fourth variable is:", fourth 
print "The fifth variable is:", fifth 
print "The sixth variable is:", sixth

