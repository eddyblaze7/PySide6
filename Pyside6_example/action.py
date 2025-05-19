from PySide6.QtWidgets import (QMainWindow, QLabel,QWidget, 
                               QVBoxLayout, QFileDialog, QToolBar)
from PySide6.QtGui import QAction, QKeySequence, QIcon, QFont, Qt
from qt_material import apply_stylesheet

import os

basedir = os.path.dirname(__file__)

# creating a list of file filters
# FILE_FILTERS = [
#     "Portable Network Graphics files (*.png)",
#     "Text files (*.txt)",
#     "Comma Separated values (*.csv)",
#     "All files (*)",
# ]

class Action(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Menu Project")
        

        #File Menu Actions
        new_file_action = QAction(
             QIcon(os.path.join(basedir, "new.png")),
             "&New File", self,
        )
        save_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&Save", self,
        )
        save_action.setShortcut(QKeySequence("Ctrl+s"))

        image_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&Image", self,
        )
        network1_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&Network", self,
        )
        network2_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&Network", self,
        )
        open_file_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&File(s)", self,
        )
        open_file_action.setShortcut(QKeySequence("Ctrl+Shift+F"))

        open_folder_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&Folder", self,
        )
        open_folder_action.setShortcut(QKeySequence("Ctrl+Shift+L"))

        open_file2_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&File(s)", self,
        )
        open_file2_action.setShortcut(QKeySequence("Ctrl+Alt+F"))
        
        open_folder2_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&Folder", self,
        )
        open_folder2_action.setShortcut(QKeySequence("Ctrl+Alt+O"))

        #Edit Menu Actions
        undo_action = QAction(
             QIcon(os.path.join(basedir, "undo-curve.png")),
             "&Undo", self,
        )
        undo_action.setShortcut(QKeySequence("Ctrl+Z"))

        redo_action = QAction(
             QIcon(os.path.join(basedir, "arrow-curve.png")),
             "&Redo", self,
        )
        redo_action.setShortcut(QKeySequence("Ctrl+Y"))

        zoomIn_action = QAction(
             QIcon(os.path.join(basedir, "scissors-blue.png")),
             "&Zoom", self,
        )
        zoomIn_action.setShortcut(QKeySequence("+"))
        zoomOut_action = QAction(
             QIcon(os.path.join(basedir, "scissors-blue.png")),
             "&Zoom", self,
        )
        zoomOut_action.setShortcut(QKeySequence("-"))
        zoom_selection = QAction(
             QIcon(os.path.join(basedir, "scissors-blue.png")),
             "&Zoom Selection", self,
        )
        pan_action = QAction(
             QIcon(os.path.join(basedir, "documents.png")),
             "&Pan", self,
        )
        pan_action.setShortcut(QKeySequence("Shift+P"))
        
       

        
       
        #View Menu Actions
        map_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Map", self,
        )
        map_action.setShortcut(QKeySequence("F1"))

        image2_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Image", self,
        )
        image2_action.setShortcut(QKeySequence("F2"))

        video_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Video", self,
        )
        video_action.setShortcut(QKeySequence("F3"))
        
     #     #Settings Menu Actions
     #    default_action = QAction(
     #         QIcon(os.path.join(basedir, "bug.png")),
     #         "&Default", self,
     #    )
     #    dark_action = QAction(
     #         QIcon(os.path.join(basedir, "bug.png")),
     #         "&Dark", self,
     #    )


        

        #creating the menu bar
        menu_bar = self.menuBar()

        #adding the File Menu and it's actions to the menu bar
        file_menu =menu_bar.addMenu("&File")
         #submenu
        import_menu = file_menu.addMenu("&Import")

        #submenu under import
        video_menu = import_menu.addMenu("&Video")
      

        local_menu = video_menu.addMenu("&Local")
        video_menu.addAction(network1_action)
        image_menu = import_menu.addMenu("&Image")

        local_menu2 = image_menu.addMenu("&Local")
        image_menu.addAction(network2_action)

        local_menu.addAction(open_file_action)
        open_file_action.triggered.connect(self.get_Video_filenames)
        local_menu.addAction(open_folder_action)
        open_folder_action.triggered.connect(self.get_folder)

        local_menu2.addAction(open_file2_action)
        open_file2_action.triggered.connect(self.get_image_filenames)
        local_menu2.addAction(open_folder2_action)
        open_folder2_action.triggered.connect(self.get_folder)

        file_menu.addAction(save_action)
        

     
        #adding the File Menu and it's actions to the menu bar
        edit_menu =menu_bar.addMenu("&Edit")
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()

        zoom_menu = edit_menu.addMenu("&Zoom")
        zoom_menu.addAction(zoomIn_action)
        zoom_menu.addAction(zoomOut_action)
        zoom_menu.addAction(zoom_selection)
        #edit_menu.addAction(zoom_action)
        edit_menu.addAction(pan_action)
     
        edit_menu.addSeparator()

     
        #adding the View Menu and it's actions to the menu bar
        view_menu =menu_bar.addMenu("&View")
        view_menu.addAction(map_action)
        view_menu.addSeparator()

        view_menu.addAction(image2_action)
        
        view_menu.addSeparator()
        view_menu.addAction(video_action)

     #    #adding the File Menu and it's actions to the menu bar
     #    settings_menu = menu_bar.addMenu("&Settings")
     #    theme_menu = settings_menu.addMenu("&Themes")
     #    theme_menu.addAction(default_action)
     #    theme_menu.addAction(dark_action)

        

        #creating a toolbar
        tool_bar = QToolBar()
        self.addToolBar(tool_bar) 

       



        
        layout = QVBoxLayout()
        widget = QWidget()

        #widget.setLayout(layout)

     #    serifFont = QFont("Times", 10, QFont.Bold)
     #    sansFont = QFont("Helvetica [Cronyx]", 12)
        
     
        self.label = QLabel("Add a View")
        font = QFont()
        font.setFamily("Arial")
        
        font.pointSize()
        #font.setWeight(75)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        #self.label.setGeometry(20,20,100,100)
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        
     #    serifFont = QFont("Times", 10, QFont.Bold)
     #    sansFont = QFont("Helvetica [Cronyx]", 12)

    def get_Video_filenames(self):
        FILE_FILTERS = [
          "MPEG-4 (*.mp4)",
          "Transport Stream (*.ts)",
          "QuickTime Video Format (*.mov)",
          
          ]
        caption = "" #Empty use default caption.
        initial_dir = "" # Empty uses current folder.
        #adding specific file filters
        initial_filter = FILE_FILTERS[0] # selecting one from the list.

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

    def get_image_filenames(self):
        FILE_FILTERS = [
          "Joint Photograph Experts Group (*.jpg)",
          
          ]
        caption = "" #Empty use default caption.
        initial_dir = "" # Empty uses current folder.
        #adding specific file filters
        initial_filter = FILE_FILTERS[0] # selecting one from the list.

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
     
    



