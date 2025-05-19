import sys
import os
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QToolBar)

from PySide6.QtGui import QAction, QKeySequence, QIcon
from PySide6.QtCore import Qt, QSize 
from qt_material import apply_stylesheet

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Menu Project")
        apply_stylesheet(app,theme='dark_lightgreen.xml')

        #File Menu Actions
        new_file_action = QAction(
             QIcon(os.path.join(basedir, "new.png")),
             "&New File", self,
        )
        new_window_action = QAction(
             QIcon(os.path.join(basedir, "layer.png")),
             "&New Window", self,
        )
        open_file_action = QAction(
             QIcon(os.path.join(basedir, "document-text.png")),
             "&Open File", self,
        )
        open_folder_action = QAction(
             QIcon(os.path.join(basedir, "folder-open-document.png")),
             "&Open Folder", self,
        )
        save_action = QAction(
             QIcon(os.path.join(basedir, "disk-black.png")),
             "&Save", self,
        )
        save_as_action = QAction(
             QIcon(os.path.join(basedir, "disk.png")),
             "&Save As", self,
        )
        exit_action = QAction(
             QIcon(os.path.join(basedir, "cross.png")),
             "&Exit", self,
        )

        #Edit Menu Actions
        undo_action = QAction(
             QIcon(os.path.join(basedir, "undo-curve.png")),
             "&Undo", self,
        )
        redo_action = QAction(
             QIcon(os.path.join(basedir, "arrow-curve.png")),
             "&Redo", self,
        )
        cut_action = QAction(
             QIcon(os.path.join(basedir, "scissors-blue.png")),
             "&Cut", self,
        )
        copy_action = QAction(
             QIcon(os.path.join(basedir, "documents.png")),
             "&Copy", self,
        )
        paste_action = QAction(
             QIcon(os.path.join(basedir, "clipboard-paste.png")),
             "&Paste", self,
        )
        find_action = QAction(
             QIcon(os.path.join(basedir, "document-search-result.png")),
             "&Find", self,
        )
        replace_action = QAction(
             QIcon(os.path.join(basedir, "arrow-circle-225-left.png")),
             "&Replace", self,
        )

        #Selection Menu Actions
        selectAll_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Select All", self,
        )
        expand_selection_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Expand Selection", self,
        )
        shrink_selection_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Shrink Selection", self,
        )
        copyLineUp_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Copy Line Up", self,
        )
        copyLineDown_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Copy Line Down", self,
        )
        moveLineUp_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Move Line Up", self,
        )
        moveLineDown_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Move Line Down", self,
        )

        #View Menu Actions
        command_pallete_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Command Pallete...", self,
        )
        open_view_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Open View...", self,
        )
        appearance_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Appearance", self,
        )
        editor_layout_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Editor Layout", self,
        )
        explorer_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Explorer", self,
        )
        search_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Search", self,
        )
        source_control_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Source Control", self,
        )

         #Go Menu Actions
        back_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Back", self,
        )
        forward_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Forward", self,
        )
        last_edit_location_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Last Edit Location", self,
        )
        switch_editor_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Switch Editor", self,
        )
        switch_group_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Switch Group", self,
        )
        goto_file_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Go To File...", self,
        )
        goto_symbol_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Go To Symbol in Workspace...", self,
        )

        #Terminal Menu Actions
        new_terminal_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&New Terminal", self,
        )
        split_terminal_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Split Terminal", self,
        )
        run_task_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Run Task...", self,
        )
        run_build_task_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Run Build Task...", self,
        )
        configureTask_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Configure Tasks...", self,
        )
        configureTask_DefaultBuild_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Configure Default Build Task...", self,
        )

        #Help Menu Actions
        welcome_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Welcome", self,
        )
        documentation_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Documentation", self,
        )
        show_all_commands_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Show All Commands", self,
        )
        checkUpdates_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&Check Updates...", self,
        )
        about_action = QAction(
             QIcon(os.path.join(basedir, "bug.png")),
             "&About", self,
        )
        

        #creating the menu bar
        menu_bar = self.menuBar()

        #adding the File Menu and it's actions to the menu bar
        file_menu =menu_bar.addMenu("&File")
        file_menu.addAction(new_file_action)
        file_menu.addAction(new_window_action)

        file_menu.addSeparator()

        file_menu.addAction(open_file_action)

        file_menu.addAction(open_folder_action)
        file_menu.addSeparator()

        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()

        file_menu.addAction(exit_action)

        #adding the File Menu and it's actions to the menu bar
        edit_menu =menu_bar.addMenu("&Edit")
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()

        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addSeparator()

        edit_menu.addAction(find_action)
        edit_menu.addAction(replace_action)

        #adding the Selection Menu and it's actions to the menu bar
        selection_menu =menu_bar.addMenu("&Selection")
        selection_menu.addAction(selectAll_action)
        selection_menu.addAction(expand_selection_action)
        selection_menu.addAction(shrink_selection_action)
        selection_menu.addSeparator()
        
        selection_menu.addAction(copyLineUp_action)
        selection_menu.addAction(copyLineDown_action)
        selection_menu.addAction(moveLineUp_action)
        selection_menu.addAction(moveLineDown_action)
        

        #adding the View Menu and it's actions to the menu bar
        view_menu =menu_bar.addMenu("&View")
        view_menu.addAction(command_pallete_action)
        view_menu.addAction(open_view_action)
        view_menu.addSeparator()

        view_menu.addAction(appearance_action)
        view_menu.addAction(editor_layout_action)
        view_menu.addSeparator()

        view_menu.addAction(explorer_action)
        view_menu.addAction(search_action)
        view_menu.addAction(source_control_action)

        #adding the Go Menu and it's actions to the menu bar
        Go_menu =menu_bar.addMenu("&Go")
        Go_menu.addAction(back_action)
        Go_menu.addAction(forward_action)
        Go_menu.addAction(last_edit_location_action)
        Go_menu.addSeparator()

        Go_menu.addAction(switch_editor_action)
        Go_menu.addAction(switch_group_action)
        Go_menu.addSeparator()
        Go_menu.addAction(goto_file_action)
        Go_menu.addAction(goto_symbol_action)


        terminal_menu =menu_bar.addMenu("&Terminal")
        terminal_menu.addAction(new_terminal_action)
        terminal_menu.addAction(split_terminal_action)
        terminal_menu.addSeparator()

        terminal_menu.addAction(run_task_action)
        terminal_menu.addAction(run_build_task_action)
        terminal_menu.addSeparator()

        terminal_menu.addAction(configureTask_action)
        terminal_menu.addAction(configureTask_DefaultBuild_action)



        help_menu =menu_bar.addMenu("&Help")
        help_menu.addAction(welcome_action)
        help_menu.addAction(documentation_action)
        help_menu.addAction(show_all_commands_action)
        help_menu.addSeparator()

        help_menu.addAction(checkUpdates_action)
        help_menu.addSeparator()

        help_menu.addAction(about_action)

        




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
    

    