# Form implementation generated from reading ui file 'C:\Users\Guilherme\PycharmProjects\Urna_Eletronica_CEIT/tela_inicial.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(866, 600)
        font = QtGui.QFont()
        font.setPointSize(8)
        Dialog.setFont(font)
        self.titulo = QtWidgets.QLabel(Dialog)
        self.titulo.setGeometry(QtCore.QRect(290, 30, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 220, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input = QtWidgets.QLineEdit(Dialog)
        self.input.setGeometry(QtCore.QRect(290, 300, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.input.setFont(font)
        self.input.setText("")
        self.input.setMaxLength(12)
        self.input.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.input.setObjectName("input")
        self.btn = QtWidgets.QPushButton(Dialog)
        self.btn.setGeometry(QtCore.QRect(290, 390, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(10, 0, 230, 230))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:\\Users\\Guilherme\\PycharmProjects\\Urna_Eletronica_CEIT\\../../OneDrive - UNIVALI/Imagens/Logo CEIT.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titulo.setText(_translate("Dialog", "ELEIÇÕES GRÊMIO ESTUDANTIL CEIT - 2022"))
        self.label.setText(_translate("Dialog", "Insira seu Token de aluno:"))
        self.btn.setText(_translate("Dialog", "Próximo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
