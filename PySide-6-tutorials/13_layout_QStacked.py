import sys

from PySide6.QtCore import Qt 
from PySide6.QtWidgets import (QApplication, 
                               QMainWindow,
                               QStackedLayout,
                               QLabel,
                               QWidget
                               )

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #we create a grid layout instance
        layout = QStackedLayout()

        
        
        #we create 4 color widget instances and adds them
        #to the grid layout
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))


        layout.setCurrentIndex(2)


        widget = QWidget()
        widget.setLayout(layout)

        #we set the entire widgets on the mainwindow
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
