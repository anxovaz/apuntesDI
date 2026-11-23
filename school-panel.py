import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLineEdit, QComboBox, QRadioButton, QLabel, QGridLayout, QListView, QPushButton,
                             QHBoxLayout)
from PyQt6.QtGui import QColor, QPalette
from TaskModel import TaskModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SCHOOL")
        self.resize(400, 600)
        self.setMaximumSize(400, 650)

        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("darkblue"))
        self.setPalette(paleta)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        self.diseno_principal = QVBoxLayout(widget_central)

        self.selector_tipo = QComboBox()
        self.selector_tipo.addItems(("Student", "Parent", "Teacher"))
        self.selector_tipo.setCurrentIndex(0)
        self.selector_tipo.currentIndexChanged.connect(self.handleCmbSignal)
        self.diseno_principal.addWidget(QLabel("Type:"))
        self.diseno_principal.addWidget(self.selector_tipo)

        self.selector_asignatura = QComboBox()
        self.selector_asignatura.addItems(("IT", "Math", "LAWS"))
        self.diseno_principal.addWidget(QLabel("Grade:"))
        self.diseno_principal.addWidget(self.selector_asignatura)

        self.diseno_datos = QVBoxLayout()
        self.diseno_principal.addLayout(self.diseno_datos)

        self.diseno_cursos = QGridLayout()
        for fila, curso in enumerate(("1st", "2nd", "3rd", "4th")):
            boton_opcion = QRadioButton(curso, self)
            boton_opcion.toggled.connect(self.toggle)
            self.diseno_cursos.addWidget(boton_opcion, fila, 1)

        self.diseno_principal.addWidget(QLabel("Year:"))
        self.diseno_principal.addLayout(self.diseno_cursos)

        # --- Sección de lista de tareas ---
        self.diseno_principal.addWidget(QLabel("Dumb Todo List:"))
        self.vista_tareas = QListView()
        self.modelo_tareas = TaskModel([
            (True, "Option 1"),
            (False, "Option 2"),
            (True, "Option 3")
        ])
        self.vista_tareas.setModel(self.modelo_tareas)
        self.diseno_principal.addWidget(self.vista_tareas)
        # Configuración adicional de la vista (pendiente)

        # Campo de tareas y diseño de botones
        diseno_entrada_tarea = QHBoxLayout()
        self.campo_nueva_tarea = QLineEdit()
        self.campo_nueva_tarea.setPlaceholderText("Enter new task...")
        diseno_entrada_tarea.addWidget(self.campo_nueva_tarea)

        self.boton_anadir = QPushButton("Add")
        self.boton_anadir.clicked.connect(self.addNewTask)
        diseno_entrada_tarea.addWidget(self.boton_anadir)

        self.boton_eliminar = QPushButton("Delete")
        self.boton_eliminar.clicked.connect(self.deleteSelectedTask)
        diseno_entrada_tarea.addWidget(self.boton_eliminar)

        self.boton_hecha = QPushButton("Done")
        self.boton_hecha.clicked.connect(self.done)
        diseno_entrada_tarea.addWidget(self.boton_hecha)

        self.boton_pendiente = QPushButton("UnDone")
        self.boton_pendiente.clicked.connect(self.done)
        diseno_entrada_tarea.addWidget(self.boton_pendiente)

        self.diseno_principal.addLayout(diseno_entrada_tarea)
        # -------------------------

        self.handleCmbSignal()
        self.show()

    def toggle(self, marcada):
        if marcada:
            print(self.sender().text())

    def done(self):
        boton = self.sender()
        indices = self.vista_tareas.selectedIndexes()
        if not indices:
            return

        fila = indices[0].row()
        esta_hecha = (boton.text() == "Done")
        self.modelo_tareas.setTaskStatus(fila, esta_hecha)



    def clearLayout(self, diseno):
        while diseno.count():
            elemento = diseno.takeAt(0)
            widget = elemento.widget()
            if widget is not None:
                widget.deleteLater()
            subdiseno = elemento.layout()
            if subdiseno is not None:
                self.clearLayout(subdiseno)

    def handleCmbSignal(self):
        self.clearLayout(self.diseno_datos)

        seleccion = self.selector_tipo.currentText()
        if seleccion == "Student":
            campo_alumno = QLineEdit()
            campo_alumno.setPlaceholderText("Student Name")
            self.diseno_datos.addWidget(campo_alumno)

            campo_padre = QLineEdit()
            campo_padre.setPlaceholderText("Father Name")
            self.diseno_datos.addWidget(campo_padre)

            campo_madre = QLineEdit()
            campo_madre.setPlaceholderText("Mother Name")
            self.diseno_datos.addWidget(campo_madre)

        elif seleccion == "Teacher":
            campo_profesor = QLineEdit()
            campo_profesor.setPlaceholderText("Teacher Name")
            self.diseno_datos.addWidget(campo_profesor)

            campo_hora_entrada = QLineEdit()
            campo_hora_entrada.setPlaceholderText("Entry Time")
            self.diseno_datos.addWidget(campo_hora_entrada)

            campo_hora_salida = QLineEdit()
            campo_hora_salida.setPlaceholderText("Leave time")
            self.diseno_datos.addWidget(campo_hora_salida)

        else:
            self.diseno_principal.addWidget(QLabel("Parent Info:"))
            campo_nombre_padre = QLineEdit()
            campo_nombre_padre.setPlaceholderText("Parent name")
            self.diseno_datos.addWidget(campo_nombre_padre)

    def addNewTask(self):
        texto = self.campo_nueva_tarea.text().strip()
        if texto:
            self.modelo_tareas.addTask(texto)
            self.campo_nueva_tarea.clear()

    def deleteSelectedTask(self):
        indices = self.vista_tareas.selectedIndexes()
        if not indices:
            return
        fila = indices[0].row()
        self.modelo_tareas.removeTask(fila)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    aplicacion.exec()