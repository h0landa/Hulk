import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow.self)
        loadUi("hulk.ui", self)
        self.browse.clicked.connect(self.browsefiles)
    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')
        self.filename.setText(fname[0])

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackeWidget()
widget.addWidget(mainwindow)
widget.setFixedwidth(400)
widget.setFixedheight(300)
widget.show()
widget.show()
sys.exit(app.exec_())