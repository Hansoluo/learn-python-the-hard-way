# -*- coding: utf-8 -*-

# 函数定义,括号中的参数名及个数要和下面保持一致

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1
	
def print_none():
    print "nothing."
	
print_two("shy", "yt")
print_two_again("shy", "yt")
print_one("First!")
print_none()