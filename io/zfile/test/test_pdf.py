# -*- coding: utf8 -*-
'''
封装Android设备端常用操作, 基于adbpy.adb类库
@Created on 2016-05-17
@author: jy.zenist.song

@Lasted edite by jy.zenist.song 2016.05.17
'''

import unittest


class TestReportUserGuide(unittest.TestCase):


    def test_01_start(self):
        from reportlab.pdfgen import canvas
        c = canvas.Canvas("demo.pdf")
        c.drawString(100,100, "Hello World")
        c.showPage()
        c.save()

    def test_02_pageSize(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen.canvas import Canvas
        myCanvas = Canvas('demo.pdf', pagesize=A4)
        width, height = A4
        print width, height
        myCanvas.drawString(width*1/3,height*2/3, "Hello World")
        myCanvas.showPage()
        myCanvas.save()

    def test_03_draw(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen.canvas import Canvas
        from reportlab.lib.units import inch
        c = Canvas('demo.pdf', pagesize=A4)
        c.translate(inch,inch)
        c.setFont("Helvetica", 14)
        c.setStrokeColorRGB(0.2,0.5,0.3)
        c.setFillColorRGB(1,0,1)
        c.line(0,0,0,1.7*inch)
        c.line(0,0,1*inch,0)
        c.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch,fill=1)
        c.rotate(90)
        c.setFillColorRGB(0,0,0.77)
        c.drawString(0.3*inch, -inch, "Hello World")
        c.showPage()
        c.save()

    def test_04_canvasMethods(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen.canvas import Canvas
        from reportlab.lib.units import inch
        c = Canvas('demo.pdf', pagesize=A4)
        c.translate(inch,inch)
        c.setFont("Helvetica", 14)
        c.setAuthor("JY.zenist.song")
        c.setTitle("Hello ReportLib")
        c.drawString(3*inch, 3*inch, "Hello World")
        c.showPage()
        c.save()

    def test_05_coordinates(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen.canvas import Canvas
        from reportlab.lib.units import inch
        from reportlab.lib.colors import pink, black, red, blue, green
        c = Canvas('demo.pdf', pagesize=A4)
        c.translate(inch,inch)
        c.setStrokeColor(pink)
        c.grid([1*inch,2*inch,3*inch,4*inch],[0.5*inch, 1*inch, .5*inch, 2*inch, 2.5*inch])
        c.setFont("Times-Roman", 20)
        c.drawString(0,0, "(0,0) the Origin")
        c.drawString(2.5*inch, 1*inch, "(2.5,1) in inches")
        c.drawString(4*inch, 2.5*inch, "(4,2.5)")
        c.setFillColor(red)
        c.rect(0,2*inch,0.2*inch, 0.3*inch, fill=1)
        c.setFillColor(green)
        c.circle(4.5*inch, 0.4*inch, 0.2*inch, fill=1)
        c.showPage()
        c.save()

    def test_06_fontsize(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen.canvas import Canvas
        from reportlab.lib.units import inch
        from reportlab.lib.colors import red, magenta
        c = Canvas('demo.pdf', pagesize=A4)
        c.translate(inch, inch)
        c.setFont("Times-Roman", 20)
        c.setFillColor(red)
        c.saveState()
        c.drawCentredString(2.75*inch, 2.5*inch,"Font size excmples")
        c.setFillColor(magenta)
        size = 7
        x = 2.3 * inch
        y = 1.3 * inch
        for line in range(7):
            c.setFont("Helvetica", size)
            c.drawRightString(x, y, "%s points" % size)
            c.drawString(x,y, "test")
            y = y-size*1.2
            size = size+1.5
        c.restoreState()
        c.drawString(0,0, "%s" % c.getAvailableFonts())
        c.showPage()
        c.save()

    def test_07_registerFont(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen.canvas import Canvas
        from reportlab.lib.units import inch
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        c = Canvas('demo.pdf', pagesize=A4)
        c.translate(inch, inch)
        c.setFont('chsFont', 32)
        c.drawString(0,0,"这个字体可以支持中文")
        c.showPage()
        c.save()

    def test_08_table(self):
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table
        from reportlab.lib.units import inch
        from reportlab.lib.enums import TA_JUSTIFY
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.lib import fonts, colors

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo.pdf")

        elements.append(Paragraph('<font name="chsFont">AUT OOM测试报告</font>', stylesheet['Title']))
        elements.append(Spacer(1,12))

        stylesheet.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
        stylesheet['Justify'].contName = 'chsFont'

        data  = []
        data.append(["最大值","最小值","平均值"])
        data.append(["120","6","50"])
        ts = [('INNERGRID',(0,0),(-1,-1),0.25, colors.black),("BOX",(0,0),(-1,-1),0.25,colors.black),('FONT',(0,0),(-1,-1), 'chsFont')]
        table = Table(data, 2.1*inch, 0.24*inch, ts)
        elements.append(table)

        doc.build(elements)

    def test_09_docTemplate(self):
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo.pdf")

        elements.append(Paragraph('<font name="chsFont">AUT OOM测试报告</font>', stylesheet['Title']))
        elements.append(Spacer(1,12))

        doc.build(elements)

    def test_11_drawing(self):
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
        from reportlab.pdfbase import pdfmetrics
        from reportlab.graphics.shapes import Drawing, Rect
        from reportlab.pdfbase.ttfonts import TTFont

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo.pdf")

        elements.append(Paragraph('<font name="chsFont">JY.zenist.song - 俊毅</font>', stylesheet['Title']))
        elements.append(Spacer(1,12))

        d = Drawing(400,200)
        d.add(Rect(50,50,300,100, fillColor=colors.yellow))
        elements.append(d)

        doc.build(elements)


    def test_12_drawingRenderPDF(self):
        from reportlab.lib import colors
        from reportlab.graphics.shapes import Drawing, Rect
        from reportlab.graphics import renderPDF

        d = Drawing(400,200)
        d.add(Rect(50,50,300,100, fillColor=colors.yellow))
        renderPDF.drawToFile(d, 'demo.pdf', 'JY.zenist.song')

    def test_13_drawingRenderPNG(self):
        from reportlab.lib import colors
        from reportlab.graphics.shapes import Drawing, Rect
        from reportlab.graphics import renderPM

        d = Drawing(400,200)
        d.add(Rect(50,50,300,100, fillColor=colors.yellow))
        renderPM.drawToFile(d, 'demo.jpg','JPG')

    def test_21_barCharts(self):
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
        from reportlab.pdfbase import pdfmetrics
        from reportlab.graphics.shapes import Drawing
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.graphics.charts.barcharts import VerticalBarChart

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo.pdf")

        elements.append(Paragraph('<font name="chsFont">JY.zenist.song - 俊毅</font>', stylesheet['Title']))
        elements.append(Spacer(1,12))

        d = Drawing(400,200)
        data = [
            (13,5,20,22,37,45,19,4),
            (14,6,21,23,38,46,20,5)
        ]
        bc = VerticalBarChart()
        bc.x = 50
        bc.y = 50
        bc.height = 125
        bc.width = 300
        bc.data = data
        bc.strokeColor = colors.black
        bc.groupSpacing = 10
        bc.barSpacing = 2.5

        bc.valueAxis._valueMin = 0
        bc.valueAxis._valueMax = 50
        bc.valueAxis._valueStep = 10

        bc.categoryAxis.categoryNames = ['1','2','3','4','5','6','7','8']
        # bc.categoryAxis.style = 'stacked'
        d.add(bc)

        elements.append(d)

        doc.build(elements)

    def test_22_lineCharts(self):
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
        from reportlab.pdfbase import pdfmetrics
        from reportlab.graphics.shapes import Drawing
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.graphics.charts.linecharts import HorizontalLineChart
        import random

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo.pdf")

        elements.append(Paragraph('<font name="chsFont">JY.zenist.song - 俊毅</font>', stylesheet['Title']))
        elements.append(Spacer(1,1*inch))

        d = Drawing(400,200)
        data = [
            [13,5,20,22,37,45,19,4],
            # [14,6,21,23,38,46,20,5]
        ]
        for i in range(500):
            data[0].append(random.randint(1,100))
            # data[1].append(random.randint(1,100))
        lc = HorizontalLineChart()
        lc.x = 50
        lc.y = 50
        lc.height = 180
        lc.width = 300
        lc.data = data
        lc.joinedLines = 1
        # lc.categoryAxis.categoryNames = data[0]
        d.add(lc)

        elements.append(d)

        doc.build(elements)

    def test_23_linePlotCharts(self):
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
        from reportlab.pdfbase import pdfmetrics
        from reportlab.graphics.shapes import Drawing
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.graphics.charts.lineplots import LinePlot
        from reportlab.graphics.widgets.markers import makeMarker

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo.pdf")

        elements.append(Paragraph('<font name="chsFont">JY.zenist.song - 俊毅</font>', stylesheet['Title']))
        elements.append(Spacer(1,1*inch))

        d = Drawing(400,200)
        data = [
            [(1,1), (2,2), (2.5,1), (3,3), (4,5)],
        ]
        lp = LinePlot()
        lp.x = 5
        lp.y = 5
        lp.height = 190
        lp.width = 390
        lp.data = data
        lp.joinedLines = 1
        lp.lines[0].symbol = makeMarker('FilledCircle')
        d.add(lp)

        elements.append(d)

        doc.build(elements)

    def test_24_PieCharts(self):
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
        from reportlab.pdfbase import pdfmetrics
        from reportlab.graphics.shapes import Drawing
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.graphics.charts.piecharts import Pie

        pdfmetrics.registerFont(TTFont('chsFont', 'STHeiti Light.ttc'))
        stylesheet = getSampleStyleSheet()

        elements = []
        doc = SimpleDocTemplate("demo.pdf")

        elements.append(Paragraph('<font name="chsFont">JY.zenist.song - 俊毅</font>', stylesheet['Title']))
        elements.append(Spacer(1,1*inch))

        d = Drawing(400,200)
        data = [13,5,20,22,37,45]
        pc = Pie()
        pc.x = 65
        pc.y = 15
        pc.width = 150
        pc.height = 150
        pc.data = data
        pc.labels = ['a','b','c','d','e','f']
        d.add(pc)

        elements.append(d)

        doc.build(elements)

    def test_list_extend(self):
        import random
        __list = []
        for i in range(60000):
            __list.append(random.randint(0,100))
        print __list

    def test_list_min(self):
        data = [[6,2,3,4,5]]
        print min(data[0])







if __name__ == '__main__':
    unittest.main()
