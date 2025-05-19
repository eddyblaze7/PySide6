import sys
from PyQt5.QtCore import QByteArray
from PyQt5.QtWidgets import QApplication



app= QApplication(sys.argv)

# Create a new byte array
ba = QByteArray()

# Append some data to the byte array
ba.append(b'Hello, world!')

# Print the contents of the byte array
print(ba.data())

app.exec_()