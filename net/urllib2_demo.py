# -*- coding: utf-8 -*-

import unittest
import urllib, urllib2


class URLLib2_Demo(unittest.TestCase):

    def test_01_urlopenWithParam(self):
        '''调用电影所搜API'''
        __exp_val = '英雄'

        # 1. 配置所需访问的URL, 及页面期望值
        # 1.1 基础url
        __url = "https://api.douban.com/v2/movie/search"
        print("[DEBUG]url=%s" % __url)
        # 1.2 数据
        __data = urllib.urlencode({'q': '张艺谋'})
        print("[DEBUG]__data=%s" % __data)

        ##2. 使用urllib发送requst,并获取response信息
        __resp = urllib2.urlopen(__url, __data)
        __page_content = __resp.read().decode('unicode-escape').encode('utf-8')
        print("[DEBUG]page_content=%s" % __page_content)

        # 3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val), \
            '页面检测启失败,未发现检测关键字[%s], GET %s' % (__exp_val, __url)

    def test_02_urlopenWithHeader(self):
        '''调用电影所搜API'''
        __exp_val = '英雄'
        # 1. 配置所需访问的URL, 及页面期望值
        # 1.1 基础url
        __url = "https://api.douban.com/v2/movie/search"
        print("[DEBUG]URL=%s" % __url)
        # 1.2 数据
        __data = urllib.urlencode({'q': '张艺谋'})
        print("[DEBUG]DATA=%s" % __data)
        # 1.3 headers配置 - agent
        __agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
        __headers = {'User-Agent':__agent}
        print("[DEBUG]HEAD=%s" % __headers)
        # 1.5 生成request
        __request = urllib2.Request(__url, __data, __headers)

        ##2. 使用urllib发送requst,并获取response信息
        __resp = urllib2.urlopen(__request)
        __page_content = __resp.read().decode('unicode-escape').encode('utf-8')
        print("[DEBUG]page_content=%s" % __page_content)
        # 3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val), \
            '页面检测启失败,未发现检测关键字[%s], GET %s' % (__exp_val, __url)

        #常用移动端 UserAgent:
        #1. Android原生
        __agent = "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
        #2. IOS Safria
        __agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3"


