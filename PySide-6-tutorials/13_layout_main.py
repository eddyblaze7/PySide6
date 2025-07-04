import sys
from typing import Optional
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = Color("red")
        self.setCentralWidget(widget)

        
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()