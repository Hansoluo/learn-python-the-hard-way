# -*- coding: UTF-8 -*-
# 习题39 字典

# creat a mapping of state to abbreviation   州名字和对应的缩写
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#creat a basic set of states and some cities in them  州和对应的城市
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities  
# 添加元素
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print out some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict  
# 嵌套调用字典中的元素
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation   
# items()是字典自带的可调用函数
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
    print states.items()

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time 
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (
        state, abbrev,cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there  
# get()为字典自带函数，用来查询是否有这个元素，有的话返回True
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

