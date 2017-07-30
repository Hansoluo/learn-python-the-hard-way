# -*- coding: utf-8 -*-

def add(a,b):
    return a + b
	
def subtract(a,b):
    return a - b
	
def multiply(a,b):
    return a * b
	
def divide(a,b):
    return a / b

# 调用函数进行运算

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide (100,2)

# 利用格式化字符输出
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# 函数嵌套，递归调用
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

# 附加练习4
what =  subtract(add(24,divide(34,100)),1023)
print what