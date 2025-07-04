import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QVBoxLayout, QInputDialog, QWidget,
                               QLineEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self. setWindowTitle("My App")

        layout = QVBoxLayout()
        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_an_int)
        layout.addWidget(button1)


        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_a_float)
        layout.addWidget(button2)

        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_a_str_from_a_list)
        layout.addWidget(button3)

        button4 = QPushButton("String")
        button4.clicked.connect(self.get_a_str)
        layout.addWidget(button4)

        button5 = QPushButton("Text")
        button5.clicked.connect(self.get_text)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    #integer
    def get_an_int(self):
        title = "Enter an integer"
        label = "Type your integer here"

        # my_int_value, ok = QInputDialog.getInt(
               
        #             self, "Get an integer", "Enter a number"
        #             )
        # print("Result:", ok, my_int_value)

        my_int_value, ok = QInputDialog.getInt(
            self,
            title,
            label,
            value= 0,
            minValue=-5,
            maxValue= 5,
            step= 1,
        )
        
        print("Result:", ok, my_int_value)

    #floats
    def get_a_float(self):
        title = "Enter a float"
        label = "Type your float here"
        my_float_value, ok = QInputDialog.getDouble(
            self,
            title,
            label,
            value= 0,
            minValue=-5.3,
            maxValue= 5.7,
            step= 2,
        )
        print("Result:", ok, my_float_value)

    #select from a list of strings
    def get_a_str_from_a_list(self):
        title = "Select a string"
        label = "Select a fruit from the list"
        items = ["apple", "pear", "orange", "grape"]
        initial_selection =1 # orange, indexed from 0
        my_selected_str, ok = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            current=initial_selection,
            editable= False,
        )
        print("Result:", ok, my_selected_str)

    #single line of text
    def get_a_str(self):
        title = "Enter a string"
        label = "Type your password"
        text = "my secret password"
        mode = QLineEdit.Password
        my_selected_str, ok = QInputDialog.getText(
            self, title, label, mode, text
        )
        print("Result:", ok, my_selected_str)


    #Multi-line text
    def get_text(self):
        title = "Enter text"
        label = "Type your novel here"
        text = "Once upon a time..."
        
        my_selected_str, ok = QInputDialog.getMultiLineText(
            self, title, label, text
        )
        print("Result:", ok, my_selected_str)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
