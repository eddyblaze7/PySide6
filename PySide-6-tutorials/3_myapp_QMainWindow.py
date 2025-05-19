from PySide6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()

window.show() #Important- windows are hidden by default

#start the event loop

app.exec() 

#the QMainWindow must be structured well with other components to work well
