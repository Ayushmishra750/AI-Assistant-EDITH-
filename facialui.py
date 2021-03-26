from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 600)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(25, 90, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Audiowide")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.facialr = QtWidgets.QLabel(self.centralwidget)
        self.facialr.setGeometry(QtCore.QRect(0, 200, 499, 250))
        self.facialr.setObjectName("facialr")
        self.facialr_2 = QtWidgets.QLabel(self.centralwidget)
        self.facialr_2.setEnabled(True)
        self.facialr_2.setGeometry(QtCore.QRect(-70, 0, 600, 610))
        self.facialr_2.setAutoFillBackground(False)
        self.facialr_2.setText("")
        self.facialr_2.setPixmap(QtGui.QPixmap("extra_image/back.png"))
        self.facialr_2.setScaledContents(False)
        self.facialr_2.setIndent(-1)
        self.facialr_2.setObjectName("facialr_2")
        self.facialr_2.raise_()
        self.l1.raise_()
        self.facialr.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E.D.I.T.H Voice Assitant"))
        self.l1.setText(_translate("MainWindow", "E.D.I.T.H Facial Recognition"))
        self.facialr.setText(_translate("MainWindow", "TextLabel"))
        
        self.movie = QMovie("extra_image/facialmain.gif")
        self.facialr.setMovie(self.movie)
        self.movie.start()

        # QtCore.QTimer.singleShot(3000, self.exec_())
        # time.sleep(3)
        # print("ok")
        # self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



# # importing the required libraries 
  
# from PyQt5.QtWidgets import * 
# from PyQt5 import QtCore 
# from PyQt5 import QtGui 
# import sys 
# import time 
  
  
# class Window(QMainWindow): 
#     def __init__(self): 
#         super().__init__() 
  
#         # set the title 
#         self.setWindowTitle("Close") 
  
#         # setting  the geometry of window 
#         self.setGeometry(0, 0, 400, 300) 
  
#         # creating a label widget 
#         self.label = QLabel("Icon is set", self) 
  
#         # moving position 
#         self.label.move(100, 100) 
  
#         # setting up border 
#         self.label.setStyleSheet("border: 1px solid black;") 
  
#         # show all the widgets 
#         self.show() 
  
#         # waiting for 2 second 
#         time.sleep(2) 
  
#         # closing the window 
#         self.close() 
  
# # create pyqt5 app 
# App = QApplication(sys.argv) 
  
# # create the instance of our Window 
# window = Window() 
  
# # start the app 
# sys.exit(App.exec()) 