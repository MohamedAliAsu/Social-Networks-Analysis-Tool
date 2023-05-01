import matplotlib.pyplot as plot

import networkx as nx
import sys
import mainwindow
from PyQt5 import QtWidgets



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mainwindow.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

sys.exit(app.exec_())
