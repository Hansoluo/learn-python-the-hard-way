# -*- coding: utf-8 -*-

# 文件用write命令时，必须要以w模式打开
# 文件用read命令时，必须要以r模式打开，即默认模式
# 格式化字符串的新用法，可以接命令返回参数，如len()

from os.path import exists  

file_from = raw_input("please enter the file_from name:")
file_to = raw_input("please enter the file_to name:")
print "Copying from %s to %s." % (file_from, file_to)

print "opening the file...."  
txt1 = open(file_from)  # open打开文件
w_txt1 = txt1.read()             # 读文件

print "The file is %d bytes long." % len(w_txt1)  # 返回字节数 

print "copying the file...."  
txt2 = open(file_to, 'w')  # open打开文件
txt2.write(w_txt1)             # 写入文件

print "Does this file exist? %r" % exists(file_to)  # exists可以判断文件是否存在

txt1.close()
txt2.close()

# 附加练习，再把写入的文件读一遍

txt_again = open(file_to)
print txt_again.read()