# -*- coding: utf-8 -*-

# 读取文件操作open
# 两种获取文件名称的操作
# 附加练习5，用raw_inputa方法获取更好，不会写死
# 附加练习8，如果对文件内容有更改，用close()是个好习惯，保存你的工作内容

from sys import argv

script, filename = argv

print "Here is your file %s:" % filename
txt = open(filename)  # open打开文件是类似raw_input的命令，接收文件名，并返回参数
print txt.read()  # read可以读取文件内容
txt.close()

file_again = raw_input("Type the filename again:")
txt_again = open(file_again)
print txt_again.read() 
txt_again.close()
