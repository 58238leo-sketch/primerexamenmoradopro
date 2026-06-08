import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def generar_reporte(self):
        if self.radio <= 0:
            return "¡Error! El radio debe ser mayor a cero."
            
        area = math.pi * (self.radio ** 2)
        perimetro = 2 * math.pi * self.radio
        
        reporte = "--- Resultados del Círculo ---\n"
        reporte += f"Radio ingresado: {self.radio}\n"
        reporte += f"Área total: {area:.2f}\n"
        reporte += f"Perímetro: {perimetro:.2f}"
        
        return reporte