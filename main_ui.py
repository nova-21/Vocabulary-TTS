# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playAll = QtWidgets.QPushButton(self.centralwidget)
        self.playAll.setGeometry(QtCore.QRect(10, 20, 81, 23))
        self.playAll.setObjectName("playAll")
        self.tabla = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla.setGeometry(QtCore.QRect(10, 70, 580, 501))
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(0)
        self.tabla.setRowCount(0)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.verticalHeader().setStretchLastSection(False)
        self.playThis = QtWidgets.QPushButton(self.centralwidget)
        self.playThis.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.playThis.setObjectName("playThis")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.getMp3 = QtWidgets.QPushButton(self.centralwidget)
        self.getMp3.setGeometry(QtCore.QRect(260, 20, 75, 23))
        self.getMp3.setObjectName("getMp3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(340, 20, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocabulary"))
        self.playAll.setText(_translate("MainWindow", "Play All"))
        self.playThis.setText(_translate("MainWindow", "Play only this"))
        self.pushButton.setText(_translate("MainWindow", "Stop"))
        self.getMp3.setText(_translate("MainWindow", "Get mp3"))

        df = pd.read_csv('words.csv', encoding='latin-1')
        df['French'] = df['French'].replace({'(inf)': ' '})
        self.tabla.setColumnCount(len(df.columns))
        self.tabla.setHorizontalHeaderLabels(df.columns)
