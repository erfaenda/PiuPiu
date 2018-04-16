from PyQt5.QtWidgets import QCompleter, QPlainTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
import PyQTT.Complitter.test_3.MyCompleter

class AwesomeTextEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super(AwesomeTextEdit, self).__init__(parent)

        #self.completer = MyCompleterparent()
        self.completer.setWidget(self)
        self.completer.insertText.connect(self.insertCompletion)

    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (len(completion) - len(self.completer.completionPrefix()))
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)
        self.completer.popup().hide()

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self)
        QPlainTextEdit.focusInEvent(self, event)

    def keyPressEvent(self, event):

        tc = self.textCursor()
        if event.key() == Qt.Key_Tab and self.completer.popup().isVisible():
            self.completer.insertText.emit(self.completer.getSelected())
            self.completer.setCompletionMode(QCompleter.PopupCompletion)
            return

        QPlainTextEdit.keyPressEvent(self, event)
        tc.select(QTextCursor.WordUnderCursor)
        cr = self.cursorRect()

        if len(tc.selectedText()) > 0:
            self.completer.setCompletionPrefix(tc.selectedText())
            popup = self.completer.popup()
            popup.setCurrentIndex(self.completer.completionModel().index(0,0))

            cr.setWidth(self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:
            self.completer.popup().hide()