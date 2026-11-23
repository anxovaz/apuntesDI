# Guía de estudio: Python Qt (PyQt6 / PySide)

Resumen de arquitectura, diseños, widgets, eventos y modelo-vista para preparar el examen.

## Objetivo

Esta guía reúne los conceptos, estructuras de código, clases de widgets, gestores de diseño y patrones de arquitectura de los apuntes de Python Qt. Incluye ejemplos de interfaz, descripciones de objetos Qt y explicaciones de los ejercicios prácticos.

## Índice

1. [Arquitectura base y ciclo de vida](#1-arquitectura-base-y-ciclo-de-vida)
2. [Gestores de diseño](#2-gestores-de-diseño-layouts)
3. [Catálogo de objetos y widgets](#3-catálogo-de-objetos-y-widgets)
4. [Eventos, señales y slots](#4-eventos-señales-slots-y-menús-contextuales)
5. [Arquitectura modelo-vista](#5-arquitectura-modelo-vista)
6. [Proyectos y casos prácticos](#6-proyectos-y-casos-prácticos)
7. [Resumen rápido para el examen](#7-resumen-rápido-para-el-examen)

## 1. Arquitectura base y ciclo de vida

Una aplicación Qt en Python se apoya en tres componentes fundamentales:

- `QApplication` gestiona el bucle principal de eventos.
- `QMainWindow` proporciona una ventana con widget central y soporte para barras de estado y menús.
- `QWidget` es la clase base de los elementos gráficos.

Para iniciar una GUI, se crea `QApplication(sys.argv)`, se configura y muestra la ventana, y se cede el control al bucle de eventos mediante `app.exec()`.

Para personalizar los colores con `QPalette`, activa `setAutoFillBackground(True)` y asigna el color al rol `QPalette.ColorRole.Window`.

### Ejemplo: primera aplicación Qt

```python
import sys
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Demo")
        self.setMinimumSize(700, 520)

        # Configuración de la paleta (fondo negro)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("black"))
        self.setPalette(paleta)

        # Inicialización de los widgets
        self.etiqueta = QLabel("Insert your name:")
        self.campo_texto = QLineEdit()
        self.campo_texto.setPlaceholderText("Your Name")
        self.boton = QPushButton("Press me")
        self.boton.clicked.connect(self.al_pulsar_boton)
        self.campo_texto.returnPressed.connect(self.al_pulsar_boton)

        diseno_vertical = QVBoxLayout()
        widget_central = QWidget()
        widget_central.setLayout(diseno_vertical)
        diseno_vertical.addWidget(self.etiqueta)
        diseno_vertical.addWidget(self.campo_texto)
        diseno_vertical.addWidget(self.boton)
        self.setCentralWidget(widget_central)
        self.show()

    def al_pulsar_boton(self):
        if not self.campo_texto.text():
            self.etiqueta.setText("Please enter your name")
        else:
            self.etiqueta.setText("Hi " + str(self.campo_texto.text()))


aplicacion = QApplication(sys.argv)
ventana = MainWindow()
sys.exit(aplicacion.exec())
```

La interfaz del ejemplo organiza verticalmente sus controles y utiliza una paleta oscura.

## 2. Gestores de diseño (layouts)

Los layouts administran automáticamente la posición y el redimensionamiento de los widgets. En lugar de fijar posiciones en píxeles, Qt utiliza contenedores dinámicos:

- `QVBoxLayout`: organiza los widgets en una columna, de arriba abajo.
- `QHBoxLayout`: organiza los widgets en una fila, de izquierda a derecha.
- `QGridLayout`: distribuye elementos en filas y columnas; permite extender celdas con `rowSpan` y `colSpan`.
- `QStackedLayout`: mantiene varias páginas y muestra una cada vez mediante `setCurrentIndex(i)`.

Se pueden anidar layouts con `parent_layout.addLayout(child_layout)`. Un widget añadido directamente a un layout horizontal puede ocupar la altura disponible, como en el ejemplo de `box-layout.py`.

### Ejemplo: alternar páginas con QStackedLayout

```python
# Alternancia de páginas sin lambdas
diseno_apilado = QStackedLayout()

pagina1 = QWidget()
diseno1 = QVBoxLayout(pagina1)
diseno1.addWidget(QLabel("¡Estás en la Página 1!"))
boton_siguiente = QPushButton("Ir a la Página 2")
boton_siguiente.clicked.connect(self.ir_a_pagina_2)
diseno1.addWidget(boton_siguiente)

pagina2 = QWidget()
diseno2 = QVBoxLayout(pagina2)
diseno2.addWidget(QLabel("¡Estás en la Página 2!"))
boton_anterior = QPushButton("Volver a la Página 1")
boton_anterior.clicked.connect(self.ir_a_pagina_1)
diseno2.addWidget(boton_anterior)

diseno_apilado.addWidget(pagina1)
diseno_apilado.addWidget(pagina2)

def ir_a_pagina_1(self):
    self.diseno_apilado.setCurrentIndex(0)

def ir_a_pagina_2(self):
    self.diseno_apilado.setCurrentIndex(1)
```

El diseño apilado muestra la página activa indicada por su índice (0 o 1).

La ilustración del layout de cajas muestra un diseño horizontal con columnas verticales; la del `QStackedLayout` representa el cambio entre vistas según el índice activo.

## 3. Catálogo de objetos y widgets

| Objeto Qt | Categoría | Descripción y métodos principales |
|---|---|---|
| `QApplication` | Aplicación | Inicializa la aplicación con `sys.argv` y ejecuta el bucle de eventos con `exec()`. |
| `QMainWindow` | Ventana principal | Ventana de alto nivel; admite widget central (`setCentralWidget()`), título (`setWindowTitle()`) y límites de tamaño. |
| `QWidget` | Widget base | Elemento gráfico fundamental, contenedor o base para componentes personalizados. |
| `QLabel` | Visualización | Muestra texto o imágenes; se actualiza con `setText()` y se lee con `text()`. |
| `QLineEdit` | Entrada | Campo de texto de una línea; incluye `setPlaceholderText()`, `text()`, `setText()` y `returnPressed`. |
| `QPushButton` | Control | Botón que emite `clicked`; puede personalizarse con hojas de estilo o paletas. |
| `QComboBox` | Entrada | Menú desplegable; `addItems()` agrega opciones y `currentIndexChanged` notifica cambios. |
| `QRadioButton` | Entrada | Opción circular de selección exclusiva dentro de su grupo. |
| `QListView` | Vista modelo-vista | Muestra los datos de un modelo, por ejemplo `QAbstractListModel`, asignado con `setModel()`. |
| `QVBoxLayout` | Layout | Organiza widgets en columna con `addWidget()` y otros layouts con `addLayout()`. |
| `QHBoxLayout` | Layout | Organiza widgets en una fila horizontal. |
| `QGridLayout` | Layout | Organiza widgets en una cuadrícula; `addWidget(widget, fila, columna, rowSpan, colSpan)` ubica y extiende celdas. |
| `QStackedLayout` | Layout | Mantiene paneles apilados y muestra el índice seleccionado con `setCurrentIndex(int)`. |
| `QPalette` | Estilo | Configura colores por rol, como `ColorRole.Window`, texto y fondos. |
| `QColor` | Gráficos | Representa colores por nombre o valor RGB/HEX. |
| `QSizePolicy` | Layout | Define el redimensionamiento; `Expanding` permite ocupar el espacio disponible. |
| `QAbstractListModel` | Modelo | Modelo abstracto de lista; normalmente se implementan `rowCount()` y `data(index, role)`. |
| `QModelIndex` | Modelo | Referencia a un elemento; `row()` indica su fila. |
| `Qt.ItemDataRole` | Roles | Roles como `DisplayRole` (texto), `DecorationRole` (icono) y `BackgroundRole` (color). |

## 4. Eventos, señales, slots y menús contextuales

La comunicación entre la interfaz de Qt y la lógica de Python se basa en **señales y slots**. Una acción del usuario emite una señal que ejecuta la función o método conectado.

- **Identificar quién emite la señal:** dentro de un slot, `self.sender()` devuelve el widget que desencadenó el evento.
- **Detectar el clic derecho:** establece `Qt.ContextMenuPolicy.CustomContextMenu` con `setContextMenuPolicy()` y conecta `customContextMenuRequested` al método correspondiente.
- **Subclasificar un botón:** para un juego como Buscaminas, una subclase de `QPushButton` puede guardar atributos propios como bomba, fila, columna y número de bombas vecinas.

```python
class BotonCelda(QPushButton):
    def __init__(self, fila, columna):
        super().__init__()
        self.fila = fila
        self.columna = columna
        self.tiene_bomba = False
        self.numero = 0


boton = BotonCelda(fila, columna)
boton.clicked.connect(self.al_pulsar_boton_izquierdo)
boton.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
boton.customContextMenuRequested.connect(self.al_pulsar_boton_derecho)


def al_pulsar_boton_derecho(self):
    boton = self.sender()
    if boton.text() == "":
        boton.setText(" ")
    else:
        boton.setText("")
```

## 5. Arquitectura modelo-vista

Model-View separa la gestión de los datos de su representación gráfica. En los ejemplos, un `QListView` presenta un `QAbstractListModel` personalizado.

El método `data(index, role)` proporciona los datos según el rol solicitado:

- `Qt.ItemDataRole.DisplayRole`: texto de la lista.
- `Qt.ItemDataRole.DecorationRole`: imagen (`QImage`) usada como icono.
- `Qt.ItemDataRole.BackgroundRole`: color de fondo (`QColor`), por ejemplo rojo para tareas pendientes.

Para insertar o eliminar elementos, delimita las operaciones con `beginInsertRows()` / `endInsertRows()` y `beginRemoveRows()` / `endRemoveRows()`. Si cambia el contenido sin cambiar el tamaño de la lista, notifica el cambio con `dataChanged` o, cuando corresponda, con `layoutChanged`. Para reconstruir formularios dinámicos, se pueden retirar elementos con `layout.takeAt(0)` y liberar widgets con `widget.deleteLater()`.

### Ejemplo: modelo de tareas

```python
class ModeloTareas(QAbstractListModel):
    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas or []

    def data(self, indice, rol=Qt.ItemDataRole.DisplayRole):
        if not indice.isValid():
            return None

        esta_hecha, texto = self.tareas[indice.row()]
        if rol == Qt.ItemDataRole.DisplayRole:
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            return imagen_marca if esta_hecha else imagen_cruz
        if rol == Qt.ItemDataRole.BackgroundRole and not esta_hecha:
            return QColor("red")
        return None

    def rowCount(self, indice=QModelIndex()):
        return 0 if indice.isValid() else len(self.tareas)

    def addTask(self, texto):
        self.beginInsertRows(QModelIndex(), len(self.tareas), len(self.tareas))
        self.tareas.append((False, texto))
        self.endInsertRows()
```

## 6. Proyectos y casos prácticos

### Caso 1: calculadora

Combina `QVBoxLayout` para la pantalla y `QGridLayout` para los botones. El botón `=` puede ocupar dos columnas, por ejemplo `grid.addWidget(boton_igual, 3, 2, 1, 2)`. El botón de borrado `C` puede ocupar dos filas con `grid.addWidget(boton_borrar, 1, 3, 2, 1)`. La evaluación procesa primero multiplicación y división, y después suma y resta.

La ilustración correspondiente muestra la distribución de la calculadora y la expansión de sus botones dentro del `QGridLayout`.

### Caso 2: Buscaminas 10 × 10

Inicializa una matriz de 10 × 10 botones de celda. Una vez creada la cuadrícula, cada celda recibe la referencia al tablero mediante `initLocalList()` y calcula sus bombas vecinas con `getCloseBombs()`, comprobando las ocho direcciones:

```text
[(-1, -1), (-1, 0), (-1, 1), (0, -1),
 (0, 1), (1, -1), (1, 0), (1, 1)]
```

Al pulsar una celda vacía (cero bombas cercanas), `revealClose()` se invoca recursivamente para revelar las celdas adyacentes.

### Caso 3: panel escolar

Muestra formularios dinámicos. Al seleccionar un tipo en el `QComboBox` (estudiante, profesor o padre), `clearLayout()` vacía el contenedor dinámico y se crean los campos de texto específicos. La lista de tareas se presenta mediante el patrón modelo-vista.

La ilustración final representa el Buscaminas junto al panel escolar con su lista de tareas.

## 7. Resumen rápido para el examen

| Operación | Sintaxis | Punto clave |
|---|---|---|
| Iniciar la aplicación | `app = QApplication(sys.argv)`; `app.exec()` | No olvides ejecutar el bucle al final del script. |
| Asignar widget central | `self.setCentralWidget(widget)` | En `QMainWindow`, asigna el layout a un `QWidget` central. |
| Añadir widget a una cuadrícula | `grid.addWidget(widget, fila, columna, filas, columnas)` | El orden es fila y columna, no coordenadas x e y. |
| Identificar el emisor | `button = self.sender()` | Se usa dentro del slot conectado a la señal. |
| Detectar clic derecho | `setContextMenuPolicy(...)` y `customContextMenuRequested.connect(...)` | Configura primero `CustomContextMenu`. |
| Notificar una inserción | `beginInsertRows(QModelIndex(), inicio, fin)` y `endInsertRows()` | Sin estas llamadas, la vista no se actualiza correctamente. |
| Cambiar el estilo | `widget.setStyleSheet("background-color: red")` | Acepta sintaxis CSS para colores y propiedades. |
| Limpiar un layout | `elemento = layout.takeAt(0)`; `elemento.widget().deleteLater()` | Libera correctamente los widgets retirados. |
