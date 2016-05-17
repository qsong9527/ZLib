# -*- coding: utf8 -*-
'''
封装Android设备端常用操作, 基于adbpy.adb类库
@Created on 2016-05-17
@author: jy.zenist.song

@Lasted edite by jy.zenist.song 2016.05.17
'''

import unittest

from reportlab.platypus import *
from io.zfile.pdf_helper import PDFHelper


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

    def test_08_forms(self):
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

        from reportlab.lib.units import inch
        from reportlab.lib.enums import TA_JUSTIFY
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfgen import canvas
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





if __name__ == '__main__':
    unittest.main()
