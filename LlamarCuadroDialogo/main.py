import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QMenuBar, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ejemplo de Menú en PyQt5')
        self.setGeometry(100, 100, 500, 300)

        # Crear la barra de menú
        menu_bar = self.menuBar()

        # Crear los menús
        file_menu = menu_bar.addMenu('Archivo')
        help_menu = menu_bar.addMenu('Ayuda')

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

        # Crear las acciones para el menú Ayuda
        about_action = QAction('Acerca de...', self)
        about_action.triggered.connect(self.show_about)

        # Añadir la acción al menú Ayuda
        help_menu.addAction(about_action)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   "Abrir Archivo",
                                                   "",
                                                   "Todos los Archivos (*);;Archivos de Texto (*.txt)",
                                                   options=options)
        if file_name:
            QMessageBox.information(self, "Archivo Abierto", f"Has abierto el archivo: {file_name}")

    def get_user_input(self):
        text, ok = QInputDialog.getText(self, 'Entrada de Usuario', 'Introduce tu nombre:')
        if ok and text:
            QMessageBox.information(self, 'Hola', f'Hola, {text}!')

    def show_about(self):
        QMessageBox.about(self, "Acerca de", "Este es un ejemplo de menú en PyQt5.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
