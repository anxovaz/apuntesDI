import sys

import PyQt6
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QLabel, QComboBox, QStackedLayout, \
    QGridLayout, QLineEdit, QPushButton, QHBoxLayout


class Pantalla(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lista_alumnos = [("Pepito","2ESO","20/09/2006"),("Menganito","1ESO","10/09/2007")]
        self.lista_padres = [("Juan", "Pepito","juan@correo.com"),("Jorge", "Menganito","jorge@correo.com")]
        self.setWindowTitle("Pantalla")
        self.setMinimumSize(800, 600)

        self.widget_central = QWidget()
        self.diseno_principal = QVBoxLayout(self.widget_central)
        self.setCentralWidget(self.widget_central)

        self.diseno_apilado = QStackedLayout()

        # Cuadro combinado
        self.etiqueta_tipo = QLabel("Tipo: ")
        self.diseno_principal.addWidget(self.etiqueta_tipo)
        self.selector_tipo = QComboBox()
        self.selector_tipo.currentIndexChanged.connect(self.cmbFun)
        self.selector_tipo.addItems(["alumno", "padre"])
        self.diseno_principal.addWidget(self.selector_tipo)

        self.show()


        # QStackedLayout
        self.diseno_principal.addLayout(self.diseno_apilado)

        # Página del alumno
        self.widget_alumno = QWidget()
        self.diseno_alumno = QGridLayout()
        self.widget_alumno.setLayout(self.diseno_alumno)

        self.diseno_alumno.addWidget(QLabel("Nombre"),0,0)
        self.campo_nombre_alumno = QLineEdit()
        self.diseno_alumno.addWidget(self.campo_nombre_alumno, 0, 1)

        self.diseno_alumno.addWidget(QLabel("Curso"), 1, 0)
        self.campo_curso = QLineEdit()
        self.diseno_alumno.addWidget(self.campo_curso, 1, 1)

        self.diseno_alumno.addWidget(QLabel("Nacimiento"), 2, 0)
        self.campo_nacimiento = QLineEdit()
        self.diseno_alumno.addWidget(self.campo_nacimiento, 2, 1)

        self.diseno_apilado.addWidget(self.widget_alumno)  # Índice = 0

        # Página del padre
        self.widget_padre = QWidget()
        self.diseno_padre = QGridLayout()
        self.widget_padre.setLayout(self.diseno_padre)

        self.diseno_padre.addWidget(QLabel("Nombre"),0,0)
        self.campo_nombre_padre = QLineEdit()
        self.diseno_padre.addWidget(self.campo_nombre_padre, 0, 1)

        self.diseno_padre.addWidget(QLabel("Hijo"), 1, 0)
        self.campo_hijo = QLineEdit()
        self.diseno_padre.addWidget(self.campo_hijo, 1, 1)

        self.diseno_padre.addWidget(QLabel("Correo"), 2, 0)
        self.campo_correo = QLineEdit()
        self.diseno_padre.addWidget(self.campo_correo, 2, 1)

        self.diseno_apilado.addWidget(self.widget_padre)  # Índice = 1


        self.diseno_apilado.setCurrentIndex(0)


        # Botones
        self.diseno_botones = QHBoxLayout()

        self.boton_buscar = QPushButton("Buscar")
        self.boton_agregar = QPushButton("Agregar")

        self.boton_agregar.clicked.connect(self.onClickAgregar)
        self.boton_buscar.clicked.connect(self.onClickBuscar)

        self.diseno_botones.addWidget(self.boton_buscar)
        self.diseno_botones.addWidget(self.boton_agregar)

        self.diseno_principal.addLayout(self.diseno_botones)

        self.etiqueta_resultado = QLabel("")
        self.diseno_principal.addWidget(self.etiqueta_resultado)

        self.show()

    def cmbFun(self):
        if self.selector_tipo.currentIndex() == 0:
            self.diseno_apilado.setCurrentIndex(0)
        else:
            self.diseno_apilado.setCurrentIndex(1)

    def onClickBuscar(self):
        if self.selector_tipo.currentIndex() == 0:  # Alumno
            for registro in self.lista_alumnos:
                if registro == (self.campo_nombre_alumno.text(), self.campo_curso.text(), self.campo_nacimiento.text()):
                    self.etiqueta_resultado.setText("Alumno encontrado")
                    return
            self.etiqueta_resultado.setText("Alumno no encontrado")
        else:  # Padre
            for registro in self.lista_padres:
                if registro == (self.campo_nombre_padre.text(), self.campo_hijo.text(), self.campo_correo.text()):
                    self.etiqueta_resultado.setText("Padre encontrado")
                    return
            self.etiqueta_resultado.setText("Padre no encontrado")
    def onClickAgregar(self):
        if self.selector_tipo.currentIndex() == 0:  # Alumno
            self.lista_alumnos.append((self.campo_nombre_alumno.text(), self.campo_curso.text(), self.campo_nacimiento.text()))
            print(self.lista_alumnos)
        else:  # Padre
            self.lista_padres.append((self.campo_nombre_padre.text(), self.campo_hijo.text(), self.campo_correo.text()))
            print(self.lista_padres)
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Pantalla()
    aplicacion.exec()
