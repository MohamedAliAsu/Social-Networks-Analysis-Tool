# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import visualisation

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 110, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 290, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 290, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nodesPath = QtWidgets.QLabel(self.centralwidget)
        self.nodesPath.setGeometry(QtCore.QRect(160, 380, 200, 50))
        self.nodesPath.setText("")
        self.nodesPath.setObjectName("nodesPath")
        self.edgesPath = QtWidgets.QLabel(self.centralwidget)
        self.edgesPath.setGeometry(QtCore.QRect(550, 380, 200, 50))
        self.edgesPath.setText("")
        self.edgesPath.setObjectName("edgesPath")
        self.uploadN = QtWidgets.QPushButton(self.centralwidget)
        self.uploadN.setGeometry(QtCore.QRect(140, 340, 93, 28))
        self.uploadN.setObjectName("uploadN")
        self.uploadE = QtWidgets.QPushButton(self.centralwidget)
        self.uploadE.setGeometry(QtCore.QRect(530, 340, 93, 28))
        self.uploadE.setObjectName("uploadE")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(240, 460, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.directed = QtWidgets.QCheckBox(self.centralwidget)
        self.directed.setGeometry(QtCore.QRect(370, 360, 90, 21))

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.edgesFile = ""
        self.nodesFile = ""
        self.uploadN.clicked.connect(self.browseNodes)
        self.uploadE.clicked.connect(self.browseEdges)
        self.pushButton.clicked.connect(self.preview)

    def preview(self):
        self.window = QtWidgets.QWidget()
        self.ui = visualisation.Ui_Form()
        self.ui.setupUi(self.window,self.nodesFile,self.edgesFile,self.directed.isChecked())
        self.window.show()


    def browseNodes(self):
        fName = QFileDialog.getOpenFileName(self.uploadN,"Upload File","C:","Csv Files (*.csv)")
        if(fName):
            self.nodesFile = fName[0]
            self.nodesPath.setText(self.nodesFile)
        if (self.nodesFile != "" and self.edgesFile != ""):
            self.pushButton.setEnabled(True)



    def browseEdges(self):
        fName = QFileDialog.getOpenFileName(self.uploadN,"Upload File","C:","Csv Files (*.csv)")
        if(fName):
            self.edgesFile = fName[0]
            self.edgesPath.setText(self.edgesFile)
        if (self.nodesFile != "" and self.edgesFile != ""):
            self.pushButton.setEnabled(True)









    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini Social Networks Analyzer"))
        self.label.setText(_translate("MainWindow", "Upload Nodes and Edges Csv Files to Proceed"))
        self.label_2.setText(_translate("MainWindow", "Nodes"))
        self.label_3.setText(_translate("MainWindow", "Edges"))
        self.uploadN.setText(_translate("MainWindow", "Browse..."))
        self.uploadE.setText(_translate("MainWindow", "Browse..."))
        self.pushButton.setText(_translate("MainWindow", "PREVIEW"))
        self.directed.setText("Directed")





