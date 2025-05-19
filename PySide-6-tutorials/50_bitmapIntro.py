import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen,QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()

        #create the pixmap object we'll draw onto
        self.canvas = QPixmap(400,300)

        #fill the entire canvas with white (so we cam see our line)
        self.canvas.fill(Qt.GlobalColor.gray)

        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter =QPainter(self.canvas)
        #draw a line from (10,10) to (300,200)
        painter.drawLine(10,10,300,200)
        painter.end()
        self.label.setPixmap(self.canvas)


app= QApplication(sys.argv)
window= MainWindow()
window.show()
app.exec()