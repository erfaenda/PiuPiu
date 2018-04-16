from PyQt5.QtWidgets import QCompleter
from PyQt5 import QtCore

class MyCompleter(QCompleter):
    insertText = QtCore.pyqtSignal(str)

def __init__(self, parent=None):
    QCompleter.__init__(self, ["test","foo","bar"], parent)
    self.setCompletionMode(QCompleter.PopupCompletion)
    self.highlighted.connect(self.setHighlighted)

def setHighlighted(self, text):
    self.lastSelected = text

def getSelected(self):
    return self.lastSelected