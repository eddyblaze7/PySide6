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
    QLabel
)

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it will appear
    as a free-floating window.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = AnotherWindow()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        #this code simple displays the QWidget window instance 'w'
        #note that the window is created once-a persistent window 
        self.w.show()


app = QApplication(sys.argv)
y=MainWindow()
y.show()
app.exec()




