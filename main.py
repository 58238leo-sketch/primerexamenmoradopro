import sys
from PyQt5.QtWidgets import QApplication
from clases_load.menu_principal import VentanaPrincipal

def main():
    app = QApplication(sys.argv)
    dialogo = VentanaPrincipal()
    dialogo.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()