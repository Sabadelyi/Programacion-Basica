import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QMessageBox

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora en PyQt5")
        self.setGeometry(100, 100, 350, 400)
        self.initUI()

    def initUI(self):
        # Crear el cuadro de entrada
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; height: 50px;")

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        layout = QVBoxLayout()
        layout.addWidget(self.display)

        grid_layout = QGridLayout()

        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                button = QPushButton(button_text, self)
                button.setStyleSheet("font-size: 20px; height: 60px;")
                button.clicked.connect(lambda _, text=button_text: self.on_button_click(text))
                grid_layout.addWidget(button, i, j)

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                QMessageBox.warning(self, "Error", "Expresión inválida.")
        elif button_text == "C":
            self.display.clear()
        else:
            self.display.setText(self.display.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CalculatorApp()
    ventana.show()
    sys.exit(app.exec_())