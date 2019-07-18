#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   12_detailBasicType.py
@Time    :   2019/07/08 11:40:38
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# here put the import lib
# 1.数字类型（int）
power_int = 2 ** 40
print("power_int：", power_int)
print("power_int_type：", type(power_int))
str_int = int('123')
print("str_int_type：", type(str_int))
# 将数字转换为二进制，并返回最少位二进制的位数
bit_length_int = 123
print(bit_length_int.bit_length())


# 2.bool类型（bool）
none_value = bool(None)
print("none_value: ", none_value)
blank_1 = bool([])
print("blank_1: ", blank_1)
blank_2 = bool({})
print("blank_2: ", blank_2)
blank_3 = bool("")
print("blank_3: ", blank_3)
blank_4 = bool(())
print("blank_4: ", blank_4)
zero_value = bool(0)
print("zero_value: ", zero_value)