# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'git_log_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(667, 531)
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fileOrDirectory = QtGui.QComboBox(self.centralwidget)
        self.fileOrDirectory.setObjectName(_fromUtf8("fileOrDirectory"))
        self.gridLayout.addWidget(self.fileOrDirectory, 0, 0, 1, 1)
        self.pathDisplay = QtGui.QLineEdit(self.centralwidget)
        self.pathDisplay.setEnabled(False)
        self.pathDisplay.setText(_fromUtf8(""))
        self.pathDisplay.setObjectName(_fromUtf8("pathDisplay"))
        self.gridLayout.addWidget(self.pathDisplay, 0, 1, 1, 1)
        self.timeLine = QtGui.QComboBox(self.centralwidget)
        self.timeLine.setWhatsThis(_fromUtf8(""))
        self.timeLine.setObjectName(_fromUtf8("timeLine"))
        self.gridLayout.addWidget(self.timeLine, 1, 0, 1, 1)
        self.revisions = QtGui.QLineEdit(self.centralwidget)
        self.revisions.setText(_fromUtf8(""))
        self.revisions.setObjectName(_fromUtf8("revisions"))
        self.gridLayout.addWidget(self.revisions, 1, 1, 1, 1)
        self.commentTree = QtGui.QTreeWidget(self.centralwidget)
        self.commentTree.setMaximumSize(QtCore.QSize(643, 16777215))
        self.commentTree.setObjectName(_fromUtf8("commentTree"))
        self.commentTree.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.commentTree, 2, 0, 1, 2)
        self.errorBox = QtGui.QPlainTextEdit(self.centralwidget)
        self.errorBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.errorBox.setFrameShadow(QtGui.QFrame.Sunken)
        self.errorBox.setDocumentTitle(_fromUtf8(""))
        self.errorBox.setObjectName(_fromUtf8("errorBox"))
        self.gridLayout.addWidget(self.errorBox, 3, 0, 1, 2, QtCore.Qt.AlignVCenter)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout.addWidget(self.quitButton, 4, 1, 1, 1)
        self.resetButton = QtGui.QPushButton(self.centralwidget)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.gridLayout.addWidget(self.resetButton, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionControl_q = QtGui.QAction(MainWindow)
        self.actionControl_q.setObjectName(_fromUtf8("actionControl_q"))
        self.quitFromMenu = QtGui.QAction(MainWindow)
        self.quitFromMenu.setObjectName(_fromUtf8("quitFromMenu"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GitLog", None))
        self.fileOrDirectory.setToolTip(_translate("MainWindow", "Select the file or folder for which the history has to be found", None))
        self.fileOrDirectory.setStatusTip(_translate("MainWindow", "Select the required file or folder", None))
        self.pathDisplay.setPlaceholderText(_translate("MainWindow", "Path of selected file/folder will be displayed here.", None))
        self.timeLine.setToolTip(_translate("MainWindow", "Select the time duration for which the history has to be displayed.", None))
        self.timeLine.setStatusTip(_translate("MainWindow", "Select the timeline", None))
        self.revisions.setPlaceholderText(_translate("MainWindow", "Seach using SHA revisions (short(atleast first 4 characters) or full form).", None))
        self.commentTree.setToolTip(_translate("MainWindow", "Tree widget to dipaly the history.", None))
        self.commentTree.setStatusTip(_translate("MainWindow", "Tree widget to dipaly the history", None))
        self.errorBox.setToolTip(_translate("MainWindow", "Errors will be displayed here.", None))
        self.errorBox.setStatusTip(_translate("MainWindow", "Error Box", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.resetButton.setToolTip(_translate("MainWindow", "Resets all the fields to their original values.", None))
        self.resetButton.setStatusTip(_translate("MainWindow", "Reset the fields", None))
        self.resetButton.setText(_translate("MainWindow", "Reset All Fields", None))
        self.actionControl_q.setText(_translate("MainWindow", "control+q", None))
        self.quitFromMenu.setText(_translate("MainWindow", "Quit", None))
        self.quitFromMenu.setStatusTip(_translate("MainWindow", "Quit the application", None))
        self.quitFromMenu.setShortcut(_translate("MainWindow", "Meta+Q", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

