from typing import Optional
from PySide6.QtWidgets import (QApplication, 
                               QLabel, 
                               QGridLayout,  
                               QWidget, 
                               QPushButton, 
                               QSlider,
                               QLineEdit,)
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet

import sys



class widget(QWidget):
   
    def __init__(self,):
        super().__init__()
        apply_stylesheet(app, theme='dark_cyan.xml')
        self.counter = 0

        self.setWindowTitle("Signals and Slots")

        self.button = QPushButton("Increment")
        self.button2= QPushButton("Decrement")
        self.label = QLabel("Counter: 0 ")
        #self.label2 = QLabel("Label Text 2 ")
        self.slider = QSlider(Qt.Horizontal)
        self.lineEdit = QLineEdit()

        
        grid = QGridLayout()

        grid.addWidget(self.button, 0,0)
        grid.addWidget(self.button2, 0,1)
        grid.addWidget(self.label, 0,2)
        grid.addWidget(self.slider, 1,0)
        grid.addWidget(self.lineEdit, 1,1)

        self.setLayout(grid)

        #connections- signals and slots
        self.button.clicked.connect(self.increase_counter)
        self.button2.clicked.connect(self.decrease_counter)
        self.slider.valueChanged.connect(self.slide_counter)
        
    def increase_counter(self):
        #self.counter =0 
        self.counter += 1
        self.label.setText(f"Counter: {self.counter}")
        #self.counter += 1


    def decrease_counter(self):
        #self.counter =0 
        self.counter -= 1
        self.label.setText(f"Counter: {self.counter}")
        #self.counter += 1

    def slide_counter(self,data):
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.counter = data
        self.label.setText(f"Counter: {self.counter}")
        self.lineEdit.setText(f" {data}")
        #self.counter += 1


app = QApplication(sys.argv)
window = widget()
window.show()

app.exec()





# def update_label():
#     global counter
#     counter += 1
#     label.setText(f"Counter: {counter}")

# # Create the application
# app = QApplication([])

# # Create the main window widget
# window = QWidget()

# # Create a vertical layout for the window
# layout = QVBoxLayout()
# window.setLayout(layout)

# # Create the label widget
# label = QLabel("Counter: 0")
# layout.addWidget(label)

# # Create a QTimer to update the label every second
# timer = QTimer()
# timer.timeout.connect(update_label)
# timer.start(1000)  # 1000 milliseconds = 1 second

# # Show the main window
# window.show()

# # Start the application event loop
# app.exec()