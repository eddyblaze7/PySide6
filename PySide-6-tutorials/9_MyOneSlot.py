from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QMainWindow
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")

        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        #also change the text on the button
        self.button.setText("You already clicked me")
        self.button.setEnabled(False)

        #Also change the window title
        self.setWindowTitle("My Oneshot App")
        self.setWindowTitle("A new window title")

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()