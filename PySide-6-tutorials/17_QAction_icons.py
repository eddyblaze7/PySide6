import os
import sys

from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import (
                            QApplication,
                            QLabel,
                            QMainWindow,
                            QToolBar,
                            QStatusBar,
                            QCheckBox,
                            
)

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        #creating a toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #creating an action

        #button_action = QAction("Your button", self)

        button_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "Your button", self,
        )
        
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        #the code below makes the button_action checkable
        #it returns the signal "click True" or "click False"
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        #Add more actions to the toolbar
        button_action2 = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "Your button2", self,
        )
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        #adding a label and a checkbox to the toolbar
        toolbar.addWidget(QLabel("Hello"))

        button_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "Your button", self,
        )

        toolbar.addSeparator()
        toolbar.addWidget(QCheckBox())

        toolbar.addSeparator()

        #This allow adds the status to the main window
        self.setStatusBar(QStatusBar(self))


    def onMyToolBarButtonClick(self, s):
            print("click", s)      

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

