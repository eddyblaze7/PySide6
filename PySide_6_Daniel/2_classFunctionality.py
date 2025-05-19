#VERSION2 : Setting up a separate class
#Everything done here is in a class form so modules can be call
#from the main class
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#Subclass QMainWindow to customize your application's main window
class ButtonHolder(QMainWindow):
    def __init(self):
        super().__init__()

        self.setWindowTitle("Button Holder App")

        #this creates the pushButton instance 
        self.button = QPushButton("Press Me!!")
    

        #this command adds the button widget to the mainWindow
        self.setCentralWidget(self.button)

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
