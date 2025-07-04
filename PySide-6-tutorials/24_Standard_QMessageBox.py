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

    # using the following static method of declaring parameters for the QMessageBox
    #QMessageBox.question(parent, title, message)
    #QMessageBox.critical(parent, title, message)
    #QMessageBox.information(parent, title, message)
    #QMessageBox.warning(parent, title, message)
    def button_clicked(self, s):
        button = QMessageBox.question(
            self,"Question dialog", "The longer message"

        )
        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()