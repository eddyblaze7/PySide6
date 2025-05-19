import sys
import os
from typing import Optional
import PySide6.QtCore 
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
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
        layout = QVBoxLayout()

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)
        layout.addWidget(button1)
        
        

        button2 = QPushButton("Open files")
        button2.clicked.connect(self.get_filenames)
        layout.addWidget(button2)

        button3 = QPushButton("Save file")
        button3.clicked.connect(self.get_save_filename)
        layout.addWidget(button3)

        button4 = QPushButton("Select folder")
        button4.clicked.connect(self.get_folder)
        layout.addWidget(button4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        

    def get_filename(self):
        caption = "" #Empty use default caption.
        initial_dir = "" # Empty uses current folder.
        #adding specific file filters
        initial_filter = FILE_FILTERS[3] # selecting one from the list.

        #the below code joins the separate filter string to the list of filters
        #created earlier
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)
        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption= caption,
            #directory = initial_dir,
            filter = filters,
            #initialFilter=initial_filter, #unsupported key word 'initialFilter'
            )
        #this method returns - the filename and the current active file filter
        #in this case - the 'All File (*)'
        print("Result:", filename, selected_filter)

        ##########################################################################

        #creating QFileDialog instances manipulating the object using methods
        #instead of static method above:
        # caption = "Open file"
        # initial_dir ="" #Empty uses current folder
        # initial_filter = FILE_FILTERS[3] # Select one from the list.

        # dialog = QFileDialog()
        # dialog.setWindowTitle(caption)
        # dialog.setDirectory(initial_dir)
        # dialog.setNameFilters(FILE_FILTERS)
        # dialog.selectNameFilter(initial_filter)
        # dialog.setFileMode(QFileDialog.ExistingFile)

        # ok = dialog.exec()
        # print(
        # "Result:",
        # ok,
        # dialog.selectedFiles(),
        # dialog.selectedNameFilter(),
        # )

    def get_filenames(self):
        caption = "" #Empty use default caption.
        initial_dir = "" # Empty uses current folder.
        #adding specific file filters
        initial_filter = FILE_FILTERS[3] # selecting one from the list.

        #the below code joins the separate filter string to the list of filters
        #created earlier
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)
        filename, selected_filter = QFileDialog.getOpenFileNames(
            self,
            caption= caption,
            #directory = initial_dir,
            filter = filters,
            #initialFilter=initial_filter, #unsupported key word 'initialFilter'
            )
        #this method returns - the filename and the current active file filter
        #in this case - the 'All File (*)'
        print("Result:", filename, selected_filter)

        ##########################################################################

        #creating QFileDialog instances manipulating the object using methods
        #instead of static method above:
        # caption = "Open files"
        # initial_dir = "" # Empty uses current folder.
        # initial_filter = FILE_FILTERS[1] # Select one from the list.
        # dialog = QFileDialog()
        # dialog.setWindowTitle(caption)
        # dialog.setDirectory(initial_dir)
        # dialog.setNameFilters(FILE_FILTERS)
        # dialog.selectNameFilter(initial_filter)
        # dialog.setFileMode(QFileDialog.ExistingFiles)
        # ok = dialog.exec()
        # print(
        # "Result:",
        # ok,
        # dialog.selectedFiles(),
        # dialog.selectedNameFilter(),
        # )

    def get_save_filename(self):
        caption = "" #Empty use default caption.
        initial_dir = "" # Empty uses current folder.
        #adding specific file filters
        initial_filter = FILE_FILTERS[2] # selecting one from the list.

        #the below code joins the separate filter string to the list of filters
        #created earlier
        filters = ";;".join(FILE_FILTERS)
        print("Filters are:", filters)
        print("Initial filter:", initial_filter)
        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption= caption,
            #directory = initial_dir,
            filter = filters,
            #initialFilter=initial_filter, #unsupported key word 'initialFilter'
            )
        #this method returns - the filename and the current active file filter
        #in this case - the 'All File (*)'
        print("Result:", filename, selected_filter)

        ##########################################################################

        #creating QFileDialog instances manipulating the object using methods
        #instead of static method above:

        
        if filename:
            if os.path.exists(filename):
                #Existing file, ask the user for confirmation
                write_confirmed = QMessageBox.question(
                    self,
                    "Overwrite file?",
                    f"The file {filename} exists. Are you sure you want to overwrite it?",
                )
            else:
                #File does not exist, always-confirmed.
                write_confirmed= True

            if write_confirmed:
                with open(filename, "w") as f:
                    file_content = "YOUR FILE CONTENT"
                    f.write(file_content)


        ##########################################################################

        #creating QFileDialog instances manipulating the object using methods
        #instead of static method above:
        # caption = "Save As"
        # initial_dir = "" # Empty uses current folder.
        # initial_filter = FILE_FILTERS[1] # Select one from the list.
        # dialog = QFileDialog()
        # dialog.setWindowTitle(caption)
        # dialog.setDirectory(initial_dir)
        # dialog.setNameFilters(FILE_FILTERS)
        # dialog.selectNameFilter(initial_filter)
        # dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        # ok = dialog.exec()
        # print(
        # "Result:",
        # ok,
        # dialog.selectedFiles(),
        # dialog.selectedNameFilter(),
        # )

    def get_folder(self):
        #creating QFileDialog instances manipulating the object using methods
        #instead of static method
        caption = "Select folder"
        initial_dir = "" # Empty uses current folder.

        dialog = QFileDialog()
        dialog.setWindowTitle(caption)
        dialog.setDirectory(initial_dir)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        ok = dialog.exec()
        print(
        "Result:",
        ok,
        dialog.selectedFiles(),
        dialog.selectedNameFilter(),
        )

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
