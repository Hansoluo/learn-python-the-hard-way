# -*- coding: utf-8 -*-

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
empty_cars = cars - drivers  # 变量赋值后可以直接运算
carpool = drivers * space_in_a_car
average_passengers_per_car = passengers / drivers

print "There are", cars, "cars available."     # 因为还没学格式化字符串，只能用这么费劲的办法
print "There are only", drivers, "drivers available."
print "There will be", empty_cars, "empty cars today."
print "We can transport", carpool, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print 120.0 / 30




