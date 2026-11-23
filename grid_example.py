import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, \
    QGridLayout, QSizePolicy
from PyQt6.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Example")

        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)

        diseno_cuadricula = QGridLayout()
        boton = QPushButton("A")
        boton2 = QPushButton("B")
        boton3 = QPushButton("C")
        boton4 = QPushButton("D")
        boton5 = QPushButton("E")
        boton6 = QPushButton("F")
        boton6.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))  ## Para que se expanda

        diseno_cuadricula.addWidget(boton, 0,0)
        diseno_cuadricula.addWidget(boton2, 1, 0)
        diseno_cuadricula.addWidget(boton3, 2, 0)
        diseno_cuadricula.addWidget(boton4, 3, 0)
        diseno_cuadricula.addWidget(boton5, 4, 0)
        diseno_cuadricula.addWidget(boton6, 0, 1, 2, 1)

        widget_principal = QWidget()
        widget_principal.setLayout(diseno_cuadricula)
        self.setCentralWidget(widget_principal)

        self.show()


if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    aplicacion.exec()