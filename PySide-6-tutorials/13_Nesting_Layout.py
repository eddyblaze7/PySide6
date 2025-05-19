import sys

from PySide6.QtWidgets import (QApplication, 
                               QMainWindow,
                               QVBoxLayout,
                               QHBoxLayout,
                               QWidget
                               )

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #we create an nesting layout instance
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        #we create 3 color widget instances and adds them
        #to the vertical layout(layout2)
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))

        #we are now adding the vertical layouts to the 
        #horizontal layout
        layout1.addLayout(layout2)

        #added one color widget to the horizontal layout(layout 1)
        layout1.addWidget(Color("green"))

        #created 2 color widget and then added them to the vertical
        #layout
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)
        
        #the code below create spacing around the main window 
        layout1.setContentsMargins(5,5,5,5)
        #the code below creates spacing between elements
        layout1.setSpacing(5)


        widget = QWidget()
        widget.setLayout(layout1)

        #we set the entire widgets on the mainwindow
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
