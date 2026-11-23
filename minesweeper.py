import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import *
from Cell import CellBtn


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper")
        self.resize(700, 700)
        self.setMaximumSize(700, 700)

        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("green"))
        self.setPalette(paleta)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        self.diseno_principal = QVBoxLayout(widget_central)
        self.cuadricula = QGridLayout()

        # 1. Inicializar correctamente una matriz 10x10 con valores None
        self.tablero = [[None for _ in range(10)] for _ in range(10)]

        # 2. Crear todos los botones y añadirlos a la cuadrícula y la lista
        for fila in range(10):
            for columna in range(10):
                boton = CellBtn(fila, columna)
                boton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                boton.clicked.connect(self.onBtnLeftClick)

                boton.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                boton.customContextMenuRequested.connect(self.onBtnRightClick)

                self.cuadricula.addWidget(boton, fila, columna)
                self.tablero[fila][columna] = boton

        # 3. Compartir la referencia de la cuadrícula cuando estén creados todos los botones
        for fila in range(10):
            for columna in range(10):
                self.tablero[fila][columna].initLocalList(self.tablero)

        # 4. Calcular las bombas cercanas después de enlazar todas las celdas
        for fila in range(10):
            for columna in range(10):
                self.tablero[fila][columna].getCloseBombs()

        self.diseno_principal.addLayout(self.cuadricula)
        self.show()

    def revealAll(self):
        for fila in self.tablero:
            for columna in fila:
                columna.reveal()

    def onBtnLeftClick(self):
        boton = self.sender()
        if boton.tiene_bomba:
            self.revealAll()
        self.revealClose(boton.posicion_x, boton.posicion_y)

    def onBtnRightClick(self):
        boton = self.sender()
        if boton.text() == "⚑":
            boton.setText(" ")
        else:
            boton.setText("⚑")

    def revealClose(self, posicion_x, posicion_y):
        if not (0 <= posicion_x < len(self.tablero) and 0 <= posicion_y < len(self.tablero[0])):
            return

        casilla = self.tablero[posicion_x][posicion_y]
        if casilla is None or not casilla.isEnabled():
            return

        casilla.reveal()

        if casilla.numero == 0:
            for desplazamiento_x in (-1, 0, 1):
                for desplazamiento_y in (-1, 0, 1):
                    if desplazamiento_x == 0 and desplazamiento_y == 0:
                        continue
                    self.revealClose(posicion_x + desplazamiento_x, posicion_y + desplazamiento_y)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    aplicacion.exec()