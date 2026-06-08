class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def generar_reporte(self):
        if self.base <= 0 or self.altura <= 0:
            return "¡Error! La base y la altura deben ser mayores a cero."
            
        area = self.base * self.altura
        perimetro = 2 * (self.base + self.altura)
        
        reporte = "--- Resultados del Rectángulo ---\n"
        reporte += f"Base: {self.base}\n"
        reporte += f"Altura: {self.altura}\n"
        reporte += f"Área total: {area:.2f}\n"
        reporte += f"Perímetro: {perimetro:.2f}"
        
        return reporte