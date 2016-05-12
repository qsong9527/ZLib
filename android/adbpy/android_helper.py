# -*- coding: utf8 -*-
'''
封装Android设备端常用操作, 基于adbpy.adb类库
Created on 2014-10-17
@author: zen
'''

import time

from adbpy.adb import Adb

from android.resource import android_key_code as KEY_CODE


# from setting import devices_info as DEV_INFO
# from utils.pyTags import singleton
# from utils.logger import Logger
# from utils.system_helper import SystemHelper

def singleton(cls, *args, **kw):
    '''singleton修饰器'''
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class AndroidHandler():
    '''android系统及设备相关功能实现'''

    def __init__(self):
        '''
        AndroidHandler构造函数
        '''
        self.__adb = Adb()
        self.__devices_list = self.__getConnection()
        if len(self.__devices_list) == 0:
            raise NoDeviceConnectionException
        self.__get_system_properties()

    def __getConnection(self):
        '''
        获取设备连接状态
        :return: 连接的设备列表
        '''
        __ret_device_list = []
        try:
            __devices_list = self.__adb.devices()
        except Exception, e:
            print str(e)
            raise ADBServerException
        if len(__devices_list) == 0:
            pass
        else:
            for __dev in __devices_list:
                if not __dev[1] == 'device':
                    raise DeviceStatuException
                __ret_device_list.append(__dev)
        return __ret_device_list

    def __get_system_properties(self):
        '''获取设备系统build信息'''
        __prop_dic = {}
        # 1. 获取系统相关属性
        __sys_info = self.shell("cat /system/build.prop")
        # 2. 转换返回的系统数据为字典
        for __prop in __sys_info:
            if __prop.startswith("#") or len(__prop) < 5:
                pass
            else:
                __prop_m = __prop.split("=")
                __prop_dic[__prop_m[0]] = __prop_m[1]
        # 4. 返回系统数据
        self.__system_properties = __prop_dic

    @property
    def DEVICES(self):
        '''属性:当前连接的设备'''
        return self.__devices_list

    @property
    def BUILD_PROPERTIES(self):
        '''获取系统build相关属性'''
        return self.__system_properties

    @property
    def HEAP_SET(self):
        '''
        系统内存相关设置:
        初始值,受限最大值,不受限最大值
        '''
        __head_set_dic = {}
        __head_set_dic['START'] = self.__system_properties['dalvik.vm.heapstartsize']
        __head_set_dic['MAX_LIMITED'] = self.__system_properties['dalvik.vm.heapgrowthlimit']
        __head_set_dic['MAC_UNLIMITED'] = self.__system_properties['dalvik.vm.heapsize']
        return __head_set_dic

    @property
    def DEVICE_INFO(self):
        '''
        系统内存相关设置:
        设备名称,CPU配置,LOCAL信息,分辨率,系统版本
        '''
        __device_info = {}
        __device_info['NAME'] = "%s - %s" % (
        self.__system_properties['ro.product.brand'], self.__system_properties['ro.product.model'])
        __device_info['CPU'] = self.__system_properties['ro.product.cpu.abi']
        __device_info["MEMORY"] = self.shell("cat /proc/meminfo", grep="MemTotal")[0].split(':')[-1].lstrip(" ").rstrip(
            " ")
        __device_info['LOCAL'] = self.__system_properties['ro.product.locale']
        __device_info["DISPLAY"] = self.shell("dumpsys window displays", grep="init")[0].split('cur=')[0].split("=")[
            1].rstrip(" ")
        __device_info["OS_VERSION"] = self.__system_properties['ro.build.version.release']
        return __device_info

    @property
    def SYSTEM_STATUS(self):
        __system_status = {}
        __power_info = self.shell("dumpsys power")
        for __info in __power_info:
            if __info.count("mBatteryLevel="):
                __system_status['BATTERY_LEVE:'] = __info.split("=")[-1]
            elif __info.count("mScreenOffTimeoutSetting="):
                __system_status['SCREENOFF_TIMEOUT'] = __info.split("=")[-1]
            elif __info.count("mScreenBrightnessSetting="):
                __system_status['DISPLAY_BRIGHTNESS'] = __info.split("=")[-1]
            elif __info.count(" mScreenBrightnessModeSetting="):
                __system_status['DISPLAY_MODE'] = (lambda x: x == '1' and "Auto" or "Manual")(__info.split("=")[-1])
        return __system_status

    def shell(self, cmd, serial=None, timeout=None, grep=None):
        '''
        运行设备端命令
        :param shell_cmd: 命令
        :param timeout: 超时时间，默认无
        :return: 命令运行返回值
        '''
        # 1. 获取命令运行结果
        if serial == None:
            __retVal = self.__adb.shell(cmd, timeout=timeout)
        else:
            __retVal = self.__adb.shell(cmd, serial, timeout=timeout)
        # 2. 处理命令返回结果
        try:
            __retVal.encode('UTF-8')
        except:
            pass
        __retVal = __retVal.replace("\r\n", '\r').split('\r')
        # 3. 返回数据
        if grep == None:
            return __retVal
        else:
            __grep_val = []
            for line in __retVal:
                if line.count(grep):
                    __grep_val.append(line)
            return __grep_val

    def senKey(self, key_code):
        '''
        发送按键
        :KEY_CODE: 系统按键编码
        :return: null
        '''
        if KEY_CODE.SYSKEYLIST.count(key_code) == 0 and KEY_CODE.NORKEYLIST.count(key_code) == 0:
            return -1
        else:
            self.shell('input keyevent %s' % key_code)
            return 0

    def sendTap(self, xy):
        '''
        发送点击事件
        :xy: 屏幕坐标（x,y）
        :return:'''
        if len(xy) > 2 or xy[0] < 0 or xy[1] < 0:
            return -1
        else:
            self.shell('input tap  %s %s' % (xy[0], xy[1]))

    def sendSwip(self, from_xy, to_xy):
        '''
        发送滑动事件
        :from_xy: 起始屏幕坐标（x,y）
        :to_xy: 终点屏幕坐标（x,y）
        :return:
        '''
        if len(from_xy) > 2 or from_xy[0] < 0 or from_xy[1] < 0:
            return -1
        if len(to_xy) > 2 or to_xy[0] < 0 or to_xy[1] < 0:
            return -1

        self.shell('input swipe %s %s %s %s' % (from_xy[0], from_xy[1], to_xy[0], to_xy[1]))

    def startApp(self, component):
        '''启动App
        component: ${package_name}/${package_name}${activity_name}
        :return:
        '''
        __cmd = "am start -W com.tencent.mm/.ui.LauncherUI"
        __ret_val = self.shell(__cmd)
        if __ret_val[1].count('Error'):
            return "failed:", __ret_val[2]
        else:
            return "ok", __ret_val[4].split(" ")

    def forceStopApp(self, package_name):
        '''
        强制关闭app
        :param package_name:
        :return:
        '''
        self.shell('am force-stop ' + package_name)

    def get_current_component(self):
        '''
        获取当前Activity
        :return: 当前activity名称
        '''
        __retVal = self.shell('dumpsys window', grep="mCurrentFocus=")[0]
        __comp = __retVal.split(" ")[-1].split("}")[0]
        return __comp

    def create_dir(self, dir_name):
        '''建立设备端文件夹'''
        _retVal = self.shell('mkdir -p %s' % (dir_name))
        if _retVal.count('exists') == 0:
            return 0
        else:
            return -1

    def init_tools_dir(self, type):
        '''初始化Smonkey工作目录'''
        __date = time.strftime("%Y%m%d")
        __work_dir = '/sdcard/zTools/' + __date + "/" + type
        __retval = self.create_dir(__work_dir)
        if __retval == 0:
            return 0, __work_dir
        else:
            return -1, __work_dir

    def clear_dev_log(self):
        '''清楚设备端内容log'''
        # adb shell logcat -c 清楚内存log
        __clear_log = 'logcat -c'
        self.__adb.shell(__clear_log)

    def dump_dev_log(self, flag='', type=0):
        '''dump设备端log'''
        # adb shell logcat -v raw -d > d:/xx.log    log 简要
        # adb shell logcat -v time -d > d:/xx.log   log 含时间戳
        # log文件存储地址
        __save_path = self.init_tools_dir("log")[1]
        __log_file_name = flag + '_' + time.strftime("%Y%m%d-%H%M%S") + '.log'
        __log_save_path = __save_path + '/' + __log_file_name
        if type == 0:
            __log_cmd = 'logcat -v time -d > ' + __log_save_path
        else:
            __log_cmd = 'logcat -v raw -d > ' + __log_save_path
        self.__adb.shell(__log_cmd)
        return 0, __log_save_path

    def cap_screen(self, file_flage='', save_path=None):
        '''截屏'''
        # 判断截屏文件名
        __file_name = file_flage + '_' + time.strftime("%Y%m%d-%H%M%S") + '.png'
        # 初始化存储地址
        __save_path = self.init_tools_dir('screen')[1]
        __save_file = __save_path + '/' + __file_name
        # 执行截屏命令
        __cmd_capScreen = '/system/bin/screencap -p %s' % (__save_file)
        __retVal = self.shell(__cmd_capScreen)
        if __retVal.count('Error'):
            return -1, __retVal
        else:
            return 0, __save_file


class ADBServerException(Exception): pass


class DeviceStatuException(Exception): pass


class NoDeviceConnectionException(Exception): pass
