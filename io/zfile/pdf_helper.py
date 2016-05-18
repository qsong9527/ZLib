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
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.barcharts import BarChart
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
        '''定义封面页模板'''
        canvas.saveState()
        canvas.setFont("chsFont", 16)
        canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, self.TITLE)
        canvas.setFont("chsFont", 9)
        canvas.drawString(inch, 0.75*inch, "Copy Right @%s"% self.PAGE_INFO)
        canvas.restoreState()

    def __myLaterPage(self, canvas, doc):
        '''定义内容页模板'''
        canvas.saveState()
        canvas.setFont("chsFont", 9)
        canvas.drawString(inch, 0.75*inch, "Copy Right @%s"% self.PAGE_INFO)
        canvas.restoreState()

    def add_str_content(self, content, size=9, Bold=False, indent=(0.05*inch, 0.05*inch), style=None):
        '''
        增加文字段落
        :param content: 段落内容文字
        :param size: 文字大小,默认9
        :param Bold: 是否加粗,默认False
        :param indent: 段落前后间距,(前间距,后间距)
        :param style: 样式文件
        '''
        if style == None:
            style = styles["Normal"]
        __content = "<font name='chsFont' size=%s>%s</font>" % (size, content)
        if Bold:
            __content = "<b>%s</b>" % __content
        p = Paragraph(__content, style)
        self.__content.append(Spacer(PAGE_WIDTH, indent[0]))
        self.__content.append(p)
        self.__content.append(Spacer(PAGE_WIDTH, indent[1]))


    def add_table_content(self, head, data, rowHeights=[30,14], colWidths=[80], style=None):
        '''
        添加表格
        :param head: 表格标题(第一行)
        :param data: 表格数据
        :param rowHeights: 行高 默认,[30, 14*len(data)]
        :param colWidths: 列宽 默认,[80* len(data)]
        :param style: 样式, 默认:左对齐,上下居中,表头亮蓝色,10号中文字体,黑色0.5网格线
        '''
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
        t=Table(__table_data,
                rowHeights=[rowHeights[0],].extend([rowHeights[1]]*len(data)),
                colWidths=(lambda x: x==[80] and x.extend(x*len(head)) or x)(colWidths),
                style=__sty,
            )
        self.__content.append(t)

    def add_page_break(self):
        '''添加分页符'''
        self.__content.append(PageBreak())

    def add_empty_line(self, lines=1):
        '''添加空行'''
        self.__content.append(Spacer(PAGE_WIDTH, 0.3*inch*lines))

    def add_lineChart(self, title, data, size=(PAGE_WIDTH-100, 300)):
        '''
        添加一个折线图
        :param title: 折线图标题
        :param data: 折线图数据
        '''
        __chart_width, __chart_heigh = size[0], size[1]
        __draw = Drawing(__chart_width, __chart_heigh)
        __draw.add(String(20, __chart_heigh-10, title, fontName="chsFont",fontSize=18, fillColor=colors.black))

        lc = HorizontalLineChart()
        lc.x, lc.y = 25, 50
        lc.width, lc.height = __chart_width-50, __chart_heigh-100
        lc.data = data
        lc.joinedLines = 1

        lc.valueAxis.valueMin = min(data[0])
        lc.valueAxis.valueMax = max(data[0])
        valueRange = lc.valueAxis.valueMax - lc.valueAxis.valueMin
        lc.valueAxis.valueStep = valueRange / 10.0

        __draw.add(lc)
        self.__content.append(__draw)

    def add_linePlotChart(self, title, data, size=(PAGE_WIDTH-100, 300)):

        __chart_width, __chart_heigh = size[0], size[1]
        __draw = Drawing(__chart_width, __chart_heigh)
        __draw.add(String(20, __chart_heigh-10, title, fontName="chsFont",fontSize=18, fillColor=colors.black))
        #LinePlot基本属性
        lp = LinePlot()
        lp.x, lp.y = 25, 50
        lp.width, lp.height = __chart_width-50, __chart_heigh-100
        lp.data = data
        lp.joinedLines = 1
        #X轴配置
        lp.xValueAxis.valueMin = min([x[0] for x in data[0]])
        lp.xValueAxis.valueMax = max([x[0] for x in data[0]])
        valueRange = lp.xValueAxis.valueMax - lp.xValueAxis.valueMin
        lp.xValueAxis.valueStep = valueRange / 10.0
        #Y轴配置
        yValueMin = min([x[1] for x in data[0]])
        yValueMax = max([x[1] for x in data[0]])
        yValueRange = yValueMax - yValueMin
        if (yValueMin-yValueRange/2) > 0:
            lp.yValueAxis.valueMin = yValueMin - yValueRange/2
        else:
            lp.yValueAxis.valueMin = yValueMin
        lp.yValueAxis.valueMax = yValueMax+ 0.01 + yValueRange/3 #+1避免当y轴最大值和最小值相等时valuseStep为0,导致绘图库计算y轴格数时出现除零错误
        lp.yValueAxis.valueStep = (lp.yValueAxis.valueMax - lp.yValueAxis.valueMin)/10
        lp.yValueAxis.visibleGrid = 1
        lp.yValueAxis.gridStrokeWidth = 0.5
        lp.yValueAxis.gridStrokeColor = colors.gray
        __draw.add(lp)
        self.__content.append(__draw)

    def build(self):
        '''生成PDF文件'''
        self.__doc.build(self.__content, onFirstPage=self.__myFirstPage, onLaterPages=self.__myLaterPage)



if __name__ == '__main__':
    pdf = PDFHelper('demo.pdf')
    pdf.add_str_content("俊毅的PDF测试Demo")
    pdf.add_str_content("俊毅的PDF测试Demo", Bold=True)
    pdf.add_str_content("俊毅的PDF测试Demo", size=24)
    pdf.add_empty_line(4)
    data = [[1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,6,7,8,9]]
    pdf.add_lineChart("测试折线图", data)
    pdf.add_empty_line(4)
    data = [[(1,2),(2,3),(3,4),(4,2),(5,1),(6,4),(7,2),(8,3),(9,7),(10,5)]]
    pdf.add_linePlotChart("测试折线图", data)
    pdf.add_page_break()
    pdf.add_str_content("Table Demo")
    __table_head = ["Item","Author", "CreateDate"]
    __table_date = ["Python Reportlib Demo","jy.zenist.song", "2016-05-17"]
    pdf.add_table_content(__table_head,__table_date, colWidths=[360,100,100])
    pdf.build()



