# -*- coding: utf8 -*-
'''
封装Android设备端常用操作, 基于adbpy.adb类库
@Created on 2016-05-17
@author: jy.zenist.song

@Lasted edite by jy.zenist.song 2016.05.17
'''

import os
import csv

class CSVHelper():

    def __init__(self, file_name, type="r"):
        self.__open_csv_file(file_name, type)


    def __open_csv_file(self, file_name, type):
        if type in ['r', 'read']:
            if os.path.isfile(file_name):
                self.__csv_file = file(file_name, 'rb')
            else:
                raise OpenFileNotExistsExcetption
        elif type in ['w', 'write']:
            self.__csv_file = file(file_name, 'wb')
        else:
            raise OpenTypeExcetption

    @property
    def CONTENT(self):
        try:
            __csv_content = []
            __csv_reader = csv.reader(self.__csv_file)
            for __line in __csv_reader:
                __csv_content.append(__line)
        except Exception, e:
            print("[ERROR]:"+str(e))
            raise ReadCSVContentException
        finally:
            self.__csv_file.close()
        return __csv_content

    def write(self, content_list):
        try:
            __csv_writer = csv.writer(self.__csv_file)
            for __line in content_list:
                __csv_writer.writerow(__line)
        except Exception, e:
            print("[ERROR]:"+str(e))
            raise WriteCSVContentException
        finally:
            self.__csv_file.close()
        return len(content_list)



class OpenTypeExcetption(Exception): pass
class OpenFileNotExistsExcetption(Exception): pass
class ReadCSVContentException(Exception): pass
class WriteCSVContentException(Exception): pass