# -*- coding: UTF-8 -*-

# 习题32 循环和列表 

# 创建列表list，并给变量赋值
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#用for循环把列表中的值都打印一遍。注意变量都不同。
# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number
	
# same the above
for fruit in fruits:
    print "A fruit of tyep: %s" % fruit
	
# also we go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i
	
# we can also built lists, first start with an empty one
elements = []

# then we use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
	# append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i 
	
# 附加练习 2
lists = []
lists = range(0,6)
print lists