# -*- coding: UTF-8 -*- 

import unittest
import pythonic
from decorator import SingletonObject

class SingletonTester(unittest.TestCase):

    def test_pythonic(self):
        singleton_1 = pythonic.SINGLETON_OBJECT
        singleton_2 = pythonic.SINGLETON_OBJECT
        assert id(singleton_1) == id(singleton_2)

    def test_decorator(self):
        singleton_1 = SingletonObject()
        singleton_2 = SingletonObject()
        assert id(singleton_1) == id(singleton_2)

    def test_assert(self):
        singleton_1 = "abc"
        singleton_2 = "abc"
        print
        assert id(singleton_1) == id(singleton_2)
