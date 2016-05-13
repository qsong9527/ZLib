# -*- coding: UTF-8 -*-

import argparse
import sys

def __analysis_args():
    '''处理命令行所传入参数'''

    #1. 初始化,设置描述信息
    __description = "This is a demo script, uesd to show how argprase uesage"
    parser = argparse.ArgumentParser(description=__description)

    #2. 增加一个参数
    parser.add_argument('-p', '--appPackageName', required=True, help="The package name of your AUT")
    parser.add_argument('-f', '--LogCSVFileName', required=True, help="The path for trace-log save")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = __analysis_args()
    print args.appPackageName
    print args.LogCSVFileName