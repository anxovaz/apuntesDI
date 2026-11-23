import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout,QPushButton,QHBoxLayout,QWidget, QLabel, QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Demo")
        self.setMinimumSize(700, 520)
        self.setMaximumSize(1100, 1000)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("black"))
        self.setPalette(paleta)

        # Inicialización de elementos
        self.campo_texto = QLineEdit()
        self.campo_texto.setPlaceholderText("Your Name")
        self.etiqueta = QLabel("Insert your name:")
        self.boton = QPushButton("Press me")

        # Eventos
        self.boton.clicked.connect(self.mainButtonClick)  # Conectar el botón con el método
        self.campo_texto.returnPressed.connect(self.mainButtonClick)

        # Diseño vertical
        diseno_vertical = QVBoxLayout()
        widget_diseno_vertical = QWidget()
        widget_diseno_vertical.setLayout(diseno_vertical)

        # Imprime el texto del botón

        # Añadir los elementos al diseño vertical
        diseno_vertical.addWidget(self.etiqueta)
        diseno_vertical.addWidget(self.campo_texto)
        diseno_vertical.addWidget(self.boton)
        self.setCentralWidget(widget_diseno_vertical)  # Establecer el diseño vertical como widget principal

        self.show()

    # Método que se ejecuta al pulsar el botón principal
    def mainButtonClick(self):
        if self.campo_texto.text() == "" or self.campo_texto.text() is None:
            self.etiqueta.setText("Please enter your name")
        else:
            self.etiqueta.setText("Hi " + str(self.campo_texto.text()))

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    aplicacion.exec()
