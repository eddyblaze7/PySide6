
import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QDialog, QDialogButtonBox, QVBoxLayout,
                               QLabel, QMessageBox)


#This is a subclass of the QDialog class- we call in the the QMainWindow
#class below, the parent:
class CustomDialog(QDialog):
    #we set a default value of None so we can omit the parent if we wish.
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hello")

        buttons =  QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        #we have to connnect the appropriate signal 'accepted' to the slots on the dialog
        #in this case, we've connected these signals from the QDialogButtonBox
        # to the handlesrs '.accept()'and '.reject()' on our subclass QDialog
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


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
        #that the dialog block interaction with the parent window.

        #we can now pass the main window in as a parameter, self
        #this centers the QDialogBox over the mainwindow
        dlg = CustomDialog(self)
        if dlg.exec():
            print("Success!")
        else:
            print("cancel")

    


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
