import sys
from typing import Optional
import PySide6.QtCore 
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        #adding specific file filters
        filters ="Portable Network Graphics files (*.png);;Comma Separated Values (*.csv);;All files (*)"
        print("Filters are:", filters)
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            filter = filters,
            )
        #this method returns - the filename and the current active file filter
        #in this case - the 'All File (*)'
        print("Result:", filename, selected_filter)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
