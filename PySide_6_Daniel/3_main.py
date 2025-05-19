#VERSION 3: Move the class into  a separate file
import sys
from PySide6.QtWidgets import QApplication
from buttonHolder import ButtonHolder 

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()