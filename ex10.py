# -*- coding: utf-8 -*-

a_cat = "\tI'm a cat."  # 水平制表符\t，自动缩进字符
b_cat = "I'm \na cat."  # 换行符\n
c_cat = "I'm \\ a \\ cat."  # 换行符\n

d_cat = """
I'll do a list:
\t* a_cat
\t* b_cat
\t* c_cat\n\t* d_cat
"""  # \n直接代替ENTER来换行

print a_cat
print b_cat
print c_cat
print d_cat

# 附加练习3和4

print "%r" % "\nda\\\'\""   # 如果是已经定义好的变量则无需引号，如果是字符串需要引号才能识别。
                            # 转义序列不起作用
print "%s" % "\nda\\\'\""   # 转义序列起作用