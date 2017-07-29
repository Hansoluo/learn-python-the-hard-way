# -*- coding: utf-8 -*-

# 与练习4相同的结构，变量定义一致，打印用了格式化字符串，更加方便
# 变量的值直接写死在程序里不好，在后面的练习中改成了用户输入

my_name = 'shy'
my_age = 24
my_height = 176
my_weight = 70
my_eyes = 'black'
my_hair = 'black'
my_teeth = 'white'

print "Let's talk about %s." % my_name     # 格式化字符串%s
print "He's %s cm tall." % my_height
print "He's %s kg heavy." % my_weight
print "He's got %s eyes, %s teeth and %s hair." % (my_eyes, my_teeth, my_hair)   # 连续用三个%s，必须用括号括起来
print "If I add %s, %s, and %s I get %s." % (my_age, my_height, my_weight, my_age + my_height + my_weight)







