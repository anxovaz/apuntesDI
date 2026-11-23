import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QColor, QPalette


class ColorWidget(QWidget):
    """Un widget simple que muestra un color de fondo sólido."""

    def __init__(self, nombre_color):
        super().__init__()
        self.setAutoFillBackground(True)

        # Establecer el color
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(nombre_color))
        self.setPalette(paleta)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.setWindowTitle("box layout")
        self.resize(800, 600)

        # Widget central y diseño horizontal principal
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        diseno_horizontal = QHBoxLayout(widget_central)

        # Columna 1: Rojo, Amarillo, Morado
        diseno_columna1 = QVBoxLayout()
        diseno_columna1.addWidget(ColorWidget("red"))
        diseno_columna1.addWidget(ColorWidget("yellow"))
        diseno_columna1.addWidget(ColorWidget("purple"))
        diseno_horizontal.addLayout(diseno_columna1)

        # Columna 2: Un bloque Verde grande
        # Se añade el widget directamente al diseño horizontal para que ocupe toda la altura
        diseno_horizontal.addWidget(ColorWidget("green"))

        # Columna 3: Rojo, Morado
        diseno_columna3 = QVBoxLayout()
        diseno_columna3.addWidget(ColorWidget("red"))
        diseno_columna3.addWidget(ColorWidget("purple"))
        diseno_horizontal.addLayout(diseno_columna3)

        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(aplicacion.exec())