from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from clases.triangulo import Triangulo

class DialogoTriangulo(QDialog):
    def __init__(self):
        super().__init__()
        # Carga la interfaz gráfica del triángulo
        uic.loadUi("ui/triangulo.ui", self)

        # Conectar el botón para realizar el cálculo
        self.btn_calcular.clicked.connect(self.procesarArea)

    def procesarArea(self):
        # 1. Capturar los datos de la interfaz y pasarlos a flotantes
        base_ingresada = float(self.txt_base.text())
        altura_ingresada = float(self.txt_altura.text())

        # 2. Instanciar nuestra clase lógica
        triangulo = Triangulo(base_ingresada, altura_ingresada)
        
        # 3. Obtener el texto del resultado matemático
        resultado_texto = triangulo.calcular_area()

        # 4. Mostrar el resultado en la etiqueta de la ventana
        self.lbl_resultado.setText(resultado_texto)