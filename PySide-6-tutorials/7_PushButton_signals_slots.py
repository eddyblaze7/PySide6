import sys

from PySide6.QtCore import QSize, Qt 
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton,
            )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #storing up data
        self.button_is_checked = True
        self.setWindowTitle("My App")

        button = QPushButton("Press Me !")
        button.setCheckable(True)

        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
