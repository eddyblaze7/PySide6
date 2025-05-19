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

        self.button = QPushButton("Press Me !")
        self.button.setCheckable(True)

        #this released signal fires when the button is released
        #but does not send the check state
        self.button.clicked.connect(self.the_button_was_released)

        self.setCentralWidget(self.button)

    #we need to keep a reference to the 'button' on self so we can
    #access it in our slot
    def the_button_was_released(self):
        #the '.isChecked()' returns the check state of the button
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

