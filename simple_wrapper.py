#Another alternative is to create a WRAPPER CLASS and load the UI inside that. The
#main window itself is stored as 'self.ui' — you can safely hook signals from this to
#methods on your wrapper class.

import os
import sys
from typing import Optional

from PySide6 import QtCore, QtWidgets
import PySide6.QtCore
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
basedir = os.path.dirname(__file__)

class MainUI(QtCore.QObject): # Not a widget.
    def __init__(self):
        super().__init__()
        self.ui = loader.load(
            os.path.join(basedir, "simple.ui"), None
        )
        self.ui.setWindowTitle("MainWindow Title")
        self.ui.show()

app = QtWidgets.QApplication(sys.argv)
ui = MainUI()
app.exec()