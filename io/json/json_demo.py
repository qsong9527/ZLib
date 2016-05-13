# -*- coding: utf-8 -*-

import unittest
import json

class TestJson(unittest.TestCase):
    '''JSON Demo'''

    '''
    Simple
    '''
    def test_01_dic2json(self):
        __data = [{'a':"A",'b':(2,4),'c':3.0}]
        __json_str = json.dumps(__data)
        print type(__json_str), __json_str

        __json_dic = json.loads(__json_str)
        print type(__json_dic), __json_dic
