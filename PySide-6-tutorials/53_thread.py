import sys
import time

from PySide6.QtCore import QTimer, QRunnable,QThreadPool, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget

)

class Worker(QRunnable):
    """
    Worker thread
    """
    @Slot()
    def run(self):
        """
        Your code goes in this method
        """
        

        




        print("Thread start")
        time.sleep(5)
        print("Thread complete")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads"
            % self.threadpool.maxThreadCount()
        )

        self.counter = 0
        layout = QVBoxLayout()
        self.l = QLabel("Start")
        b= QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w=QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)
        self.show()




    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)


app = QApplication(sys.argv)

window = MainWindow()
app.exec()