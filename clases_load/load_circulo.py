from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.circulo import Circulo

class DialogoCirculo(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/circulo.ui", self)

        self.btn_calcular.clicked.connect(self.procesarCirculo)

    def procesarCirculo(self):
        radio_ingresado = float(self.txt_radio.text())

        circulo = Circulo(radio_ingresado)     
        resultado_texto = circulo.generar_reporte()
        self.lbl_resultado.setText(resultado_texto)