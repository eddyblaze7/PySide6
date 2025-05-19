from typing import Optional
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QObject, Qt, Signal, QRunnable, QThreadPool

class WorkerSignals(QObject):
    finished = Signal()
    result = Signal(str)


class MyRunnable(QRunnable):
    def __init__(self, data):
        super(MyRunnable, self).__init__()
        self.data = data
        self.signals = WorkerSignals()

    def run(self):
        #Simulate a time-consuming task
        result=f"Processed data: {self.data}"
        self.signals.result.emit(result)
        self.signals.finished.emit()


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Waiting for result...")

        self.threadpool = QThreadPool()

        #Example data to be processed
        data_to_process = ["Data 1", "Data 2", "Data 3", "Data 4"]

        for data in data_to_process:
            runnable =MyRunnable(data)
            runnable.signals.result.connect(self.on_result)
            runnable.signals.finished.connect(self.on_finished)

            #Execute the runnable in the thread pool
            self.threadpool.start(runnable)

        self.setLayout(self.layout)

    def on_result(self, result):
        #Handle the result from the runnable
        self.label.setText(result)

    def on_finished(self):
        print("Task finished")

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()