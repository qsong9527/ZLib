# -*- coding: utf8 -*-
'''
封装Android设备端常用操作, 基于adbpy.adb类库
@Created on 2016-05-17
@author: jy.zenist.song

@Lasted edite by jy.zenist.song 2016.05.17
'''

import platform

class PlatformHelper():

    @classmethod
    def get_system_type(cls):
        '''判断当前平台的系统类型'''
        if platform.system() == 'Windows':
            if platform.win32_ver()[0] == '8':
                return 'Win8'
            else:
                return 'Win7orLower'
        elif platform.system() == 'Linux':
            return 'Linux'
        else:
            return 'MacOS'