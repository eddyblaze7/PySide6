import sys
from typing import Optional
from PySide6.QtCore import QSize  
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
                               QMainWindow,
                               QToolBar
                               )

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        #creating a menu bar instance
        menu_bar = self.menuBar()
        #adding a file menu to the menu bar
        file_menu = menu_bar.addMenu("&File")

        #creating an action under the file menu
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        #creating and adding actions to the edit menu
        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste") 
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("&Window")
        menu_bar.addMenu("&Setting")
        menu_bar.addMenu("&Help")

        #creating toolbar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #adding the 
        toolbar.addAction(quit_action)
        action1 = QAction("Some Action", self)
        action1.setStatusTip("status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        
       
        toolbar.addAction(action1)

        
        action2 = QAction(QIcon("start.png"), "Some  Other Action", self)
        action2.setStatusTip("status message for some action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)




    def quit_app(self): 
        self.app.quit()

    def toolbar_button_click(self): 
        print("action1 triggered")


 