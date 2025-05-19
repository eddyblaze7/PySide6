import sys
import os
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QApplication,QSpinBox,
                               QMainWindow, QComboBox,
                               QTextEdit, QFileDialog,
                               QToolBar)
from PySide6.QtGui import QAction, QIcon, QFont, Qt
from PySide6 import QtPrintSupport


class RTE(QMainWindow):
    def __init__(self):
        super().__init__()

        self.textEditor = QTextEdit()
        self.setCentralWidget(self.textEditor)
        self.setWindowTitle("Rich Text Editor")
        #change of font size functionality
        self.fontSizeBox = QSpinBox()

        self.createToolBar()
        self.showMaximized()
        self.textEditor.setFontPointSize(22)
        self.boldText()

        #static font
        font = QFont("Times New Roman", 24)
        self.textEditor.setFont(font)
        self.path = ""

    def createToolBar(self):
        toolbar = QToolBar()
        
        self.saveBtn = QAction(QIcon("noun-floppy-1866618.svg "), 'Save', self)
        self.saveBtn.triggered.connect(self.saveFile)
        toolbar.addAction(self.saveBtn)

        self.undoBtn = QAction(QIcon("undo-curve.png"), 'Undo', self)
        self.undoBtn.triggered.connect(self.textEditor.undo)
        toolbar.addAction(self.undoBtn)

        self.redoBtn = QAction(QIcon("arrow-curve.png"), 'Redo', self)
        self.redoBtn.triggered.connect(self.textEditor.redo)
        toolbar.addAction(self.redoBtn)

        self.copyBtn = QAction(QIcon("documents.png"), 'Copy', self)
        self.copyBtn.triggered.connect(self.textEditor.copy)
        toolbar.addAction(self.copyBtn)

        self.cutBtn = QAction(QIcon("scissors-blue.png"), 'Cut', self)
        self.cutBtn.triggered.connect(self.textEditor.cut)
        toolbar.addAction(self.cutBtn)

        self.pasteBtn = QAction(QIcon("clipboard-paste-document-text.png"), 'Paste', self)
        self.pasteBtn.triggered.connect(self.textEditor.paste)
        toolbar.addAction(self.pasteBtn)

        #creating a combo box for a list of font types
        self.fontBox = QComboBox(self)
        self.fontBox.addItems(["Courier Std","Hellentic Typewriter Regular","Helvetica",
                               "Times New Roman","Monospace","Arial"])
        
        self.fontBox.activated.connect(self.setFont)
        toolbar.addWidget(self.fontBox)

        #you can add widgets to your toolbar
        self.fontSizeBox.setValue(24)
        self.fontSizeBox.valueChanged.connect(self.setFontSize)
        toolbar.addWidget(self.fontSizeBox)

        self.leftAlign = QAction(QIcon("edit-alignment-left.png"),'Right Align', self)
        self.leftAlign.triggered.connect(lambda:self.textEditor.setAlignment(Qt.AlignLeft))
        toolbar.addAction(self.leftAlign)
        self.addToolBar(toolbar)

        self.centerAlign = QAction(QIcon("edit-alignment-center.png"),'Center Align', self)
        self.centerAlign.triggered.connect(lambda:self.textEditor.setAlignment(Qt.AlignCenter))
        toolbar.addAction(self.centerAlign)
        self.addToolBar(toolbar)


        self.rightAlign = QAction(QIcon("edit-alignment-right.png"),'Right Align', self)
        self.rightAlign.triggered.connect(lambda:self.textEditor.setAlignment(Qt.AlignRight))
        toolbar.addAction(self.rightAlign)
        self.addToolBar(toolbar)

        self.justifyAlign = QAction(QIcon("edit-alignment-justify.png"),'Justify Align', self)
        self.justifyAlign.triggered.connect(lambda:self.textEditor.setAlignment(Qt.AlignJustify))
        toolbar.addAction(self.justifyAlign)
        self.addToolBar(toolbar)

        self.boldBtn = QAction(QIcon("scissors-blue.png"), 'Bold', self)
        self.boldBtn.triggered.connect(self.boldText)
        toolbar.addAction(self.boldBtn)

        self.underlineBtn = QAction(QIcon("scissors-blue.png"), 'Cut', self)
        self.underlineBtn.triggered.connect(self.underlineText)
        toolbar.addAction(self.underlineBtn)

        self.italicBtn = QAction(QIcon("scissors-blue.png"), 'Cut', self)
        self.italicBtn.triggered.connect(self.italicText)
        toolbar.addAction(self.italicBtn)

    #font type
    def setFont(self):
        font = self.fontBox.currentText()
        fontSize = self.fontSizeBox.value()
        self.textEditor.setCurrentFont(QFont(font, fontSize))

    #font size
    def setFontSize(self):
        value =self.fontSizeBox.value()
        self.textEditor.setFontPointSize(value)

    def italicText(self):
        state= self.textEditor.fontItalic()
        self.textEditor.setFontItalic(not(state))

    def underlineText(self):
        state= self.textEditor.fontUnderline()
        self.textEditor.setFontUnderline(not(state))

    def boldText(self):
         if self.textEditor.fontWeight != QFont.Bold:
            self.textEditor.setFontWeight(QFont.Bold)
            return
         self.textEditor.setFontWeight(QFont.Normal)

    def saveFile(self):
        print(self.path)
        if self.path == "":
            self.file_saveas()
        text = self.textEditor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def file_saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(
           "Save file", "", "text documents(*txt);All files (*.*)" 
        )
        if self.path == "":
            return
        text = self.textEditor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)



app= QApplication(sys.argv)
window = RTE()
window.show()
app.exec()