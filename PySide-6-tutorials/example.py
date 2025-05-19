from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer

counter = 0

def update_label():
    global counter
    counter += 1
    label.setText(f"Counter: {counter}")

# Create the application
app = QApplication([])

# Create the main window widget
window = QWidget()

# Create a vertical layout for the window
layout = QVBoxLayout()
window.setLayout(layout)

# Create the label widget
label = QLabel("Counter: 0")
layout.addWidget(label)

# Create a QTimer to update the label every second
timer = QTimer()
timer.timeout.connect(update_label)
timer.start(1000)  # 1000 milliseconds = 1 second

# Show the main window
window.show()

# Start the application event loop
app.exec()