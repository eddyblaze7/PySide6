import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                            QApplication,
                            QLabel,
                            QMainWindow,
                            QPushButton,
                            QTabWidget,
                            QWidget,
)
from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

            self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()