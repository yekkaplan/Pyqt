from desing import login
from desing import yek
from desing import musteriekle
from desing import musteriAra
from desing import musteriguncelle
from PyQt5 import QtWidgets
import sys
import sqlite3

class login(QtWidgets.QDialog,login.Ui_Dialog):
    def __init__(self,parent = None):
        super(login,self).__init__(parent)
        self.setupUi(self)
        self.g =  anamain(parent = self)

    def girisyap(self):

        self.kadi = self.lineEdit.text()
        self.pasw = self.lineEdit_2.text()

        if(self.kadi == "yek" and self.pasw == "2802"):
             self.g.show()

        else:
            self.close()

    def kayitOl(self):
        pass



class anamain(QtWidgets.QMainWindow,yek.Ui_MainWindow):
    def __init__(self,parent = None):
        super(anamain,self).__init__(parent)
        self.setupUi(self)
        self.veriTabaniOlustur()
        self.g = musteriekle()
        self.g2 = musteriAra()
        self.g3 = musteriGuncelle()

    def veriTabaniOlustur(self):
        self.con =  sqlite3.connect("otomasyon.db")

        self.cursor = self.con.cursor()

        self.sorgu = "CREATE TABLE IF NOT EXISTS müsteriler(siparis_no İNT,musteri_adi_soyadi TEXT,musteri_numara TEXT,musteri_adres TEXT,musteri_urun Text)"

        self.cursor.execute(self.sorgu)

        self.con.commit()


    def veriGetir(self):
        self.con = sqlite3.connect("otomasyon.db")
        self.cursor = self.con.cursor()
        self.sorgu = "SELECT *FROM müsteriler"
        self.cursor.execute(self.sorgu)
        db = self.cursor.fetchall()
        for rownumber,row_data in enumerate(db):
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(rownumber, column_number, QtWidgets.QTableWidgetItem(str(data)))



    def stokGetir(self):        self.label.linkActivated['QString'].connect(MainWindow.labelLink)

        pass
    def geriAl(self):
        pass
    def raporGetir(self):
        pass
    def musteriAra(self):
        self.g2.show()
    def musteriGuncelle(self):
        self.g3.show()
    def musteriEkle(self):
        self.g.show()
    def bizeUlasin(self):
        pass


class musteriGuncelle(QtWidgets.QDialog,musteriguncelle.Ui_Dialog):
    def __init__(self,parent = None):
        super(musteriGuncelle,self).__init__()
        self.setupUi(self)

    def baglanti(self):

        self.con = sqlite3.connect("otomasyon.db")

        self.cursor = self.con.cursor()
    def bul(self):

        self.con = sqlite3.connect("otomasyon.db")
        self.cursor = self.con.cursor()
        self.sorgu = "Select *From müsteriler where siparis_no = ?"
        self.cursor.execute(self.sorgu,(self.lineEdit_2.text(),))

        self.data = self.cursor.fetchall()

        if (len(self.data) == 0):
            print("Ürün bulunamadı.")

        else:
            for rownumber, row_data in enumerate(self.data):
                for column_number, datan in enumerate(row_data):
                    self.tableWidget.setItem(rownumber, column_number, QtWidgets.QTableWidgetItem(str(datan)))

    def guncelle(self):
        self.isim_soyisim = self.lineEdit_2.text()
        self.adres = self.textEdit.toPlainText()
        self.numara = self.lineEdit_3.text()
        self.urun = self.lineEdit_4.text()

        sorgu = "Select *From müsteriler where siparis_no"

        self.cursor.execute(sorgu, (self.ur))

        data = self.cursor.fetchall()

        print(data)

        self.close()


class musteriAra(QtWidgets.QDialog,musteriAra.Ui_Dialog):
    def __init__(self,parent = None):
        super(musteriAra,self).__init__()
        self.setupUi(self)

        self.baglanti()
    def baglanti(self):
        self.con = sqlite3.connect("otomasyon.db")
        self.cursor = self.con.cursor()
    def musteriAra(self):
        self.con = sqlite3.connect("otomasyon.db")
        self.cursor = self.con.cursor()
        ur = self.lineEdit_2.text()
        sorgu = "Select *From müsteriler where siparis_no = ?"
        self.cursor.execute(sorgu,(ur,))

        data = self.cursor.fetchall()


        if(len(data) == 0):
            print("Ürün bulunamadı.")

        else:
            for rownumber, row_data in enumerate(data):
                for column_number, datan in enumerate(row_data):
                    self.tableWidget.setItem(rownumber, column_number, QtWidgets.QTableWidgetItem(str(datan)))




class musteriekle(QtWidgets.QDialog,musteriekle.Ui_Dialog):
    def __init__(self,parent = None):
        super(musteriekle,self).__init__()
        self.setupUi(self)
        self.baglanti()

    def baglanti(self):
        self.con =  sqlite3.connect("otomasyon.db")

        self.cursor = self.con.cursor()
    def btnmusteriEkle(self):
        self.isim_soyisim = self.lineEdit.text()
        self.adres = self.textEdit.toPlainText()
        self.numara = self.lineEdit_3.text()
        self.urun = self.lineEdit_4.text()
        self.siparis_no = self.lineEdit_5.text()

        sorgu = "Insert into müsteriler values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(self.siparis_no,self.isim_soyisim,self.numara,self.adres,self.urun))
        self.lineEdit.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.textEdit.clear()
        self.close()

        self.con.commit()
    def btngeridon(self):
        pass
if __name__ == '__main__':
    app  = QtWidgets.QApplication(sys.argv)
    main = login()
    main.show()
    sys.exit(app.exec())
