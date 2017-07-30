# -*- coding: utf-8 -*-

# 附件练习，去掉所有的my，熟悉变量的定义
# 与练习4相同的结构，变量定义一致，打印用了格式化字符串，更加方便
# 变量的值直接写死在程序里不好，在后面的练习中改成了用户输入

name = 'shy'
age = 24
height = 176
weight = 70
eyes = 'black'
hair = 'black'
teeth = 'white'

print "Let's talk about %s." % name     # 格式化字符串%s
print "He's %s cm tall." % height
print "He's %s kg heavy." % weight
print "He's got %s eyes, %s teeth and %s hair." % (eyes, teeth, hair)   # 连续用三个%s，必须用括号括起来
print "If I add %s, %s, and %s I get %s." % (age, height, weight, age + height + weight)







