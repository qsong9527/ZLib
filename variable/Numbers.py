# -*- coding: UTF-8 -*- 

import unittest
import math
import random

class NumberTester(unittest.TestCase):

    def test_01_num_var(self):
        '''1. 变量赋值'''
        __num = 1
        print("__num = %d , type is %s" % (__num, type(__num)))

    def test_02_var_del(self):
        ''' 2. 变量删除'''
        __num = 1
        del __num
        try:
            print __num
        except UnboundLocalError,e:
            print("__num has been delete, " + str(e))

    ################################################################
    # Python数学函数
    #
    def test_03_asb(self):
        '''返回数字的绝对值'''
        __num_1 = -10
        __num_2 = 10
        print "%d abs value = %d" % (__num_1, abs(__num_1))
        print "%d abs value = %d" % (__num_2, abs(__num_2))

    def test_04_ceil(self):
        '''返回数字的上入整数'''
        __num_1 = 8.1
        __num_2 = 8.0
        print "%f ceil value = %f" % (__num_1, math.ceil(__num_1))
        print "%f ceil value = %f" % (__num_2, math.ceil(__num_2))

    def test_05_floor(self):
        '''返回数字的下舍整数'''
        __num_1 = 8.1
        __num_2 = 8.0
        print "%f floor value = %f" % (__num_1, math.floor(__num_1))
        print "%f floor value = %f" % (__num_2, math.floor(__num_2))

    def test_06_round(self):
        '''返回浮点数x的四舍五入值'''
        __num_1 = 8.1
        __num_2 = 8.5
        __num_3 = 8.0
        print "%f round value = %f" % (__num_1, round(__num_1))
        print "%f round value = %f" % (__num_2, round(__num_2))
        print "%f round value = %f" % (__num_3, round(__num_3))

    def test_07_cmp(self):
        '''数字大小比较'''
        __num_1 = 1
        __num_2 = 9
        print "%d cmp %d is %s" %(__num_1, __num_2, cmp(__num_1, __num_2))
        print "%d cmp %d is %s" %(__num_2, __num_1, cmp(__num_2, __num_1))

    def test_08_max(self):
        '''返回给定参数的最大值'''
        __num_list = [3,5,7,1]
        print "max of %s is %s" % (str(__num_list), max(__num_list))

    def test_09_min(self):
        '''返回给定参数的最小值'''
        __num_list = [3,5,7,1]
        print "min of %s is %s" % (str(__num_list), min(__num_list))

    def test_10_modf(self):
        '''返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示'''
        __num_1 = 8.89
        __mod_result = math.modf(__num_1)
        print "%s modf result = %s" % (__num_1, __mod_result)

    ################################################################
    # Python随机数函数
    #
    def test_11_choice(self):
        ''' 从序列的元素中随机挑选一个元素 '''
        __choice_1 = random.choice([1,2,3,4,5,6,7,8,9,10])
        __choice_2 = random.choice(range(10))
        print "__choice_1 = %s" % __choice_1
        print "__choice_2 = %s" % __choice_2

    def test_12_randrange(self):
        '''  从指定范围内，按指定基数递增的集合中获取一个随机数'''
        __randrange_1 = random.randrange(10)
        __randrange_2 = random.randrange(0,10)
        print "__randrange_1 = %s" % __randrange_1
        print "__randrange_2 = %s" % __randrange_2

    def test_13_random(self):
        '''随机生成下一个实数，它在[0,1)范围内。'''
        __random_1 = random.random()
        __random_2 = random.random()
        print "__random_1 = %s" % __random_1
        print "__random_2 = %s" % __random_2

    def test_14_shuffle(self):
        '''将序列的所有元素随机排序'''
        __list_1 = [1,2,3,4,5,6,7,8,9,10]
        __list_2 = [1,2,3,4,5,6,7,8,9,10]
        random.shuffle(__list_2)
        print "random list = %s, result = %s" % (__list_1, __list_2)
