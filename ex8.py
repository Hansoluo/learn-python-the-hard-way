# -*- coding: utf-8 -*-

# 附件练习2，双引号里有单引号没关系，不会引起混乱

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)  # 这里要注意的是加入变量的个数一定要对应起来
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
     "I had this thing.", 
	 "I had this thing.", 
	 "I don't have this thing.",
	 "I had this thing."
)  # 保持格式就是保持风格
