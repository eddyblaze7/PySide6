import os
import sys

from PySide6.QtGui import QAction, QIcon, QKeySequence
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

        #the 'Qt' namespace has a lot of attributes to customise
        #widgets.
        label.setAlignment(Qt.AlignCenter)
 
        #set the central widget of the Window. widget will expand
        #to take up all the space in the window by default
        self.setCentralWidget(label)

        #creating a toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #creating an action

        #button_action = QAction("Your button", self)

        button_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Your button", self,
        )
        
        button_action.setStatusTip("This is your button")

        #signal and slot
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        #the code below makes the button_action checkable
        #it returns the signal "click True" or "click False"
        button_action.setCheckable(True)

        button_action.setShortcut(QKeySequence("Ctrl+p"))

        #we add the actions to the toolbar using the 'addAction' method
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        #Add more actions to the toolbar
        button_action2 = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Your button2", self
        )
        button_action2.setStatusTip("This is your button2")
        button_action2.setShortcut(QKeySequence("Ctrl+p"))

        #signal and slot
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        #you can also add other widgets to the toolbar using the 'addWidget' method
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox(self))

        #to see the status of the action buttons, we need to set the 
        #status bar to the self(the main window)
        self.setStatusBar(QStatusBar(self))

        #creating the menu bar instance
        menu = self.menuBar()

        #adding different menus using the 'addMenu' method
        file_menu = menu.addMenu("&File")
        #we can add actions to the menu items on the menu bar
        file_menu.addAction(button_action)

        #adding separators
        file_menu.addSeparator()

        #creating submenus and adding actions to them
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)



    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()



