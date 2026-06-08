class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        if self.base <= 0 or self.altura <= 0:
            return "¡Error! La base y la altura deben ser mayores a cero."
            
        area = (self.base * self.altura) / 2
        
        return f"--- Resultados del Triángulo ---\nBase: {self.base}\nAltura: {self.altura}\nÁrea total: {area:.2f}"