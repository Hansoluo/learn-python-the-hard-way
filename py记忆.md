## LPTHW记忆内容 ##
书中要记忆的知识点

### 关键字 ###
- **and del from**
- **not while as**
- **elif global or** 
- **with assert else**
- **if pass yield**
- **break except import**
- **print class exec**
- **exec in raise**
- **continue finally is**
- **reture def for**
- **lanmda try**

### 数据类型 ###
-  True
-  False
-  None
-  strings
-  numbers
-  floats
-  lists

### 数学运算符 ###
- + 加号
- - 减号
- / 斜杠（除法）
- * 星号（乘法）
- % 百分号（**求余**）
- < 小于号
- > 大于号
- <= 小于等于号
- >= 大于等于号
- 运算优先级 PEMDAS 括号、指数、乘、除、加、减

### 格式化字符 ###
- %s 字符串（采用str()的显示）
- %r 字符串（采用repr()的显示）
- %c 单个字符
- %b 二进制整数
- %i 十进制整数
- %d 十进制整数
- %o 八进制整数
- %x 十六进制整数
- %e 指数（基底为e）
- %E 指数（基底为E）
- %f 浮点数
- %F 浮点数
- %g 指数e或浮点数（根据显示长度）
- %G 指数E或浮点数（根据显示长度）
- %% 字符"%"

### 转义序列 ###
- \\  反斜杠（\）
- \'  单引号（'）
- \"  双引号（"）
- \a  ASCII响铃符
- \b  ASCII退格符
- \f  ASCII进纸符
- \n  ASCII换行符
- \N{name} 
- \r  ASCII回车符
- \t  ASCII水平制表符
- \uxxxx  值为16位十六进制值
- \Uxxxxxxxx  值为32位十六进制值
- \v  ASCII垂直制表符
- \ooo  值为八进制值的字符
- \xhh  值为八进制数的字符

### 读写文件操作命令 ###
- close  关闭文件并保存
- read   读取文件内容，可以把结果赋给变量
- readline 读取文本文件的一行
- truncate 清空文件
- write(stuff) 将stuff写入文件
- seek(0) 重新设置文件读取指针到开头

### 逻辑术语 ###
-  and 与
-  or 或
-  not 非
-  ！= 不等于
-  == 等于
-  >= 大于等于
-  <= 小于等于
-  True 真
-  False 假

### 真值表 ###
NOT|真假        
---|---- 
not False |True
not True  |False

OR|真假
--|---
True or False | True          
True or True  | True          
False or True | True          
False or False| False  

AND|真假
--|---
True and False | False          
True and True  | True          
False and True | False          
False and False| False   

NOT OR|真假
--|---
not(True or False) | False          
not(True or True)  | False         
not(False or True) | False          
not(False or False)| True   

NOT AND|真假
--|---
not(True and False) | True          
not(True and True)  | False         
not(False and True) | True          
not(False and False)| True

!=|真假
--|---
1!=0 | True          
1!=1 | False
0!=1 | True
0!=0 | False

==|真假
--|---
1==0 | False         
1==1 | True
0==1 | False
0==0 | True
