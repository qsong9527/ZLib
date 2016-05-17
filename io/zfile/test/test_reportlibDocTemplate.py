# -*- coding: utf8 -*-
'''
@Created on 2016-5-17
@author: jy.zenist.song

@Lasted edite by jy.zenist.song 2016.5.17
'''

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch

styles = getSampleStyleSheet()
PAGE_HEIGHT = A4[1]
PAGE_WIDTH = A4[0]

class DemoDocTemplate():

    Title = "Hello world"
    pageinfo = "platypus example"

    def myFirstPage(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Times-Bold", 16)
        canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, self.Title)
        canvas.setFont("Times-Roman", 9)
        canvas.drawString(inch, 0.75*inch, "First Page / %s"% self.pageinfo)
        canvas.restoreState()

    def myLaterPage(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Times-Roman", 9)
        canvas.drawString(inch, 0.75*inch, "First Page / %s"% self.pageinfo)
        canvas.restoreState()

    def go(self):
        doc = SimpleDocTemplate("demo.pdf")
        Story = [Spacer(1, 2*inch)]
        style = styles["Normal"]
        for i in range(100):
            bogustext = ("This is Paragraph number %s. " % i) * 20
            p = Paragraph(bogustext, style)
            Story.append(p)
            Story.append(Spacer(1, 0.2*inch))
        doc.build(Story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPage)


if __name__ == '__main__':
    DemoDocTemplate().go()



