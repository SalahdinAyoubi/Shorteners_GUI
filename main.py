from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys
from os import path

import pyshorteners
import time
import threading


MAIN, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow , MAIN):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.label_5.setHidden(True)

        self.Handel_UI()
        self.handel_buttons()
   


    def Handel_UI(self):
        self.setWindowIcon(QIcon("Icons/logo.png"))
        self.setWindowTitle("Shorteners")
        self.setFixedSize(602, 366)
        self.setGeometry(300, 200, 602, 366)
        self.statusBar().showMessage(" Shorteners Version 0.001 ") 



    def handel_buttons(self):
        self.ButtonShort.clicked.connect(self.handel_shortener)
        self.ButtonBack.clicked.connect(self.handel_back)




    def handel_shortener(self):
        self.stackedWidget.setCurrentIndex(0)
        self.movie = QMovie("Icons/ch.gif")
        self.label_4.setMovie(self.movie)
        self.movie.start()

        url = self.lineEdit.text()
        self.git_links = threading.Thread(target=self.shortener_url , args=(url , ))
        self.git_links.start()




    def handel_back(self):
        self.stackedWidget.setCurrentIndex(1)
        self.label_5.setHidden(True)
        self.listWidget.clear()




    def shortener_url(self ,url_link):
        global List_Site 
        global List_Links
        List_Site = []  
        List_Links = []
        s = pyshorteners.Shortener()
    
        if url_link[0:8] == "https://" or url_link[0:7] == "http://":
            try:
                if self.checkBox.isChecked():
                    List_Links.append(s.tinyurl.short(url_link))
                    List_Site.append("TinyUrl")

            except:
                List_Links.append(" ERROR ...")
                List_Site.append("TinyUrl")
                

            try:
                if self.checkBox_2.isChecked():
                    List_Links.append(s.chilpit.short(url_link))
                    List_Site.append("Chilp.It")
            
            except:
                List_Links.append(" ERROR ...")
                List_Site.append("Chilp.It")

            try:
                if self.checkBox_3.isChecked():
                    List_Links.append(s.clckru.short(url_link))
                    List_Site.append("Clck.Ru")

            except:
                List_Links.append(" ERROR ...")
                List_Site.append("Clck.Ru")

            try:
                if  self.checkBox_4.isChecked():
                    List_Links.append(s.dagd.short(url_link))
                    List_Site.append("Da.Gd")

            except:
                List_Links.append(" ERROR ...")
                List_Site.append("Da.Gd")
                
        
        else:
            self.label_5.setHidden(False)
           

        if len(List_Site) != 0 :
            for site , link in zip(List_Site , List_Links):
                self.listWidget.addItem(QListWidgetItem( site+ " :              " + link))
                time.sleep(0.5)

        self.listWidget.itemClicked.connect(self.Clicked)

        logo = QPixmap("Icons/logo.png")
        self.label_4.setPixmap(logo)


    def Clicked(self,item):
        QMessageBox.about(self, "Shorteners", "You Copy : \n  "+item.text())
        clipboard = QApplication.clipboard()
        clipboard.setText(item.text().split(" :              " , 1)[1])



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__== "__main__":
    main()