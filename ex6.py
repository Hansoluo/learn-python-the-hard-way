# -*- coding: utf-8 -*-

# 附加练习1，代码加注释
# 练习2和3，确实是4个地方
# 练习4，因为运算可以直接打印

x = "There are %s type of people." % 10  # 将字符串赋值给变量x
binary = 'binary' # 定义变量
do_not = "don't"  # 定义变量，引号不能重复
y = "Those who know %s and those who %s." %(binary, do_not) # 赋值

print x
print y

print "I said: %r" % x
print "I also said: '%s'." % y  # 在这里r和s无所谓。%r是输出原始字符串，转义字符会不起作用

hailarious = True  #  这一段只是简单的拆解
joke = "Isn't that joke so funny?! %s."
print joke % hailarious

w = 'This is...'  # 这一段很无聊
e = 'bored.'

print w + e









