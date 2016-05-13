# -*- coding: utf-8 -*-

import unittest
import urllib

class URLLib_Demo(unittest.TestCase):
    '''urllib'''

    '''
    URL相关编解码
    '''
    def test_101_urlEncode(self):
        #将字典中的键值转化为url参数
        __date = {'q':'张艺谋', 'type':'文学'}
        __param = urllib.urlencode(__date)
        print __param


    def test_102_urlQuote(self):
        #quote: 将url数据获取之后，并将其编码，从而适用与URL字符串中，使其能被打印和被web服务器接受
        __url = "https://api.douban.com/v2/movie/search?q=张艺谋"
        print urllib.quote(__url)
        print urllib.quote_plus(__url)
        #unquote : 与quote相反
        __url2 = "https%3A%2F%2Fapi.douban.com%2Fv2%2Fmovie%2Fsearch%3Fq%3D%E5%BC%A0%E8%89%BA%E8%B0%8B"
        print urllib.unquote(__url2)
        print urllib.unquote_plus(__url2)

    '''
    URL open
    '''
    def test_201_urlopenWithoutParam(self):
        '''无参数访问API接口
        Eg. 访问并验证豆瓣开发者API wiki页面
        '''
        #1. 配置所需访问的URL, 及页面期望值
        __url = "https://developers.douban.com/wiki/"
        __exp_val = "豆瓣API快速入门"
        #2. 使用urllib发送requst,并获取response信息
        __resp = urllib.urlopen(__url)
        __page_content =  __resp.read()
        #3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val),  \
            '页面检测启失败, 未发现检测关键字[%s], GET %s' % (__exp_val, __url)

    def test_202_urlopenWithParam(self):
        '''调用电影所搜API'''
        #1. 配置所需访问的URL, 及页面期望值
        __exp_val = '英雄'
        __param = urllib.urlencode({'q':'张艺谋'})
        print("[DEBUG]params=%s"%__param)
        __url = "https://api.douban.com/v2/movie/search?%s"%__param
        print("[DEBUG]url=%s" % __url)
        ##2. 使用urllib发送requst,并获取response信息
        __resp = urllib.urlopen(__url)
        __page_content =  __resp.read().decode('unicode-escape').encode('utf-8')
        print __page_content
        #3. 验证response信息中是否包含期望值
        assert __page_content.count(__exp_val),  \
            '页面检测启失败,未发现检测关键字[%s], GET %s' % (__exp_val, __url)




