import sys
from PyQt6 import QtWidgets
from src.Cliente.ClienteSupermercado import Supermercado

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cliente = Supermercado()
    cliente.show()
    sys.exit(app.exec())



