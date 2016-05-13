# -*- coding: utf-8 -*-

import unittest


class TestBaseLogic(unittest.TestCase):


    def test_switch(self):
        result = {
            'A' : lambda x: '优: %s' % x,
            'B' : lambda x: '良: %s' % x,
            'C' : lambda x: '及格: %s' % x,
            'D' : lambda x: '差: %s' % x,
        }
        print result['A'](99)

