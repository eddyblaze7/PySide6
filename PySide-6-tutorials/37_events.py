import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,QLabel,QMainWindow,QTextEdit,QMenu
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        #self.setMouseTracking(True)
       
    

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            #handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mousePressEvent RIGHT")
            

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")
        

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

    def mouseMoveEvent(self, e):
         self.label.setText("mouseMoveEvent")

    # def on_context_Menu(self, pos):
    #     context = QMenu(self)
    #     context.addAction(QAction("test 1", self))
    #     context.addAction(QAction("test 2", self))
    #     context.addAction(QAction("test 3", self))
    #     context.exec(self.mapToGlobal(pos))

   
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()