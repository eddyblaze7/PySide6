import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLabel,
                               QLineEdit,
                                QPushButton,
                                QGridLayout,
                                QHBoxLayout,
                                QVBoxLayout,
                                QWidget
                                )

from qt_material import apply_stylesheet
from qt_material import list_themes
list_themes()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        apply_stylesheet(app, theme= 'dark_lightgreen.xml',
                          invert_secondary=True)

        self.setWindowTitle("My Widget Based Interface")
        self.setFixedHeight(200)
        self.setFixedWidth(300)

        self.label1 = QLabel("First Name :")
        self.label2 = QLabel("Last Name :")
        self.label3 = QLabel("Full Name : ")

        self.button1 = QPushButton("OK")
        self.button2 = QPushButton("Clear")

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()

        #layout = QGridLayout()``
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()

        layout2.addWidget(self.label1)
        layout2.addWidget(self.line1)
        layout1.addLayout(layout2)

        layout3.addWidget(self.label2)
        layout3.addWidget(self.line2)
        layout1.addLayout(layout3)

        layout1.addWidget(self.label3)

        layout4.addWidget(self.button1)
        layout4.addWidget(self.button2)
        layout1.addLayout(layout4)

        

        # layout.addWidget(self.label1,0,0)
        # layout.addWidget(self.line1,0,1)
        # layout.addWidget(self.label2,1,0)
        # layout.addWidget(self.line2,1,1)
        # layout.addWidget(self.label3,2,0)
        # layout.addWidget(self.button1,3,0)
        # layout.addWidget(self.button2,3,1)

        self.button1.clicked.connect(self.ok_button)
        self.button2.clicked.connect(self.clear_button)

        widget = QWidget()

        widget.setLayout(layout1)

        self.setCentralWidget(widget)

    def ok_button(self):
        textInput1= self.line1.text()
        textInput2= self.line2.text()
        #self.label3.setText(f"My Full Name is :"{self.line1.text()})
        self.label3.setText(f"Full Name : {textInput1} {textInput2}")

        #self.input.textChanged.connect(self.label.setText)

    def clear_button(self):
        self.line1.clear()
        self.line2.clear()



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
