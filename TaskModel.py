from PyQt6.QtCore import Qt, QAbstractListModel, QModelIndex
from PyQt6.QtGui import QImage, QColor

marca = QImage("/home/anxo/2dam/DI/DI-Clase/img/tick.png")
cruz = QImage("/home/anxo/2dam/DI/DI-Clase/img/x.png")


class TaskModel(QAbstractListModel):
    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas or []

    def setTaskStatus(self, fila, esta_hecha):
        if 0 <= fila < len(self.tareas):
            _, texto = self.tareas[fila]
            self.tareas[fila] = (esta_hecha, texto)
            indice = self.index(fila)
            self.dataChanged.emit(indice, indice)

    def data(self, indice, rol=Qt.ItemDataRole.DisplayRole):
        if not indice.isValid():
            return None

        estado, texto = self.tareas[indice.row()]

        if rol == Qt.ItemDataRole.DisplayRole:
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            return marca if estado else cruz
        if rol == Qt.ItemDataRole.BackgroundRole:
            if not estado:
                return QColor("red")
        if rol == Qt.ItemDataRole.CheckStateRole:
            return Qt.CheckState.Checked if estado else Qt.CheckState.Unchecked

        return None

    def rowCount(self, indice=QModelIndex()):
        if indice.isValid():
            return 0
        return len(self.tareas)

    def addTask(self, texto):
        self.beginInsertRows(QModelIndex(), len(self.tareas), len(self.tareas))
        self.tareas.append((False, texto))  # Las tareas nuevas empiezan sin completar
        self.endInsertRows()

    def removeTask(self, fila):
        if 0 <= fila < len(self.tareas):
            self.beginRemoveRows(QModelIndex(), fila, fila)
            self.tareas.pop(fila)
            self.endRemoveRows()

    def flags(self, indice):
        if not indice.isValid():
            return Qt.ItemFlag.NoItemFlags
        return (
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
            | Qt.ItemFlag.ItemIsUserCheckable
            | Qt.ItemFlag.ItemIsEditable
        )

    def setData(self, indice, valor, rol=Qt.ItemDataRole.EditRole):
        if indice.isValid() and rol == Qt.ItemDataRole.CheckStateRole:
            _, texto = self.tareas[indice.row()]
            esta_marcada = (valor == Qt.CheckState.Checked.value)
            self.tareas[indice.row()] = (esta_marcada, texto)
            self.dataChanged.emit(indice, indice)
            return True
        elif indice.isValid() and rol == Qt.ItemDataRole.EditRole:
            esta_marcada, _ = self.tareas[indice.row()]
            self.tareas[indice.row()] = (esta_marcada, valor)
            self.dataChanged.emit(indice, indice)
            return True
        return False