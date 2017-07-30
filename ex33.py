# -*- coding: UTF-8 -*-
# while 循环 它和if语句有点类似，就是去检查一个布尔表达式的真假
# 不一样的是它下面的代码块不是只执行一次，而是执行完后都调回到while所在的位置，如此重复进行，直到while表达式为False为止
# 它的问题在于可能永不结束

i = 0
numbers = []

def addnums(x):
    while i < 6:
        print "At the top i is %d" % i
        numbers.append(i)
	
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

x = raw_input('> ')
addnums(x)

# 附加练习
def addnums1():
    for i in range(0,6):
        print "i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers 

addnums()

for num in numbers:
    print num