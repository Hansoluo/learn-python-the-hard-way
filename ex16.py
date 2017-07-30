# -*- coding: utf-8 -*-

# 用argv方式获取文件名，在运行时老是忘记，还是raw_input好，可以提示你
# 附加练习4，如果没有w，会提示你不能执行清空命令

filename = raw_input("please enter the filename:")

print "We are going to erase %s." % filename   #这两句代码是在提示用户程序在干嘛
print "oping the file...."  
txt = open(filename, 'w')  # open打开文件
txt.truncate()             # truncate清空文件

print "I'm going to ask you three lines." 
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

# 附加练习3，将重复的写入合并

line = "%s\n%s\n%s" % (line1, line2, line3)  

print "I'm going write this things to file."   
txt.write(line)   # 写入文件，圆括号跟raw_input的很像，可以有变量和字符串，但不接受格式化字符串
                  # 一个有趣的现象是，在txt里打开不换行，而在程序里读是换行的
txt.close()

# 附加练习2，再把写入的文件读一遍

txt_again = open(filename)
print txt_again.read()
