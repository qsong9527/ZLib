# -*- coding: utf-8 -*-

import unittest
import requests
from requests import exceptions as req_exception
import json


class Request_Demo(unittest.TestCase):
    '''requests类测试,pip install requests'''

    '''
    Request with GET
    '''
    def test_101_getRequestWithoutParam(self):
        #1. 配置所需访问的URL, 及页面期望值
        __url = "https://developers.douban.com/wiki/"
        __exp_val = "豆瓣API快速入门"

        # 2. 使用urllib发送requst,并获取response信息
        __resp = requests.get(__url)

        # 3. 获取 request url 和 status code
        __req_url = __resp.url
        __resp_code = __resp.status_code
        print("[DEBUG]GET %s %s" % (__req_url, __resp_code))
        assert __resp_code == 200, \
            "URL访问失败,CODE=%S, URL=%s" % (__resp_code, __req_url)

        # 4. 获取响应返回数据headers
        __resp_headers = __resp.headers
        print("[DEBUG]HEADERS = %s " % (__resp_headers))
        assert __resp_headers['Content-Type'].lower().count('utf-8'), \
            '返回页面未使用UTF-8编码, [Content-Type]=%s' % __resp_headers['Content-Type']

        # 5.1 response page text: 返回页面嵌套字
        __page_text =  __resp.text
        print("[DEBUG]page_content=%s" % __page_text)
        # 5.2 response page content: 只返回页面展示元素
        __page_content = __resp.content
        print("[DEBUG]page_content=%s" % __page_content)


        #3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val),  \
            '页面检测启失败, 未发现检测关键字[%s], GET %s' % (__exp_val, __url)

    def test_102_getRequestWithParam(self):
        __exp_val = '英雄'
        # 1. 配置所需访问的URL, 及页面期望值
        # 1.1 基础url
        __url = "https://api.douban.com/v2/book/search"
        print("[DEBUG]url=%s" % __url)
        # 1.2 数据
        __data = {'q': '张艺谋'}
        print("[DEBUG]__data=%s" % __data)

        ##2. 使用urllib发送requst,并获取response信息
        __resp = requests.get(__url, params=__data)
        # __page_content = __resp.text.decode('unicode-escape').encode('utf-8')
        # 2.1 request url
        __req_url = __resp.url
        print("[DEBUG]request url=%s" % __req_url)
        # 2.2 response page content
        __page_content = __resp.text.encode('utf-8')
        print("[DEBUG]page_content=%s" % __page_content)

        # 3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val), \
            '页面检测启失败,未发现检测关键字[%s], GET %s' % (__exp_val, __url)


    '''
    Request with POST
    '''
    def test_201_postRequestWithFormData(self):
        '''使用Form作为POST参数类型'''
        __exp_val = '张艺谋'.decode()
        # 1. 配置所需访问的URL, 及页面期望值
        # 1.1 基础url
        __url = "http://httpbin.org/post"

        print("[DEBUG]url=%s" % __url)
        # 1.2 数据
        __data = {'q': '张艺谋'}
        print("[DEBUG]from_data=%s" % __data)


        ##2. 使用urllib发送requst,并获取response信息
        __resp = requests.post(__url, data=__data)
        # 2.1 request url
        __req_url = __resp.url
        print("[DEBUG]request url=%s" % __req_url)
        # 2.2 response page content
        __page_content = __resp.text.decode('unicode-escape').encode('utf-8')
        print("[DEBUG]page_content=%s" % __page_content)

        # 3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val), \
            '页面检测启失败,未发现检测关键字[%s], GET %s' % (__exp_val, __url)

    def test_202_postRequestWithJsonData(self):
        '''使用Json作为POST参数类型'''
        __exp_val = '张艺谋'
        # 1. 配置所需访问的URL, 及页面期望值
        # 1.1 基础url
        __url = "http://httpbin.org/post"
        print("[DEBUG]url=%s" % __url)
        # 1.2 数据
        __data = {'q': '张艺谋'}
        __json = json.dumps(__data)
        print("[DEBUG]json_data=%s" % __json)

        ##2. 使用urllib发送requst,并获取response信息
        __resp = requests.post(__url, json=__json)
        # 2.1 request url
        __req_url = __resp.url
        print("[DEBUG]request url=%s" % __req_url)
        # 2.2 response page content
        __page_content = __resp.text.decode('unicode-escape').decode('unicode-escape').encode('utf-8')
        print("[DEBUG]page_content=%s" % __page_content)

        # 3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val), \
            u'页面检测启失败,未发现检测关键字[%s], GET %s' % (__exp_val, __url)

    def test_203_postRequestWithFile(self):
        '''使用文件(文档或是图片)作为POST参数类型'''
        __exp_val = 'files'
        # 1. 配置所需访问的URL, 及页面期望值
        # 1.1 基础url
        __url = "http://httpbin.org/post"
        print("[DEBUG]url=%s" % __url)
        # 1.2 数据
        __files = {'file':open('test_file', 'rb')}
        print("[DEBUG]file=%s" % __files['file'].name)

        ##2. 使用urllib发送requst,并获取response信息
        __resp = requests.post(__url, files=__files)
        # 2.1 request url
        __req_url = __resp.url
        print("[DEBUG]request url=%s" % __req_url)
        # 2.2 response page content
        __page_content = __resp.text.decode('unicode-escape').decode('unicode-escape').encode('utf-8')
        print("[DEBUG]page_content=%s" % __page_content)

        # 3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val), \
            '页面检测启失败,未发现检测关键字[%s], GET %s' % (__exp_val, __url)


    '''
    Time out
    '''
    def test_301_getRequestWithoutParam(self):
        #1. 配置所需访问的URL, 及页面加载超时时间(秒)
        __url = "https://developers.douban.com/wiki/"
        __timeout = 0.01
        # 2. 使用urllib发送requst,并获取response信息
        try:
            requests.get(__url, timeout=__timeout)
        except req_exception.ReadTimeout,e:
            assert False,\
                "URL访问失败超时,TIMEOUT_SETTING=%s" % (__timeout)


    '''
    Session
    '''


