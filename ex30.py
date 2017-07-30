# -*- coding: UTF-8 -*-
# 习题30 else和if

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
	
# 附加练习3
if buses > cars and people > cars:
    print "That's too many buses."
elif buses < cars and people > cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses and cars > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home."