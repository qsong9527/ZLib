# -*- coding:UTF-8 -*-
# Author: JY. zenist Song

import unittest
from adbpy.adb import Adb

class TestAdbpy(unittest.TestCase):

    def test_get_devices(self):
        ##############################
        # 1. 获取ABDpy实例
        #
        #1. 获取ADBpy实例
        __adbpy = Adb()

        #############################
        # 2. 获取PID_LIST
        #
        #2.1. 运行设备端命令: ps | grep taobao, 获取淘宝相关进程PID命令原始返回字符串
        __retval_1 =  __adbpy.shell("ps | grep taobao")
        # print "Org_str: \t" + __retval_1
        #2.2 将命令返回原始字符串,按行拆分为PID数据记录
        __pid_list = __retval_1.split("\n")
        # print "PID List: %s : %s" % (type(__pid_list), __pid_list)
        #2.3 遍历pid列表,获取每一个PID记录中的PID值
        #2.4 定义一个列表容器,去存储获取的PID值
        __pids = []
        #2.5 遍历PID数据记录列表中的PID数据
        for __pid in __pid_list:
            #2.5.1 如果PID数据的长度<5个字符,则无效
            if len(__pid) < 5:
                pass
            #2.5.2 如果为有效数据,则按" "拆分,获取其中的第4个元素,即PID的值,存储至__pids容器里
            else:
                __pid = __pid.split(" ")[3]
                __pids.append(__pid)

        print("[INFO]PID_LIST= %s" % __pids)

        #############################
        # 3. 获取PID_PSS
        #
        # 获取PIDs容器中的每一个PID对应的PSS TOTAL值
        #3.1. 定义一个容器,用来存储 Tupple->(PID,PSS)
        __pid_pss_info = []
        #3.2. 遍历pid,获取每一个pid对应的PSS Tupple数据
        for __pid in __pids:
            # print "__pid = " + __pid
            #3.2.1 使用dumpsys meminfo ${pid}这个命令,获取原始的返回值
            __returnValue = __adbpy.shell("dumpsys meminfo %s" % __pid)
            #3.2.2 将原始的命令返回值,按行拆分成可以处理的信息
            __pid_mem_info = __returnValue.split('\n')
            # print "__pid info = %s" % __pid_mem_info
            #3.2.3 遍历每一信息,根据标记位获取PSS TOTAL值
            for i in range(len(__pid_mem_info)):
                #3.2.3.1 如果这行信息中还有,标记"Unkonwn",则他的下一行是目标行
                if __pid_mem_info[i].count("Unknown"):
                    # print "Total: %s" % __pid_mem_info[i+1]
                    #3.2.3.2 获取标记Unkonwn行的下一行
                    __pss_info = __pid_mem_info[i+1]
                    #3.2.3.3 使用自定义的mem数据拆分方法进行pss info行数据的拆分,拆分后的第2个数值为PSS值
                    __pss = self.split_memRec(__pss_info)[1]
                    # print "PSS = %s" % __pss
                    #3.2.3.4 将当前PID与PSS值,组合成tuplle数据,存入__pid_pss_info数据结构中
                    __pid_pss_info.append((__pid,__pss))
        #完成类所有PID及其对应的PSS值的获取
        print ('[INFO] PID_PSS = %s' %__pid_pss_info)


        #############################
        # 4. 计算AUT PSS总占用值
        #
        # 获取PIDs容器中的每一个PID对应的PSS TOTAL值
        #进行AUT 总PSS占用的计算
        #4.1. 先定义一个变量,记录总PSS值
        __total_pss = 0
        #4.2. 遍历PSS INFO列表中的每一个PID_PSS Tupple数据
        for __pss in __pid_pss_info:
            #2.1 获取Tuplle中的PSS值,下标为[1],进行累加
            __total_pss += int(__pss[1])
        #4.3. 获取类AUT 总PSS占用
        print("[INFO] AUT_PSS = %s" % __total_pss)

    def split_memRec(self, meminfo):
        '''
        转换MEM INFO记录,将其拆分不含空数据的数组
        :param meminfo:  一条MEM INFO记录
        :return: []
        '''
        #1. 将传入的PSS数据记录根据" "为标记为,进行拆分
        __rec_ele_org = meminfo.split(" ")
        #2. 定义一个新的列表,用于存放转换后的数据
        __rec_ele_pars = []
        #3. 遍历拆分后得到的列表
        for __rec in __rec_ele_org:
            #2.1 如果当前列表数据不为空,添加至新的转转后列表中
            if not __rec == "":
                __rec_ele_pars.append(__rec)
        #4. 返回转换后的数据
        return __rec_ele_pars


    def test_str_count(self):
        __list = ["a 123", "b 234", "TOTAL: 345", "d 456"]
        for __str in __list:
            if __str.count("TOTAL:"):
                print __str

    def test_str_split(self):
        __str = "hello, my name is jy.zenist"
        #以" "为标记进行目标字符串分割,返回列表[]
        # __str.replace("\r\n","\n").split('\n')
        __name = __str.split(" ")[-1]
        print __name

    def test_str_count2(self):
        __str="  abacadaeafag   "
        print __str.count("a")
        print __str.count("z")

        print __str.startswith("aba")
        print "[%s]"% __str.lstrip(" ").rstrip(" ")


        # if __str.count("z"):
        #     print "Find a"
        # else:
        #     print "Find Nothing"





