#VERSION 1 : Setting everything up in the global scope
#Everyting is in a single file 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

#this allows user to use command line 
app = QApplication(sys.argv)

#create the mainWindow instance
window = QMainWindow()

#set the title of the mainWindow
window.setWindowTitle("Our First MainWindow App")

#this creates the pushButton instance
button = QPushButton("Press Me!!")
#button.setText("Press Me!!")

#this command adds the button widget to the mainWindow
window.setCentralWidget(button)

#this command shows the window widget
window.show()
#this code start executing the event loop
app.exec()


