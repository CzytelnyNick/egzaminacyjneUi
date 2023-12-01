from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel
from PyQt6 import QtCore, uic
from PyQt6.QtGui import QPixmap
import sys

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('zadanieEgzaminacyjne.ui', self)
        # self.ui.buttonLog.clicked.connect(self.autoryzacja)
        self.show()
        self.listImg = QPixmap('list.png')
        self.packImg = QPixmap('paczka.png')
        self.cardImg = QPixmap('pocztowka.png')
        self.imgLabel = QLabel(self)
        
        self.ui.listRadio.isChecked()
        # self.imgLabel.setPixmap()
        self.ui.images.addWidget(self.imgLabel)
        self.ui.checkButton.clicked.connect(self.check)
        self.price = QLabel()
        self.price.setStyleSheet("font-weight: bold; margin-bottom: 40px;  font-size: 16px")
        self.ui.images.addWidget(self.price)
        self.ui.submitButton.clicked.connect(self.submit)
    def check(self):
        if self.ui.listRadio.isChecked():
           self.imgLabel.setPixmap(self.listImg)
           self.price.setText("Cena: 1,5 zł")
        elif self.ui.pack.isChecked():
            self.imgLabel.setPixmap(self.packImg)
            self.price.setText("Cena: 10 zł")
        elif self.ui.card.isChecked():
            self.imgLabel.setPixmap(self.cardImg)
            self.price.setText("Cena: 1 zł")
    def submit(self):
        error = 0
        if len(self.ui.postCode.text()) < 5 or len(self.ui.postCode.text()) > 5:
            error = 1
            
        # try:
        #     int(self.ui.postCode)
        # except:
        #     error = 2
        if error == 0:
            QMessageBox.information(self, "Sukces", "Dane przesylki zostaly wprowadzone")
        elif error == 1:
            QMessageBox.warning(self, "BŁĄD", "Nieprawidlowa liczba cyfr w kodzie pocztowym")
        elif error == 2:
            QMessageBox.warning(self, "BŁĄD", "„Kod pocztowy powinien się składać z samych cyfr")

app = QApplication(sys.argv)
logowanie = Login()
sys.exit(app.exec())