# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yek.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 27))
        self.menubar.setObjectName("menubar")
        self.menuSe_enekler = QtWidgets.QMenu(self.menubar)
        self.menuSe_enekler.setObjectName("menuSe_enekler")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        self.menuProfil = QtWidgets.QMenu(self.menubar)
        self.menuProfil.setObjectName("menuProfil")
        self.menuLisans = QtWidgets.QMenu(self.menubar)
        self.menuLisans.setObjectName("menuLisans")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionM_teri_Ekle = QtWidgets.QAction(MainWindow)
        self.actionM_teri_Ekle.setObjectName("actionM_teri_Ekle")
        self.actionM_teri_Ara = QtWidgets.QAction(MainWindow)
        self.actionM_teri_Ara.setObjectName("actionM_teri_Ara")
        self.actionM_teri_G_ncelle = QtWidgets.QAction(MainWindow)
        self.actionM_teri_G_ncelle.setObjectName("actionM_teri_G_ncelle")
        self.action_k = QtWidgets.QAction(MainWindow)
        self.action_k.setObjectName("action_k")
        self.actionBize_ula_n = QtWidgets.QAction(MainWindow)
        self.actionBize_ula_n.setObjectName("actionBize_ula_n")
        self.menuSe_enekler.addAction(self.actionM_teri_Ekle)
        self.menuSe_enekler.addAction(self.actionM_teri_Ara)
        self.menuSe_enekler.addAction(self.actionM_teri_G_ncelle)
        self.menuSe_enekler.addAction(self.action_k)
        self.menuYard_m.addAction(self.actionBize_ula_n)
        self.menubar.addAction(self.menuSe_enekler.menuAction())
        self.menubar.addAction(self.menuProfil.menuAction())
        self.menubar.addAction(self.menuLisans.menuAction())
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        self.actionM_teri_Ara.triggered.connect(MainWindow.musteriAra)
        self.actionM_teri_G_ncelle.triggered.connect(MainWindow.musteriGuncelle)
        self.actionM_teri_Ekle.triggered.connect(MainWindow.musteriEkle)
        self.actionBize_ula_n.triggered.connect(MainWindow.bizeUlasin)

        self.pushButton.clicked.connect(MainWindow.veriGetir)
        self.pushButton_2.clicked.connect(MainWindow.stokGetir)
        self.pushButton_3.clicked.connect(MainWindow.raporGetir)
        self.pushButton_4.clicked.connect(MainWindow.geriAl)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YEK OTOMASYON V0.1"))
        self.pushButton.setText(_translate("MainWindow", "Müşteri verilerini getir"))
        self.pushButton_2.setText(_translate("MainWindow", "Stok durumu"))
        self.pushButton_3.setText(_translate("MainWindow", "Rapor"))
        self.pushButton_4.setText(_translate("MainWindow", "Geri al"))
        self.menuSe_enekler.setTitle(_translate("MainWindow", "Seçenekler"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.menuProfil.setTitle(_translate("MainWindow", "Profil"))
        self.menuLisans.setTitle(_translate("MainWindow", "Lisans"))
        self.actionM_teri_Ekle.setText(_translate("MainWindow", "Müşteri Ekle"))
        self.actionM_teri_Ara.setText(_translate("MainWindow", "Müşteri Ara"))
        self.actionM_teri_G_ncelle.setText(_translate("MainWindow", "Müşteri Güncelle"))
        self.action_k.setText(_translate("MainWindow", "Çıkış"))
        self.actionBize_ula_n.setText(_translate("MainWindow", "Bize ulaşın"))

