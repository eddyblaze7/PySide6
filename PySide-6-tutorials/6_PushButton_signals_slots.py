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
        self.setWindowTitle("My App")

        button = QPushButton("Press Me !")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        #set the central widget of the window
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    #this slot receives data on what has just happened with
    #the events taking place
    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
