# -*- coding: utf8 -*-
'''
@Created on 2016-10-17
@author: jy.zenist.song

@Lasted edite by jy.zenist.song 2016.10.17
'''

import unittest

from system.platform_helper import PlatformHelper

class TestPlatformHelper(unittest.TestCase):

    def test_get_system_type(self):
        print PlatformHelper.get_system_type()


if __name__ == '__main__':
    unittest.main()
