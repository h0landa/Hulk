import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QProgressBar
from PyQt5.uic import loadUi
from main import Ui_Dialog
from PyQt5.QtCore import QTimer
import os
from PIL import Image
from pip import main

class MainWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("hulk.ui", self)
        self.buscar.clicked.connect(self.browsefiles)
        self.redimensionar.clicked.connect(self.reduzir_imagem)
        self.barra_de_progresso.setMaximum(100)
        self.barra_de_progresso.setValue(0)
    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/')
        self.caminho.setText(fname[0])
    def reduzir_imagem(self):
        image_path = self.caminho.text()
        image_file = Image.open(image_path)
        image_file.save(image_path, quality = 5)
        timer = QTimer(self)
        timer.timeout.connect(self.cronometro)
        timer.start(30)
        
    def cronometro(self):
        self.barra_de_progresso.setValue(self.barra_de_progresso.value() + 1)

        


        


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = mainwindow
widget.show()
sys.exit(app.exec_())