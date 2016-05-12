#coding: UTF-8

import unittest

from android.adbpy.android_helper import AndroidHandler


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.__devices = AndroidHandler()

    def test_devices(self):
        '''获取当前连接设备'''
        print self.__devices.DEVICES

    def test_get_heap_settings(self):
        '''获取系统HEAP设定:
        初始值,受限最大值,不受限最大值
        '''
        print self.__devices.HEAP_SET

    def test_get_device_settings(self):
        '''获取所连接设备的信息'''
        print self.__devices.DEVICE_INFO

    def test_get_system_status(self):
        '''获取所连接设备的信息'''
        print self.__devices.SYSTEM_STATUS

    def test_start_app(self):
        '''启动AUT(被测应用)'''
        __component = "com.tencent.mm/.ui.LauncherUI"
        print self.__devices.startApp(__component)

    def test_force_stop_aut(self):
        '''前置关闭AUT'''
        __package = "com.tencent.mm"
        self.__devices.forceStopApp(__package)

    def test_get_current_component(self):
        '''获取当前显示activiy'''
        print self.__devices.get_current_component()

    def test_clear_device_log(self):
        '''清除设备端log'''
        print self.__devices.clear_dev_log()

    def test_dump_device_log(self):
        '''dump设备端log'''
        print self.__devices.dump_dev_log()

    def test_cap_device_screen(self):
        '''dump设备端log'''
        print self.__devices.cap_screen()

    def test_shell(self):
        '''测试运行设备端命令行'''
        print self.__devices.shell("cat /system/build.prop")


if __name__ == '__main__':
    unittest.main()
