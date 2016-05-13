# -*- coding: utf-8 -*-

import unittest
import codecs

class TestUrlResponseCodec(unittest.TestCase):


    def test_01(self):
        __target = "\u5267\u60c5"
        print __target.decode('unicode-escape')

    def test(self):
        __str = '''{
              "args": {},
              "data": ""{\"q\": \"\\u5f20\\u827a\\u8c0b\"}"",
              "files": {},
              "form": {},
              "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Content-Length": "36",
                "Content-Type": "application/json",
                "Host": "httpbin.org",
                "User-Agent": "python-requests/2.9.1"
              },
              "json": "{"q": "\u5f20\u827a\u8c0b"}",
              "origin": "124.193.184.2",
              "url": "http://httpbin.org/post"
            }'''
        print __str.decode('unicode-escape').encode('utf-8')