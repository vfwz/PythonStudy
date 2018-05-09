#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# ASCII码 一个字节(byte), 8个比特(bit), 十进制(255)
# GB2312编码 两个字节
# Unicode 通常两个字节
# UTF-8编码 英文1个字节，汉字通常3个字节，生僻字4-6字节

print(u'字母A转成数字', ord('A'))
print(u'数字65转成字母', chr(65))   # 数字转字母

print(r"用u'\u4e2d'也可以直接表示'中'", u'\u4e2d')

print('ABC'.encode('utf-8'))
print(u'中文'.encode('utf-8'))
# print('\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) pyhton3报 AttributeError: 'str' object has no attribute 'decode'


# 格式化输出
# 占位符   %d    整数
#          %f    浮点数
#          %s    字符串
#          %x    十六进制整数
print('Hello %s' % 'World')
print('Hi, %s, you have $%d.' % ('Michael', 100000))
print('%%d %d \n%%f %f \n%%s %s \n%%x %x\n%%x %x' % (10, 3.14159, u'中文', 12, 0xff))

