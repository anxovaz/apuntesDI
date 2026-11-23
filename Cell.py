import random
from PyQt6.QtWidgets import QPushButton


class CellBtn(QPushButton):
    def __init__(self, posicion_x, posicion_y):
        super().__init__()

        self.setText(" ")
        self.marcada = False
        self.numero = 0
        self.tiene_bomba = False
        self.tablero = []  # Se rellenará mediante initLocalList
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y

        if random.randint(0, 8) == 0:
            self.tiene_bomba = True

    def initLocalList(self, tablero):
        self.tablero = tablero

    def getCloseBombs(self):
        if self.tiene_bomba:
            self.numero = '*'
            return

        # Las ocho direcciones posibles
        direcciones = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for desplazamiento_x, desplazamiento_y in direcciones:
            nueva_x = self.posicion_x + desplazamiento_x
            nueva_y = self.posicion_y + desplazamiento_y

            if 0 <= nueva_x < len(self.tablero) and 0 <= nueva_y < len(self.tablero[0]):
                casilla = self.tablero[nueva_x][nueva_y]
                if casilla and casilla.tiene_bomba:
                    self.numero += 1

    def reveal(self):
        self.setDisabled(True)
        if self.numero == 0:
            self.setStyleSheet("background-color: gray")
        elif self.numero == 1:
            self.setStyleSheet("background-color: yellow")
        elif self.numero == 2:
            self.setStyleSheet("background-color: orange")
        elif self.numero == "*":
            self.setStyleSheet("background-color: black")
        else:
            self.setStyleSheet("background-color: red")

        if not self.numero == 0:
            self.setText(str(self.numero))