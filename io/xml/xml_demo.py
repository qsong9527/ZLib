# -*- coding: utf-8 -*-

import unittest
from xml.etree import ElementTree as ET

class TestPraseXmlByET(unittest.TestCase):
    '''XML Demo'''

    def test_01_xml(self):

        #1. 开启xml文档
        __tree = ET.parse("test.xml")

        #2. 获取根节点
        __root = __tree.getroot()
        print("%s -- %s" % (__root.tag, __root.attrib))

        #3. 遍历根下面的子节点
        for __child in __root:
            print("%s -- %s" % (__child.tag, __child.attrib))

        #4. 通过下标访问
        print __root[0][1].text
        print __root[0].tag, __root[0].text

        #5. 通过节点tag访问
        for user in __root.findall('user'):
            id = user.get('id')
            name = user.find('username').text
            email = user.find('email').text
            print id, name, email
