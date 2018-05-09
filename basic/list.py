#!/usr/bin/env python
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))   # len() 获取list长度
print(classmates[0])     # 正向索引
print(classmates[-3])    # 逆向索引

classmates.append('Adam')   # 追加元素
print(classmates)

classmates.insert(1, 'Jack')    # 指定位置插入元素
print(classmates)

print(classmates.pop())    # 删除末尾元素
print(classmates)

print(classmates.pop(1))     # 删除指定位置的元素
print(classmates)



