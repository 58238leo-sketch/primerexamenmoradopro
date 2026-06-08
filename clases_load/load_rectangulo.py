from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.rectangulo import Rectangulo

class DialogoRectangulo(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/rectangulo.ui", self)

        self.btn_calcular.clicked.connect(self.procesarRectangulo)

    def procesarRectangulo(self):
        base_ingresada = float(self.txt_base.text())
        altura_ingresada = float(self.txt_altura.text())

        rectangulo = Rectangulo(base_ingresada, altura_ingresada)
        
        resultado_texto = rectangulo.generar_reporte()

        self.lbl_resultado.setText(resultado_texto)