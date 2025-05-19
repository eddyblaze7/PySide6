from typing import Optional
import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from WWW import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()