# Projeto Urna CEIT
import sys

import tela_inicial
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6 import uic, QtWidgets

#
# INICIO
#
# Carrega Interface

# Cria Janela
tela_inicial = QtWidgets.QDialog()

# Cria inter
ui_tela_inicial = tela_inicial.Ui_tela_inicial()

# Chama o Método de "inflar" a interface
ui_tela_inicial.setupUi(tela_inicial)

# Exibe Janela
tela_inicial.show()