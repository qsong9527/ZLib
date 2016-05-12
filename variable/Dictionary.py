# -*- coding: UTF-8 -*- 

import unittest
import math

class DicTester(unittest.TestCase):

    def test_01_add(self):

        dic1 = {'a':1}
        dic1['b'] = 2
        print dic1
