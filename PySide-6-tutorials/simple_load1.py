#using our UI in Python, we can either load it directly from Python
import os
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

basedir = os.path.dirname(__file__)
loader = QUiLoader()

def mainwindow_setup(w):
    w.setWindowTitle("MainWindow Title")

app = QtWidgets.QApplication(sys.argv)
window = loader.load(os.path.join(basedir, "simple.ui"), None)
mainwindow_setup(window)
window.show()
app.exec()