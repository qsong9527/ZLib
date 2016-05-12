# -*- coding: UTF-8 -*- 

import unittest
import math

class NumberTester(unittest.TestCase):

    def test_01_split(self):
        '''1. 字符串分割-1'''
        __str = "http://www.easou.com/"
        print __str.split(":")
        print __str.split(".")
        print __str.split(".",1)

    def test_02_rsplit(self):
        '''1. 字符串分割-2'''
        __str = "http://www.easou.com/"
        print __str.rsplit(":")
        print __str.rsplit(".")
        print __str.rsplit(".", 1)

    def test_03_partition(self):
        '''1. 字符串分割-3'''
        __str = "http://www.easou.com/"
        print __str.partition(":")
        print __str.partition(".")

    def test_04_rpartition(self):
        '''1. 字符串分割-4'''
        __str = "http://www.easou.com/"
        print __str.rpartition(":")
        print __str.rpartition(".")
        print __str.rpartition(";")

