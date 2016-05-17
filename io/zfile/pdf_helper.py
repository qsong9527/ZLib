# -*- coding: utf8 -*-
'''
@Created on 2016-5-17
@author: jy.zenist.song

@Lasted edite by jy.zenist.song 2016.5.17
'''

import platform

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont


styles = getSampleStyleSheet()
PAGE_HEIGHT = A4[1]
PAGE_WIDTH = A4[0]

class myDocTemplate(SimpleDocTemplate):

    def __init__(self, fileName,**kw):
        SimpleDocTemplate.__init__(self,fileName,**kw)
        self.leftMargin, self.rightMargin = 0.5*inch,0.5*inch
        self.topMargin,self.bottomMargin = 0.5*inch,0.5*inch


class PDFHelper():

    def __init__(self, file_path):
        self.__register_font()
        self.__doc = myDocTemplate(file_path)
        self.__title = "JY.zenist.song PDF实例"
        self.__page_info = "JY.zenist.song"
        self.__content = [PageBreak()]

    @property
    def TITLE(self):
        return self.__title

    @TITLE.setter
    def TITLE(self, title):
        self.__title = title

    @property
    def PAGE_INFO(self):
        return self.__page_info

    @PAGE_INFO.setter
    def PAGE_INFO(self, page_info):
        self.__page_info = page_info

    def __register_font(self):
        '''
        根据系统平台类型,注册不同的中文显示字体文件
        :return:
        '''
        if platform.system() == 'Windows':
            if platform.win32_ver()[0] == '8':
                __platform = 'Win8'
            else:
                __platform =  'Win7orLower'
        elif platform.system() == 'Linux':
            __platform =  'Linux'
        else:
            __platform =  'MacOS'

        if __platform != 'Win7orLower':
            if __platform == 'Win8':
                pdfmetrics.registerFont(TTFont('chsFont','msyh.TTC'))
            elif __platform == 'MacOS':
                pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
            elif __platform == 'Linux': #未确定linux上是否能直接用此字体，待实际使用验证
                pdfmetrics.registerFont(TTFont('chsFont','STHeiti Light.ttc'))
        else:
            pdfmetrics.registerFont(TTFont('chsFont','msyh.TTF'))


    def __myFirstPage(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("chsFont", 16)
        canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, self.TITLE)
        canvas.setFont("chsFont", 9)
        canvas.drawString(inch, 0.75*inch, "Copy Right @%s"% self.PAGE_INFO)
        canvas.restoreState()

    def __myLaterPage(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("chsFont", 9)
        canvas.drawString(inch, 0.75*inch, "Copy Right @%s"% self.PAGE_INFO)
        canvas.restoreState()

    def save(self):
        self.__doc.build(self.__content, onFirstPage=self.__myFirstPage, onLaterPages=self.__myLaterPage)

    def add_str_content(self, content, size=22, style=None):
        if style == None:
            style = styles["Normal"]
        p = Paragraph(content, style)
        # self.__content.append('<font size=%s>%s</font>' %(size, p))
        self.__content.append(p)


    def add_table_content(self, head, data, rowHeights=[30,14], colWidths=[80], style=None):
        __table_data = [head]
        __table_data.append(data)
        if style == None:
            __sty = [
                ('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ('BACKGROUND',(0,0),(-1,0),colors.lightblue),
                ('FONT',(0,0),(-1,0),'chsFont'),
                ('SIZE',(0,0),(-1,0),10),
                ('GRID',(0,0),(-1,-1),0.5,colors.black),
                ('RIGHTPADDING',(0,0),(-1,-1),0),
            ]
        t=Table(__table_data,style=__sty,
               rowHeights=[rowHeights[0],].extend([rowHeights[1]]*len(data)),
               colWidths=(lambda x: x==[80] and x.extend(x*len(head)) or x)(colWidths))  #列宽如果使用'x%'的形式来设定，首列的Log文件名不会自动换行，所以此处用hardcoded的数字
        self.__content.append(t)

    def add_page_break(self):
        self.__content.append(PageBreak())

    def add_empty_line(self):
        self.__content.append(Spacer(PAGE_WIDTH), 0.2*inch)

    #TBD:
    #1. 字体样式
    #2. 各种图标生成: 饼图,条形图,折线图
    #3. add_str_content 增加 字体大小选择





if __name__ == '__main__':
    pdf = PDFHelper('demo.pdf')
    pdf.add_str_content("Test Demo")
    pdf.add_page_break()
    pdf.add_str_content("Table Demo")
    __table_head = ["Item","Author", "CreateDate"]
    __table_date = ["Python Reportlib Demo","jy.zenist.song", "2016-05-17"]
    pdf.add_table_content(__table_head,__table_date, colWidths=[360,100,100])
    pdf.save()



