import sys
import platform
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt6.uic.properties import QtGui, QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('UI\\urnav2.ui', self)
        self.btn_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tela2))  # Para tela de voto
        self.btn_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tela3))  # Para tela de confirmação
        self.btn_cancelar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tela2))  # Para tela de voto novamente (cancelar)
        self.btn_votar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tela4))  # Para final
        self.btn_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.tela1)) #  Para finalizar (voltar para tela de login)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
