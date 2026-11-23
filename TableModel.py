import sys

from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QTableView


class TableModel(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla

    def rowCount(self, indice):
        return len(self.tabla)

    def columnCount(self, indice):
        return len(self.tabla[0])

    def data(self, indice, rol):
        if indice.isValid():
            if rol == Qt.ItemDataRole.DisplayRole:
                if indice.row() == 0 or indice.column() != 4:
                    return self.tabla[indice.row()][indice.column()]
            if rol == Qt.ItemDataRole.CheckStateRole:
                if indice.row() != 0 and indice.column()==4:
                    if self.tabla[indice.row()][indice.column()]:
                        return Qt.CheckState.Checked
                    else:
                        return Qt.CheckState.Unchecked
            if rol == Qt.ItemDataRole.BackgroundRole:
                if indice.row() != 0:
                    datos = self.tabla[indice.row()][indice.column()]
                    if len(str(datos)) < 2:
                        return QColor("yellow")
                else:
                    return QColor("gray")

    def flags(self, indice):
        banderas = Qt.ItemFlag.ItemIsEnabled
        if indice.row() != 0 and indice.column() != 0:  # Se cambió de != 1 a != 0
            banderas = banderas | Qt.ItemFlag.ItemIsEditable
        if indice.row() != 0 and indice.column() == 4:
            banderas = banderas | Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEditable

        return banderas

    def setData(self, indice, valor, rol=Qt.ItemDataRole.EditRole):
        if indice.row() != 0:
            if rol == Qt.ItemDataRole.EditRole and indice.column() != 0:
                if valor != "":
                    self.tabla[indice.row()][indice.column()] = valor
                    self.dataChanged.emit(indice, indice, [rol])
                    return True
                return False
            if rol == Qt.ItemDataRole.CheckStateRole and indice.column() == 4:
                self.tabla[indice.row()][indice.column()] = valor
                self.dataChanged.emit(indice, indice, [rol])
                return True
        return False

'''
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.header[section]
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Table Example")
        self.resize(600, 300)

        # 1. Datos de ejemplo que se mostrarán
        datos = [
            ["ID","Name", "Age", "Role", "Active"],
            ["001","Bob", 30, "Designer", False],
            ["002","Charlie", 35, "Manager", True],
            ["003","Bob", 25, "Manager", True]
        ]

        # 2. Crear el modelo y la vista
        self.modelo = TableModel(datos)
        self.vista_tabla = QTableView()
        self.vista_tabla.setModel(self.modelo)

        # 3. Crear un diseño vertical y añadir la vista de tabla
        diseno = QVBoxLayout()
        diseno.addWidget(self.vista_tabla)

        # 4. Asignar el diseño a un widget central para QMainWindow
        contenedor = QWidget()
        contenedor.setLayout(diseno)
        self.setCentralWidget(contenedor)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(aplicacion.exec())