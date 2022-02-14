# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hulk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 200)
        Dialog.setStyleSheet(u"background-color: rgb(158, 255, 55);")
        self.buscar = QPushButton(Dialog)
        self.buscar.setObjectName(u"buscar")
        self.buscar.setGeometry(QRect(340, 30, 141, 28))
        self.caminho = QLineEdit(Dialog)
        self.caminho.setObjectName(u"caminho")
        self.caminho.setGeometry(QRect(20, 30, 311, 28))
        self.caminho.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 100, 471, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.redimensionar = QPushButton(self.verticalLayoutWidget)
        self.redimensionar.setObjectName(u"redimensionar")

        self.verticalLayout.addWidget(self.redimensionar)

        self.barra_de_progresso = QProgressBar(Dialog)
        self.barra_de_progresso.setObjectName(u"barra_de_progresso")
        self.barra_de_progresso.setGeometry(QRect(130, 80, 241, 23))
        self.barra_de_progresso.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.barra_de_progresso.setValue(0)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Hulk", None))
        self.buscar.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.caminho.setPlaceholderText(QCoreApplication.translate("Dialog", u" Caminho:", None))
        self.redimensionar.setText(QCoreApplication.translate("Dialog", u"Redimensionar", None))
    # retranslateUi

