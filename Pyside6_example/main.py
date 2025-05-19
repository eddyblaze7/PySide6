import sys
import os
from PySide6.QtWidgets import (QApplication, 
                               QMainWindow,
                                QLabel)

from PySide6.QtCore import Qt, QSize 
from PySide6.QtGui import QAction,QKeySequence, QIcon, QFont, Qt
from action import Action
from qt_material import apply_stylesheet




     




app = QApplication(sys.argv)

apply_stylesheet(app,theme='dark_lightgreen.xml')


window = Action()
window.show()

app.exec()
    

    