# coding=utf-8

# 字典 dict, 亦即Java中的Map, key-value存储

d = {'Michael': 95, 'Gavin': 99, 'Tracy': 88}
print(d)
print(d['Gavin'])

# 直接通过给key赋值的方式就可以插入数据
d['Adam'] = 87
print(d)

# print d['Thomas'] 不存在会报错
# 避免Key不存在的两种方式
# 1. 通过in判断key是否存在
print('Thomas' in d)
# 2. 通过dict提供的get()方法
print(d.get('Thomas'), d.get('Gavin'))
print(d.get('Thomas', -1), d.get('Gavin', 100))  # 不匹配则返回默认值

# 和Java相同，通过计算key的hash值来计算value的存储位置
# 不过Python中key必须是不可变的，list可变，不能作为key


# set, dict的无value形式
# 三种创建方式 https://www.cnblogs.com/kaituorensheng/p/6139573.html
s = set([0, 1, 2, 3, 'A'])
s1 = set((0, 4, 6, 7, 'B'))
s2 = {0, '7', '8', '9', 'C'}     # set literal 效率最好
print(s, s1, s2)

print(s & s1)    # 交集
print(s | s2)    # 并集

# tuple是不可变对象，但需要保证tuple中的数据也是不可变的才可以作为key
t = (1, 2)
t1 = (3, 4, [5, 6])
print({t})
# print {t1}   报错 TypeError: unhashable type: 'list'

