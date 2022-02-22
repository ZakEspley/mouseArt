import imp
import sys
import typing

import numpy as np
from PIL import Image, ImageDraw, ImageQt
from PIL.ImageColor import getrgb
from PySide2 import QtWidgets
from PySide2.QtGui import QBrush, QColor, QPainter, QPainterPath, QPen
from PySide2.QtWidgets import QGraphicsScene, QGraphicsView, QColorDialog
from PySide2.QtCore import QPointF, Qt
# from numba.experimental import jitclass
# from numba import jit
from itertools import groupby

from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.getData)
        self.periodicitySlider.valueChanged.connect(self.setPeriodicity)
        self.periodicitySlider.sliderReleased.connect(self.reRun)
        self.filteredData = None
        self.data = None
        self.positions = None
        self.border =  1.1
        self.periodicity = 1
        self.xSize = None
        self.ySize = None
        self.im = None
        self.qim = None
        self.draw = None
        self.loaded = False
        self.scene = QGraphicsScene(self.frame)
        self.pen = QPen(QColor.fromHsl(0, 255, 127, 255))
        self.width = 5
        self.pen.setWidth(self.width)
        self.pen.setCosmetic(True)
        self.brush = QBrush(QColor(255,0,0))
        self.view = QGraphicsView(self.scene, self.frame)
        self.frameLayout.addWidget(self.view)
        self.path = QPainterPath()
        self.fractionalPoints = 1

        self.widthSlider.valueChanged.connect(self.setWidth)
        self.widthSlider.sliderReleased.connect(self.reRun)
        self.fractionalSlider.valueChanged.connect(self.setFractionalPoints)
        self.fractionalSlider.sliderReleased.connect(self.reRun)
        self.bgColorButton.clicked.connect(self.setbgColor)


        self.view.wheelEvent = self.zoom
        # self.scene.mouseMoveEvent = self.pan
        
    def zoom(self, event):
        if event.delta() > 0:
            self.view.scale(1.1, 1.1)
        else:
            self.view.scale(0.9,0.9)
    
    def pan(self, event):
        p = event.scenePos()
        lp = event.lastScenePos()
        dx = p.x()-lp.x()
        dy = p.y()-lp.y()
        self.view.translate()
        # print(dx, dy)
        # self.view.horizontalScrollBar().setValue(self.view.horizontalScrollBar().value() + dx)
        # self.view.verticalScrollBar().setValue(self.view.verticalScrollBar().value() + dy)
    
    def setFractionalPoints(self):
        self.fractionalPoints = self.fractionalSlider.value()
    
    def setbgColor(self):
        color = QColorDialog.getColor()
        self.view.setBackgroundBrush(QBrush(QColor(color)))
    
    def setPeriodicity(self):
        self.periodicity = self.periodicitySlider.value()
        self.periodicityValue.setText(str(self.periodicity))
    
    def setWidth(self):
        self.width = self.widthSlider.value()
        self.pen.setWidth(self.width)

    def reRun(self):
        if self.loaded:
            self.drawTrace()

    def drawTrace(self):
        self.scene.clear()
        hue = 0
        lastX = self.positions[0,0]
        lastY = self.positions[0,1]
        for i, position in enumerate(self.positions):
            if i%self.fractionalPoints==0:
                path = QPainterPath(QPointF(lastX, lastY))
                px, py = position
                path.lineTo(px, py)
                # path.cubicTo(px+10, py-10, px-10, py-10, px, py)
                self.scene.addPath(path,self.pen)
                lastX = px
                lastY = py
                if i%self.periodicity == 0:
                    hue = (hue+1)%359
                    self.pen.setColor(QColor.fromHsl(hue, 255, 127, 255))

    def getData(self, s):
        # self.painter.begin(self.view)
        # self.painter.setPen(QPen(QColor.fromHsl(0, 255, 127, 255)))
        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        print(filename)
        self.compileData(filename)
        
    def compileData(self, filename):
        self.data = np.genfromtxt(filename, delimiter=",")
        print(self.data.shape)
        self.data = np.delete(self.data,[0,1,2,5,6], axis=1)
        lastX = 0
        lastY = 0
        # self.positions = np.empty((0,2))
        
        self.delta = np.array([np.array(k)*len(list(g)) for k,g in groupby(self.data, key=lambda t: (t[0], t[1]))])
        self.positions = np.cumsum(self.delta, axis=0)
        # for dx, dy in self.filteredData:
        #     px = lastX+dx
        #     py = lastY+dy
        #     self.positions = np.append(self.positions, [[px, py]], axis=0)
        #     lastX = px
        #     lastY = py
        self.loaded = True
        self.drawTrace()
        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
