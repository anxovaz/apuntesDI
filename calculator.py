import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, \
    QGridLayout, QLabel, QSizePolicy
from PyQt6.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.resize(200,280)
        self.setMaximumSize(190,270)

        # Color de fondo de la ventana principal
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("gray"))
        self.setPalette(paleta)

        # Widget central
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        diseno_principal = QVBoxLayout(widget_central)

        # Pantalla de la calculadora
        self.parte_superior = QVBoxLayout()

        self.pantalla = QLineEdit()
        self.pantalla.returnPressed.connect(self.calculate)
        self.pantalla.textEdited.connect(self.handle_text_edited)  # También se puede usar textChanged

        self.etiqueta = QLabel()
        self.etiqueta.setText("Operation")

        self.parte_superior.addWidget(self.etiqueta)
        self.parte_superior.addWidget(self.pantalla)
        diseno_principal.addLayout(self.parte_superior)

        ## Sección de botones
        cuadricula = QGridLayout()

        fila = 3
        contador = 0
        for indice in range(1, 10):
            boton = QPushButton(str(indice))
            boton.clicked.connect(self.activateButton)
            cuadricula.addWidget(boton, fila, contador)

            contador += 1
            if contador == 3:
                fila -= 1
                contador = 0


        boton0 = QPushButton("0")
        boton0.clicked.connect(self.activateButton)
        cuadricula.addWidget(boton0,3,0)

        boton_decimal = QPushButton(".")
        boton_decimal.clicked.connect(self.activateButton)
        cuadricula.addWidget(boton_decimal, 3, 1)

        boton_igual = QPushButton("=")
        boton_igual.clicked.connect(self.calculate)

        # Estilo del botón igual
        boton_igual.setAutoFillBackground(True)
        paleta_igual = boton_igual.palette()
        paleta_igual.setColor(QPalette.ColorRole.Window, QColor("orange"))
        boton_igual.setPalette(paleta_igual)
        # Añadir el botón igual
        cuadricula.addWidget(boton_igual, 3, 2, 1,2)

        boton_sumar = QPushButton("+")
        boton_sumar.clicked.connect(self.activateButton)
        cuadricula.addWidget(boton_sumar,0,0)

        boton_restar = QPushButton("-")
        boton_restar.clicked.connect(self.activateButton)
        cuadricula.addWidget(boton_restar, 0, 1)

        boton_multiplicar = QPushButton("*")
        boton_multiplicar.clicked.connect(self.activateButton)
        cuadricula.addWidget(boton_multiplicar, 0, 2)

        boton_dividir = QPushButton("/")
        boton_dividir.clicked.connect(self.activateButton)
        cuadricula.addWidget(boton_dividir, 0, 3)

        boton_borrar = QPushButton("C")
        boton_borrar.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        boton_borrar.clicked.connect(self.deleteBtn)
        cuadricula.addWidget(boton_borrar, 1, 3, 2 ,1)

        diseno_principal.addLayout(cuadricula)
        self.show()

    def handle_text_edited(self, texto):
        if "=" in texto:
            self.pantalla.setText(texto.replace("=", ""))  # calculate necesita la operación sin el «=» final
            self.calculate()

    def deleteBtn(self):
        contenido = self.pantalla.text()
        self.pantalla.setText(contenido[:-1])  # Elimina el último carácter
        self.pantalla.setFocus()

    def activateButton(self):
        boton = self.sender()
        if boton:
            if self.pantalla.text() != "0":
                caracter = boton.text()
                contenido = self.pantalla.text()
                self.pantalla.setText(contenido + caracter)
            else:
                if boton.text() != "0":
                    caracter = boton.text()
                    contenido = self.pantalla.text()
                    self.pantalla.setText(contenido + caracter)
        self.pantalla.setFocus()



    def calculate(self):
        try:
            operacion = self.pantalla.text()

            # Convertir la operación en una lista
            valores_operadores = []
            valor_actual = ""
            operadores = {"+", "-", "*", "/"}

            for indice in range(len(operacion)):
                caracter = operacion[indice]

                if caracter in operadores:
                    if len(valor_actual) != 0:
                        valores_operadores.append(valor_actual)
                        valores_operadores.append(caracter)
                        valor_actual = ""
                    else:  # Si es el primer número, puede ser negativo
                        valor_actual += caracter
                else:
                    valor_actual += caracter

                # Se comprueba si se ha llegado al final de la operación
                if indice == len(operacion) - 1 and valor_actual != "":
                    valores_operadores.append(valor_actual)

            # Multiplicación y división
            while True:
                encontrado = False
                for indice in range(len(valores_operadores)):
                    if valores_operadores[indice] in {"*", "/"}:
                        simbolo = valores_operadores[indice]
                        valor1 = float(valores_operadores[indice - 1])
                        valor2 = float(valores_operadores[indice + 1])

                        if simbolo == "*":
                            resultado = valor1 * valor2
                        else:
                            resultado = valor1 / valor2

                        valores_operadores[indice - 1] = resultado
                        del valores_operadores[indice: indice + 2]
                        encontrado = True
                        break

                if not encontrado:
                    break

            # Suma y resta
            while True:
                encontrado = False
                for indice in range(len(valores_operadores)):
                    if valores_operadores[indice] in {"+", "-"}:
                        simbolo = valores_operadores[indice]
                        valor1 = float(valores_operadores[indice - 1])
                        valor2 = float(valores_operadores[indice + 1])

                        if simbolo == "+":
                            resultado = valor1 + valor2
                        else:
                            resultado = valor1 - valor2

                        valores_operadores[indice - 1] = resultado
                        del valores_operadores[indice: indice + 2]
                        encontrado = True
                        break

                if not encontrado:
                    break

            if valores_operadores:
                self.pantalla.setText(str(valores_operadores[0]))
        except Exception:
            self.pantalla.setText("Syntax Error")


if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    aplicacion.exec()



