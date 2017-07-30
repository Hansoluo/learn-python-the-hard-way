# -*- coding: utf-8 -*-

# 10种方式运行没有意义，无非是参数不同

def cats_dogs(cats, dogs):
    print "cats: %r, dogs: %r" % (cats, dogs)

cats_dogs(20, 30)

cats_count = 10
dogs_count = 50
cats_dogs(cats_count, dogs_count)

cats_dogs(10 + 20, 5 + 6)
cats_dogs(cats_count + 20, dogs_count + 6)