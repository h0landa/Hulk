import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from hulk import Ui_Dialog
import os
from PIL import Image
from pip import main

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("hulk.ui", self)
        self.buscar.clicked.connect(self.browsefiles)
        self.redimensionar.clicked.connect(self.reduzir_imagem)        
    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')
        self.caminho.setText(fname[0])
    def reduzir_imagem(self):
        image_path = self.caminho.text()
        image_file = Image.open(image_path)
        image_file.save(image_path, quality = 10)

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = mainwindow
widget.show()
sys.exit(app.exec_())