# -*- coding: utf-8 -*-


print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()

print "so, you're %r old and %r tall." % (age, height)

# 附加练习2 raw_input的其他用法，直接省略打印  也就是ex12的内容
age = raw_input("How old are you?")
height = raw_input("How tall are you?")

print "so, you're %r old and %r tall." % (age, height)