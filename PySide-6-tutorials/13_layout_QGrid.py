import sys

from PySide6.QtCore import Qt 
from PySide6.QtWidgets import (QApplication, 
                               QMainWindow,
                               QGridLayout,
                               QLabel,
                               QWidget
                               )

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #we create a grid layout instance
        layout = QGridLayout()

        # self.red =Color("red")
        # self.green =Color("green")
        # self.blue =Color("blue")
        # self.purple =Color("purple")
        
        #we create 3 color widget instances and adds them
        #to the grid layout
        layout.addWidget(Color("red"), 0,0 )
        layout.addWidget(Color("green") ,1,0)
        layout.addWidget(Color("blue"), 1,1)
        layout.addWidget(Color("purple"), 2,1)


        


        widget = QWidget()
        widget.setLayout(layout)

        #we set the entire widgets on the mainwindow
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
