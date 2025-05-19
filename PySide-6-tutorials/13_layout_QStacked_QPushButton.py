import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                            QApplication,
                            QHBoxLayout,
                            QLabel,
                            QMainWindow,
                            QPushButton,
                            QStackedLayout,
                            QVBoxLayout,
                            QWidget,
)
from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        
        #red button
        btn1 = QPushButton("red")
        btn1.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn1)
        self.stacklayout.addWidget(Color("red"))

        #green button
        btn2 = QPushButton("green")
        btn2.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn2)
        self.stacklayout.addWidget(Color("green"))

        #yellow button
        btn3 = QPushButton("yellow")
        btn3.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn3)
        self.stacklayout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

        
