import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QDialog, QDialogButtonBox, QVBoxLayout,
                               QLabel, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self. setWindowTitle("My App")
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg =QMessageBox(self)
        dlg.setWindowTitle("I have a queston !")
        dlg.setText("This is a question dialog")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        
        #here we call the 'exec()' method
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

