from PySide6.QtWidgets import QMainWindow,   QPushButton

#Building on top of QMainWindow
class ButtonHolder(QMainWindow):
    def __init(self):
        super().__init__()

        self.setWindowTitle("Our First MainWindow App")

        #this creates the pushButton instance
        button = QPushButton("Press Me!!")
    

        #this command adds the button widget to the mainWindow
        self.setCentralWidget(button)
