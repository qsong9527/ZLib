#coding: UTF-8

import unittest

from io.zfile.csv_helper import CSVHelper


class TestCsvModule(unittest.TestCase):


    def test_csv_content(self):
        '''
        获取CSV文件内容
        :return:
        '''
        __csv_content = CSVHelper("./test/demo.csv").CONTENT
        print type(__csv_content),__csv_content


    def test_csv_write(self):
        '''
        写入SCSV文件
        :return:
        '''
        __row_data = [
            ["Hello", "csv"],
            ["my name is ","jy.zenist.song"]
        ]
        print CSVHelper("./test/demo.csv",'w').write(__row_data)



if __name__ == '__main__':
    unittest.main()
