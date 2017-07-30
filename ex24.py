# -*- coding: UTF-8 -*-

# 习题24 更多联系
# 函数return的值可以赋予变量，而内部的变量都是暂时的

print "Let's practice everything."
print 'You\'d need to kown \'bout escapes with \\ that do \n newlines and \t tabs.'

# 联系打印字符串的一些分行的使用
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuotion
and requires an  explanation
\n\twhere there is none.
"""

print "---------------"
print poem
print "---------------"

# 打印结合格式化字符串
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# 函数定义和返回
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# 调用函数并执行运算	
start_point = 10000
beans, jars, crates = secret_formula(start_point)
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)