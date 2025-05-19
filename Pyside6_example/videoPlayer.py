import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QMediaContent
from PySide6.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.video_widget = QVideoWidget(self)
        self.layout.addWidget(self.video_widget)
        
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)
        
        self.open_button = QPushButton("Open Video", self)
        self.open_button.clicked.connect(self.open_video)
        self.layout.addWidget(self.open_button)
        
    def open_video(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Videos (*.mp4 *.avi *.mkv)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            media_content = QMediaContent.fromLocalFile(file_path)
            self.media_player.setMedia(media_content)
            self.media_player.play()

app = QApplication(sys.argv)
player = VideoPlayer()
player.show()
app.exec_()
