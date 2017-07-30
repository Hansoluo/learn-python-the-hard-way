# -*- coding: utf-8 -*-

# 附加练习，将程序简化在raw_input中输入

from sys import argv

script, user_name = argv

print "Hi, %s, I'm the %s script." %(user_name, script)

likes = raw_input("Do you like me?\n>")
lives = raw_input("Where do you live?\n>")
computer = raw_input("What kind computer do you have?\n>")

print """
%r %r %r
""" % (likes, lives,computer)

# 附加练习,raw_input的变化，结果证明不能这样用，不识别格式化字符数串
love = raw_input("Do you love me %s?\n>" % user_name)
print "You said %s about love me."
