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

    def get_an_int(self):
        #here we create the instance of the QInputDialog Class
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter an integer")
        dialog.setLabelText("Type your integer here")
        dialog.setIntValue(0)
        dialog.setIntMinimum(-5)
        dialog.setIntMaximum(5)
        dialog.setIntStep(1)

        ok = dialog.exec()
        print("Result:", ok, dialog.intValue())


    def get_a_float(self):
        #here we create the instance of the QInputDialog Class
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a float")
        dialog.setLabelText("Type your float here")
        dialog.setDoubleValue(0.1)
        dialog.setDoubleMinimum(-5.3)
        dialog.setDoubleMaximum(5.7)
        dialog.setDoubleDecimals(2)

        ok = dialog.exec()
        print("Result:", ok, dialog.doubleValue())

    def get_a_str_from_a_list(self):
        #here we create the instance of the QInputDialog Class
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Select a string")
        dialog.setLabelText("Select a fruit from the list")
        dialog.setDoubleValue(0.1)
        dialog.setComboBoxItems(["apple", "pear", "orange", "grape"])
        dialog.setComboBoxEditable(False)
        dialog.setTextValue("orange")

        ok = dialog.exec()
        print("Result:", ok, dialog.textValue())

    def get_a_str(self):
        #here we create the instance of the QInputDialog Class
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter a string")
        dialog.setLabelText("Type your password")
        dialog.setTextValue("my secret password")
        dialog.setTextEchoMode(QLineEdit.Password)
        
        ok = dialog.exec()
        print("Result:", ok, dialog.textValue())

    def get_text(self):
        #here we create the instance of the QInputDialog Class
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Enter text")
        dialog.setLabelText("Type your novel here")
        dialog.setTextValue("Once upon a time...")
        dialog.setOption(
            QInputDialog.UsePlainTextEditForTextInput, True,
        )
        dialog.setDoubleMaximum(5.7)
        dialog.setDoubleDecimals(2)

        ok = dialog.exec()
        print("Result:", ok, dialog.textValue())


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

