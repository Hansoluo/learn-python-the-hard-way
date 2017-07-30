# -*- coding: utf-8 -*-

# 函数和文件

input_file = raw_input("please enter the file name:") # 获取文件名

def print_all(f):
    print f.read()  # 跟直接用read一样

def rewind(f):
    f.seek(0)  # 重新设置文件读取指针到开头

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)  # 本来很简单的打印，用函数表述这么繁琐，用了多个变量。但是也许处理大量的文件来说很有用。

print "Now let's rewind, kind of like a tape." 

rewind(current_file) # 回到开头，实际上文件一旦open，就到结尾了，如果去掉这行代码，则不会读取文件

print "Let's print three lines:"

current_line = 1  
print_a_line(current_line, current_file)  # 扫第一行

# 附加练习5，+=的用法

current_line += 1
print_a_line(current_line, current_file)  # 扫第二行

current_line += 1
print_a_line(current_line, current_file)  # 扫第三行

# 附加练习4，seek回到开头

rewind(current_file)  # 回到第一行
print_a_line(1, current_file)

rewind(current_file) # 继续扫第二行
print_a_line(2, current_file)

rewind(current_file)  # 又回到第一行了
print_a_line(1, current_file)