# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1730, 1184)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setToolTipDuration(-2)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frameLayout = QVBoxLayout(self.frame)
        self.frameLayout.setObjectName(u"frameLayout")

        self.verticalLayout.addWidget(self.frame)

        self.periodicityLayout = QHBoxLayout()
        self.periodicityLayout.setObjectName(u"periodicityLayout")
        self.periodicityLabel = QLabel(self.centralwidget)
        self.periodicityLabel.setObjectName(u"periodicityLabel")

        self.periodicityLayout.addWidget(self.periodicityLabel)

        self.periodicityValue = QLabel(self.centralwidget)
        self.periodicityValue.setObjectName(u"periodicityValue")

        self.periodicityLayout.addWidget(self.periodicityValue)

        self.periodicitySlider = QSlider(self.centralwidget)
        self.periodicitySlider.setObjectName(u"periodicitySlider")
        self.periodicitySlider.setMinimum(1)
        self.periodicitySlider.setMaximum(1000)
        self.periodicitySlider.setOrientation(Qt.Horizontal)

        self.periodicityLayout.addWidget(self.periodicitySlider)


        self.verticalLayout.addLayout(self.periodicityLayout)

        self.widthLayout = QHBoxLayout()
        self.widthLayout.setObjectName(u"widthLayout")
        self.widthLabel = QLabel(self.centralwidget)
        self.widthLabel.setObjectName(u"widthLabel")

        self.widthLayout.addWidget(self.widthLabel)

        self.widthValue = QLabel(self.centralwidget)
        self.widthValue.setObjectName(u"widthValue")

        self.widthLayout.addWidget(self.widthValue)

        self.widthSlider = QSlider(self.centralwidget)
        self.widthSlider.setObjectName(u"widthSlider")
        self.widthSlider.setMinimum(1)
        self.widthSlider.setMaximum(100)
        self.widthSlider.setValue(5)
        self.widthSlider.setOrientation(Qt.Horizontal)

        self.widthLayout.addWidget(self.widthSlider)


        self.verticalLayout.addLayout(self.widthLayout)

        self.fractionalLayout = QHBoxLayout()
        self.fractionalLayout.setObjectName(u"fractionalLayout")
        self.fractionalLabel = QLabel(self.centralwidget)
        self.fractionalLabel.setObjectName(u"fractionalLabel")

        self.fractionalLayout.addWidget(self.fractionalLabel)

        self.fractionalValue = QLabel(self.centralwidget)
        self.fractionalValue.setObjectName(u"fractionalValue")

        self.fractionalLayout.addWidget(self.fractionalValue)

        self.fractionalSlider = QSlider(self.centralwidget)
        self.fractionalSlider.setObjectName(u"fractionalSlider")
        self.fractionalSlider.setMinimum(1)
        self.fractionalSlider.setMaximum(1000)
        self.fractionalSlider.setOrientation(Qt.Horizontal)

        self.fractionalLayout.addWidget(self.fractionalSlider)


        self.verticalLayout.addLayout(self.fractionalLayout)

        self.buttonLayour = QHBoxLayout()
        self.buttonLayour.setObjectName(u"buttonLayour")
        self.bgColorSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayour.addItem(self.bgColorSpacer)

        self.bgColorButton = QPushButton(self.centralwidget)
        self.bgColorButton.setObjectName(u"bgColorButton")

        self.buttonLayour.addWidget(self.bgColorButton)


        self.verticalLayout.addLayout(self.buttonLayour)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1730, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)
        self.widthSlider.valueChanged.connect(self.widthValue.setNum)
        self.fractionalSlider.valueChanged.connect(self.fractionalValue.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.periodicityLabel.setText(QCoreApplication.translate("MainWindow", u"Periodicity:", None))
        self.periodicityValue.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.widthValue.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.fractionalLabel.setText(QCoreApplication.translate("MainWindow", u"Fraction:", None))
        self.fractionalValue.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.bgColorButton.setText(QCoreApplication.translate("MainWindow", u"Background Color", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

