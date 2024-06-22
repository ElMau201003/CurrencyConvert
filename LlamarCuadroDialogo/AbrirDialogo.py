import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                             QMessageBox, QAction, QDialog, QVBoxLayout,
                             QFormLayout, QLineEdit, QPushButton, QDialogButtonBox, QDateEdit)
from PyQt5.QtCore import QDate


class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Entrada de Usuario')

        self.layout = QVBoxLayout(self)

        self.form_layout = QFormLayout()
        self.first_name_input = QLineEdit(self)
        self.last_name_input = QLineEdit(self)
        self.birth_date_input = QDateEdit(self)
        self.birth_date_input.setDisplayFormat('dd/MM/yyyy')
        self.birth_date_input.setCalendarPopup(True)
        self.phone_number_input = QLineEdit(self)

        self.form_layout.addRow('Nombre:', self.first_name_input)
        self.form_layout.addRow('Apellidos:', self.last_name_input)
        self.form_layout.addRow('Fecha de Nacimiento:', self.birth_date_input)
        self.form_layout.addRow('Número de Teléfono:', self.phone_number_input)

        self.layout.addLayout(self.form_layout)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

    def get_inputs(self):
        return {
            'first_name': self.first_name_input.text(),
            'last_name': self.last_name_input.text(),
            'birth_date': self.birth_date_input.date().toString('dd/MM/yyyy'),
            'phone_number': self.phone_number_input.text()
        }


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo Completo de QFileDialog.getOpenFileName')
        self.setGeometry(100, 100, 400, 300)

        # Crear la barra de menú
        menu_bar = self.menuBar()

        # Crear los menús
        file_menu = menu_bar.addMenu('Archivo')

        # Crear las acciones para el menú Archivo
        open_action = QAction('Abrir...', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)

        input_action = QAction('Entrada de Usuario...', self)
        input_action.setShortcut('Ctrl+I')
        input_action.triggered.connect(self.get_user_input)

        exit_action = QAction('Salir', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        # Añadir las acciones al menú Archivo
        file_menu.addAction(open_action)
        file_menu.addAction(input_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

    def open_file(self):
        # Parámetros del QFileDialog.getOpenFileName
        parent = self
        caption = "Abrir Archivo"
        directory = "/home"  # Cambia esto a un directorio válido en tu sistema
        filter = "Todos los Archivos (*);;Archivos de Texto (*.txt);;Imágenes (*.png *.jpg)"
        initialFilter = "Archivos de Texto (*.txt)"
        options = QFileDialog.Options()
        options |= QFileDialog.Option.ReadOnly  # Opcional: establece el cuadro de diálogo en modo de solo lectura

        # Abrir el cuadro de diálogo
        file_name, selected_filter = QFileDialog.getOpenFileName(parent, caption, directory, filter, initialFilter,
                                                                 options)

        # Manejo del archivo seleccionado
        if file_name:
            QMessageBox.information(self, "Archivo Abierto",
                                    f"Has abierto el archivo: {file_name}\nFiltro seleccionado: {selected_filter}")

    def get_user_input(self):
        dialog = InputDialog(self)
        if dialog.exec() == QDialog.Accepted:
            inputs = dialog.get_inputs()
            user_info = (f"Nombre: {inputs['first_name']} {inputs['last_name']}\n"
                         f"Fecha de Nacimiento: {inputs['birth_date']}\n"
                         f"Número de Teléfono: {inputs['phone_number']}")
            QMessageBox.information(self, 'Información de Usuario', user_info)

    def show_about(self):
        QMessageBox.about(self, "Acerca de", "Este es un ejemplo de menú en PyQt5.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
