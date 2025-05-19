import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QDialog)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self. setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)


    def button_clicked(self, s):
        print("click", s)
        #we create the dialog instance and pass our QMainWindow instance
        #as a parent- This makes a modal window of QMainWindow which means
        #that the dialog block interaction with the parent window
        dlg = QDialog(self)
        dlg.setWindowTitle("?")
        dlg.exec()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()