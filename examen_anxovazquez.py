import sys

import PyQt6
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QComboBox, QHBoxLayout, QLabel, QCheckBox, \
    QLineEdit, QGridLayout, QRadioButton, QStackedLayout, QTextEdit, QPushButton, QDial


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen Anxo Vázquez")
        self.setMinimumSize(250, 400)
        self.setMaximumSize(800, 900)
        self.widget_principal = QWidget()
        self.setCentralWidget(self.widget_principal)
        self.diseno_principal = QVBoxLayout()
        self.widget_principal.setLayout(self.diseno_principal)

        # Selector que permite cambiar de zona
        self.selector_zonas = QComboBox()
        self.selector_zonas.addItems(("Configuración zoa 1", "Zoa 2", "Consola"))
        self.selector_zonas.currentIndexChanged.connect(self.comboboxEvento)
        self.diseno_principal.addWidget(self.selector_zonas)

        self.diseno_apilado = QStackedLayout()
        self.diseno_principal.addLayout(self.diseno_apilado)

        # -- ZONA 1 --

        # Cuadrícula
        # Inicialización
        self.widget_zona1 = QWidget()
        self.diseno_zona1 = QVBoxLayout()
        self.widget_zona1.setLayout(self.diseno_zona1)

        # Controles
        self.diseno_cuadricula = QGridLayout()
        self.diseno_cuadricula.addWidget(QLabel("Zoa activa"), 0, 0)
        self.casilla_activa = QCheckBox()
        self.casilla_activa.setChecked(True)
        self.casilla_activa.clicked.connect(self.activaBtn)
        self.diseno_cuadricula.addWidget(self.casilla_activa, 0, 1)
        self.diseno_cuadricula.addWidget(QLabel("Opcións"), 0, 2)

        self.diseno_cuadricula.addWidget(QLabel("Hora de comezo de rego"), 1, 0)
        self.campo_hora = QLineEdit()
        self.campo_hora.returnPressed.connect(self.horaEvento)
        self.diseno_cuadricula.addWidget(self.campo_hora, 1, 1)
        self.opcion_diaria = QRadioButton()
        self.opcion_diaria.setText("Diario")
        self.opcion_diaria.setChecked(True)
        self.diseno_cuadricula.addWidget(self.opcion_diaria, 1, 2)

        self.diseno_cuadricula.addWidget(QLabel("Duración rego"), 3, 0)
        self.etiqueta_dial = QLabel("")
        self.diseno_cuadricula.addWidget(self.etiqueta_dial, 3, 1)
        self.dial = QDial()
        self.dial.valueChanged.connect(self.dialEvent)
        self.diseno_cuadricula.addWidget(self.dial,2, 1, 2,1)
        self.opcion_semanal= QRadioButton()
        self.opcion_semanal.setText("Semanal")
        self.diseno_cuadricula.addWidget(self.opcion_semanal, 2, 2)

        self.casilla_antilluvia = QCheckBox()
        self.casilla_antilluvia.setText("Antixiada")
        self.diseno_cuadricula.addWidget(self.casilla_antilluvia, 3, 2)

        self.casilla_lluvia= QCheckBox()
        self.casilla_lluvia.setText("Chuvia")
        self.diseno_cuadricula.addWidget(self.casilla_lluvia, 4, 2)
        self.diseno_zona1.addLayout(self.diseno_cuadricula)



        # Sección de días
        self.diseno_dias = QHBoxLayout()
        self.lunes = QCheckBox()
        self.lunes.setText("Luns")
        self.diseno_dias.addWidget(self.lunes)
        self.martes = QCheckBox()
        self.martes.setText("Martes")
        self.diseno_dias.addWidget(self.martes)
        self.miercoles = QCheckBox()
        self.miercoles.setText("Mércores")
        self.diseno_dias.addWidget(self.miercoles)
        self.jueves = QCheckBox()
        self.jueves.setText("Xoves")
        self.diseno_dias.addWidget(self.jueves)
        self.viernes = QCheckBox()
        self.viernes.setText("Veres")
        self.diseno_dias.addWidget(self.viernes)
        self.sabado = QCheckBox()
        self.sabado.setText("Sabado")
        self.diseno_dias.addWidget(self.sabado)
        self.domingo = QCheckBox()
        self.domingo.setText("Domingo")
        self.diseno_dias.addWidget(self.domingo)

        self.diseno_zona1.addLayout(self.diseno_dias)

        # Botón de aceptar
        self.boton_aceptar = QPushButton("Aceptar")
        self.boton_aceptar.clicked.connect(self.aceptar)
        self.diseno_zona1.addWidget(self.boton_aceptar)

        # Índices del diseño apilado
        self.diseno_apilado.addWidget(self.widget_zona1)
        self.diseno_apilado.addWidget(QLabel("Está e a zoa 2"))
        self.consola = QTextEdit()
        self.diseno_apilado.addWidget(self.consola)


        self.show()

    def dialEvent(self):
        self.etiqueta_dial.setText(str(self.dial.value()))

    # Al pulsar Intro en el campo de hora, comprueba el formato (NN:NN)
    def horaEvento(self):
        texto = self.campo_hora.text()
        try:
            partes_texto = texto.split(":")

            if not partes_texto[0].isnumeric() or not partes_texto[1].isnumeric():
                self.consola.append("Erro, formato incorrecto")
                return False
            if int(partes_texto[0]) >= 24 or int(partes_texto[1]) < 0:
                self.consola.append("Erro, formato incorrecto")
                return False
            if int(partes_texto[1]) >= 60 or int(partes_texto[1]) < 0:
                self.consola.append("Erro, formato incorrecto")
                return False
        except IndexError:
            self.consola.append("Erro, formato incorrecto")
            return False

        if len(texto) !=5:
            self.consola.append("Erro, formato incorrecto")
            return False


        if not texto[2] == ":":
            self.consola.append("Erro, formato incorrecto")
            return False

        self.consola.append("Formato correcto")
        return True

    # Activa o desactiva los controles según el estado de la zona
    def activaBtn(self):
        if not self.casilla_activa.isChecked():
            self.campo_hora.setDisabled(True)
            self.casilla_lluvia.setDisabled(True)
            self.casilla_antilluvia.setDisabled(True)
            self.opcion_semanal.setDisabled(True)
            self.opcion_diaria.setDisabled(True)
            self.lunes.setDisabled(True)
            self.martes.setDisabled(True)
            self.miercoles.setDisabled(True)
            self.jueves.setDisabled(True)
            self.viernes.setDisabled(True)
            self.sabado.setDisabled(True)
            self.domingo.setDisabled(True)
            self.boton_aceptar.setDisabled(True)
            self.dial.setDisabled(True)
        else:
            self.campo_hora.setDisabled(False)
            self.casilla_lluvia.setDisabled(False)
            self.casilla_antilluvia.setDisabled(False)
            self.opcion_semanal.setDisabled(False)
            self.opcion_diaria.setDisabled(False)
            self.lunes.setDisabled(False)
            self.martes.setDisabled(False)
            self.miercoles.setDisabled(False)
            self.jueves.setDisabled(False)
            self.viernes.setDisabled(False)
            self.sabado.setDisabled(False)
            self.domingo.setDisabled(False)
            self.boton_aceptar.setDisabled(False)
            self.dial.setDisabled(False)


    # Evento que cambia el índice del QStackedLayout
    def comboboxEvento(self):
        if self.selector_zonas.currentIndex() == 0:
            self.diseno_apilado.setCurrentIndex(0)
        elif self.selector_zonas.currentIndex() == 1:
            self.diseno_apilado.setCurrentIndex(1)
        else:
            self.diseno_apilado.setCurrentIndex(2)


    # Botón de aceptar
    def aceptar(self):
        # Comprueba la hora antes de generar el informe y muestra un error si el formato no es válido
        if not self.horaEvento():
            self.consola.append("Para xenerar un informe a hora ten que ser correcta (NN:NN)")
            return

        informe = "---Novo Informe---"
        informe = informe + "\nNumero de zoa: 1"
        informe = informe + "\nHora de comezo: " + self.campo_hora.text()
        if self.opcion_semanal.isChecked():
            informe = informe + "\nTipo: Semanal"
        else:
            informe = informe + "\nTipo: Diario"
        if self.casilla_lluvia.isChecked():
            informe = informe + "\nChuvia: Si"
        else:
            informe = informe + "\nChuvia: Non"
        if self.casilla_antilluvia.isChecked():
            informe = informe + "\nAntixiada: Si"
        else:
            informe = informe + "\nAntixiada: Non"

        # Días
        if self.lunes.isChecked():
            informe = informe + "\nLuns: Si"
        if self.martes.isChecked():
            informe = informe + "\nMartes: Si"
        if self.miercoles.isChecked():
            informe = informe + "\nMércores: Si"
        if self.jueves.isChecked():
            informe = informe + "\nXoves: Si"
        if self.viernes.isChecked():
            informe = informe + "\nVenres: Si"
        if self.sabado.isChecked():
            informe = informe + "\nSábado: Si"
        if self.domingo.isChecked():
            informe = informe + "\nDomingo: Si"

        informe = informe + "\nDial: " + str(self.dial.value())

        self.consola.append(informe)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventana = Ventana()
    aplicacion.exec()