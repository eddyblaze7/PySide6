import sys
from random import randint

from typing import Optional
import PySide6.QtCore 
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
)

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it will appear
    as a free-floating window.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w= AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def toggle_window(self, checked):
            #the '.isVisible()' and '.hide()' aids us to 
            #toggle the widget window instance between showing and hiding
            if self.w.isVisible():
                self.w.hide()

            else:
                self.w.show()

app = QApplication(sys.argv)
y=MainWindow()
y.show()
app.exec()
