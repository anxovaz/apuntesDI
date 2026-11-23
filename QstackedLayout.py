import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout,
                             QPushButton, QWidget, QLabel, QStackedLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QStackedLayout sin lambdas")
        self.setMinimumSize(600, 400)

        # Widget central y diseño principal
        widget_central = QWidget()
        diseno_principal = QVBoxLayout(widget_central)

        # 1. Inicialización del QStackedLayout
        self.diseno_apilado = QStackedLayout()

        # --- PÁGINA 1 ---
        self.pagina1 = QWidget()
        diseno1 = QVBoxLayout(self.pagina1)
        self.etiqueta1 = QLabel("¡Estás en la Página 1!")
        self.boton_siguiente = QPushButton("Ir a la Página 2")

        # Conectamos el botón a un método normal
        self.boton_siguiente.clicked.connect(self.ir_a_pagina_2)

        diseno1.addWidget(self.etiqueta1)
        diseno1.addWidget(self.boton_siguiente)

        # --- PÁGINA 2 ---
        self.pagina2 = QWidget()
        diseno2 = QVBoxLayout(self.pagina2)
        self.etiqueta2 = QLabel("¡Estás en la Página 2!")
        self.boton_anterior = QPushButton("Volver a la Página 1")

        # Conectamos el botón a un método normal
        self.boton_anterior.clicked.connect(self.ir_a_pagina_1)

        diseno2.addWidget(self.etiqueta2)
        diseno2.addWidget(self.boton_anterior)

        # 2. Añadir las páginas al QStackedLayout
        self.diseno_apilado.addWidget(self.pagina1)  # Índice 0
        self.diseno_apilado.addWidget(self.pagina2)  # Índice 1

        # 3. Agregar el diseño apilado al diseño principal de la ventana
        diseno_principal.addLayout(self.diseno_apilado)

        self.setCentralWidget(widget_central)
        self.show()

    # Métodos tradicionales definidos en la clase
    def ir_a_pagina_1(self):
        self.diseno_apilado.setCurrentIndex(0)

    def ir_a_pagina_2(self):
        self.diseno_apilado.setCurrentIndex(1)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    aplicacion.exec()