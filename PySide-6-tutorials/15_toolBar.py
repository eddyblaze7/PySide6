import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                            QApplication,
                            QLabel,
                            QMainWindow,
                            QPushButton,
                            QToolBar,
                            QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

   

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
