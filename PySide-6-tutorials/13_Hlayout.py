import sys

from PySide6.QtWidgets import (QApplication, 
                               QMainWindow,
                               QHBoxLayout,
                               QWidget
                               )

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #we create an vertical layout instance
        layout = QHBoxLayout()

        #we create 4 color widget instances and adds them
        #to the vertical layout
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(layout)

        #we set the entire widgets on the mainwindow
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
