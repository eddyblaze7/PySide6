from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
       
        self.label = QLabel()
        self.input = QLineEdit()
       

        #Note that to connect the input to the label, the input and label must both be
        #defined. so they are defined above
        self.input.textChanged.connect(self.label.setText)

        #This code adds the two widgets to a layout, 
        # and sets that on the window.
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()