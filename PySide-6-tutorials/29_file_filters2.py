import sys
from typing import Optional
import PySide6.QtCore 
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)

# creating a list of file filters
FILE_FILTERS = [
    "Portable Network Graphics files (*.png)",
    "Text files (*.txt)",
    "Comma Separated values (*.csv)",
    "All files (*)",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        #adding specific file filters
        initial_filter = FILE_FILTERS[3] # selecting one from the list.

        #the below code joins the separate filter string to the list of filters
        #created earlier
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            filter = filters,
            #initialFilter=initial_filter, #unsupported key word 'initialFilter'
            )
        #this method returns - the filename and the current active file filter
        #in this case - the 'All File (*)'
        print("Result:", filename, selected_filter)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
