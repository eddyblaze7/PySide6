import sys

from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
                            QApplication,
                            QLabel,
                            QMainWindow,
                            QPushButton,
                            QToolBar,
                            QStatusBar,
                            
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        #creating a toolbar
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        #creating an action
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        #the code below makes the button_action checkable
        #it returns the signal "click True" or "click False"
        button_action.setCheckable(True)

        toolbar.addAction(button_action)

        #This allow adds the status to the main window
        self.setStatusBar(QStatusBar(self))


    def onMyToolBarButtonClick(self, s):
            print("click", s)      

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

