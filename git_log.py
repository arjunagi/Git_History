__author__ = "Karthik Ashok Arjunagi"

'''
Application to browse git history.
This program uses the git command "git log" to enable history browsing and
it also provides a UI to select the required file/directory.
The UI is designed using QT Designer and is extracted to the file "git_log_ui.py".
This module is imported here and is used to generate the signals and handle respective slots .
'''

import sys, os
import subprocess
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL,SLOT

import git_log_ui           # import the ui module


class GitLog(QtGui.QMainWindow, git_log_ui.Ui_MainWindow):
    '''
        Class GitLog inherits the QtGui.QMainWindow and git_log_ui.Ui_MainWindow classes.
        It uses them to provide the UI for this application.
    '''
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
        git_log_ui.Ui_MainWindow.__init__(self) 
        self.setupUi(self) # The widget (here, it is window) where the app interface is created

        # Provide the options for the combo box to select a file or directory
        self.fileOrDirectory.setCurrentIndex(0)
        self.fileOrDirectory.addItem("Select File or Directory")
        self.fileOrDirectory.addItem("File")
        self.fileOrDirectory.addItem("Directory")
        self.fileOrDirectory.activated[str].connect(self.select_file_or_directory) # Define the signal when the event of selecting an option takes place

        # Define the signal (call the close_application method) when the event of clicking "Quit" button happens
        self.quitButton.clicked.connect(self.close_application)

        # Define the signal when the event of clicking "Reset All Fields" button happens
        self.resetButton.clicked.connect(self.reset_all_fields)

        self.commentTree.setHeaderHidden(True)  
        self.errorBox.setReadOnly(True)

        # Define the signal when the path of file/directory is found
        self.pathDisplay.selectionChanged.connect(self.display_path)
        self.pathDisplay.setEnabled(False) # Enabled only after a file/directory is selected

        # Provide the options for the combo box to select the timeline
        self.timeLine.setCurrentIndex(0)
        self.timeLine.addItem("Search based on timeline")
        self.timeLine.addItem("From the beginning of time")
        self.timeLine.addItem("1 year")
        self.timeLine.addItem("6 months")
        self.timeLine.addItem("3 months")
        self.timeLine.addItem("1 month")
        self.timeLine.addItem("2 weeks")
        self.timeLine.addItem("1 week")
        self.timeLine.addItem("3 days")
        self.timeLine.addItem("Today")

        self.timeLine.setEnabled(False) # Enabled only after a file/directory is selected
        self.timeLine.activated[str].connect(self.get_git_log_using_timeline) # Action to take when a timeline is selected

        # Action to take when revisions are entered in the line edit box
        self.revisions.connect(self.revisions, SIGNAL("textEdited(QString)"), self.revisions, SLOT("setText(QString)"))
        self.revisions.editingFinished.connect(lambda: self.get_git_log_using_revisions(self.revisions.text()))    
        self.revisions.setEnabled(False) # Enabled only after a file/directory is selected

        # Enable the status bar the bottom of the window
        self.statusBar()

        
    def select_file_or_directory(self, fileOrDir):
        '''
        Function to check what option was selected (File/Directory) and call the appropriate
        function to get the file/directory path.

        Parameters:
        -----------
        fileOrDir: String. Will have the value selected in the "Select File/Directory" combo box
        '''
        if fileOrDir == "File":
            self.get_file_path()  # Get the path of the selected file 
            self.errorBox.clear() # Clearing the error if a mistake was made in the previous attempts
        elif fileOrDir == "Directory":
            self.get_directory_path() # Get the path of the selected directory
            self.errorBox.clear() # Clearing the error if a mistake was made in the previous attempts
        else:
            self.errorBox.setPlainText("File/Directory not chosen") # Error will be show if neither a file nor a directory was selected

            
    def get_file_path(self):
        '''
        Function to get the full path of the selected file.
        '''
        self.filePath = QtGui.QFileDialog.getOpenFileName(self,"Pick a file") # Get the path
        self.dirPath = os.path.dirname(str(self.filePath)) # Get the directory of the file
        if self.filePath:
            self.forDir = False                     # Flag to indicate if the history search is to be made for a directory or a file
            self.display_path(str(self.filePath))   # Display the path in the display box
            self.timeLine.setEnabled(True)          # Enable the time line combo box
            self.revisions.setEnabled(True)         # Enable the text box to enter revisions
            self.errorBox.clear()                   # Clearing the error if a mistake was made in the previous attempts
        else:
            self.errorBox.setPlainText("File not chosen")


    def get_directory_path(self):
        '''
        Function to get the full path of the selected directory.
        '''
        self.dirPath = QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder") # Get the path of the directory
        if self.dirPath:
            self.forDir = True                  # Flag to indicate if the history search is to be made for a directory or a file
            self.display_path(str(self.dirPath)) # Display the path in the display box
            self.timeLine.setEnabled(True)      # Enable the time line combo box
            self.revisions.setEnabled(True)     # Enable the text box to enter revisions
            self.errorBox.clear()               # Clearing the error if a mistake was made in the previous attempts
        else:
            self.errorBox.setPlainText("Directory not chosen")

    
    def display_path(self,path):
        '''
        Function to display the path of file/directory in the text box.
        
        Parameters:
        -----------
        path: String. The path to be displayed in the text box
        '''
        if path:
            self.pathDisplay.setEnabled(True)   # Enable the text box 
            self.pathDisplay.setText(path)      # Insert the path in the text box

                
    def get_git_log_using_timeline(self, time):
        '''
        Function to get the output of the 'git log' command for the selected file/directory
        over the selected time duration.

        Parameters:
        -----------
        time: String. The time duration selected from the time line combo box.
        '''
        cmd = ""
        if self.forDir:     # For the selected directory 
            if str(time) == "From the beginning of time":   # Ready the git command to get each revision and its respective comment
                cmd = "git -C " + str(self.dirPath) + " log --pretty=format:\"%h %s\""
            else:                                           # Ready the git command to get each revision and its respective comment over the selected timeline
                cmd = "git -C " + str(self.dirPath) + " log --pretty=format:\"%h %s\" --since=\"" + str(time) + "\""
        else:               # For the selected file
            if str(time) == "From the beginning of time":   # Ready the git command to get each revision and its respective comment
                cmd = "git -C " + str(self.dirPath) + "/ " + " log --pretty=format:\"%h %s\" " + str(self.filePath)
            else:                                           # Ready the git command to get the each revision and its respective comment over the selected timeline
                cmd = "git -C " + str(self.dirPath) + "/ " + " log --pretty=format:\"%h %s\" --since=\"" + str(time) + "\" " + str(self.filePath) 
        
        try:
            self.gitLog = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True) # Get the revisions(hash) and comments of the file/directory using the git command formed above
            if self.gitLog == "":   # 'git log' returns empty when there is no logs
                self.errorBox.setPlainText("No history for the timeline: " + str(time))
            else:
                self.errorBox.clear()
                self.hashAndComment = dict(x.split(' ',1) for x in str(self.gitLog).splitlines()) # Create a dictionary of the form {'hash':'comment'} where hash is revisions
                self.create_comment_tree()  # Creat the comment tree for the retrieved logs
        except AttributeError as e2:
            self.errorBox.setPlainText ("Git error: " + str(e2))
        except subprocess.CalledProcessError as e3:
            self.errorBox.setPlainText("git log error: " + str(e3))


    def get_git_log_using_revisions(self, revs):
        '''
        Function to get the output of the 'git log' command for the given SHA revisions.

        Parameters:
        -----------
        revs: String. The revision(s) entered in the text box
        '''
        revs = str(self.revisions.displayText()).split(',') # Create a list of the revisions
        if self.forDir:         # Ready the git command to get the history of the given revisions for a directory
            cmd = "git -C " + str(self.dirPath) + " log --pretty=\"%s\" " + ' '.join(revs) + " -n " + str(len(revs))
        else:                   # Ready the git command to get the history of given revisions for a file
            cmd = "git -C " + str(self.dirPath) + " log --pretty=\"%s\" " + ' '.join(revs) + " -n " + str(len(revs)) + " " + str(self.filePath)
        try:
            comments = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True) # Get the revisions and comments of the selected file/directory using the git command formed above
            if comments == "":
                self.errorBox.setPlainText("No history available") 
            else:
                self.errorBox.clear()
                self.hashAndComment = dict(zip(revs,comments.split("\n"))) # Create a dictionary of the form {'revs':'comment'}
                self.create_comment_tree()          # Creat the comment tree for the retrieved logs
        except subprocess.CalledProcessError as e:
            self.errorBox.setPlainText("git log error: " + str(e))

        
    def create_comment_tree(self):
        '''
        Function to add the logs in the tree widget using comments as each item in the tree.
        '''
        cmd = ""
        self.commentTree.clear()
        for key in self.hashAndComment:     # Get each log one by one and add it to the tree
            if self.forDir:             # Ready the command to get the log for the directory using the revison
                cmd = "git -C " + str(self.dirPath) + " log " + key + " -n 1"
            else:                       # Ready the command to get the log for the file using the revison
                cmd = "git -C " + str(self.dirPath) + " log " + key + " -n 1 " + str(self.filePath)
            self.individualLogs = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True) # Get the log for the file/directory using the revison
            item = QtGui.QTreeWidgetItem([self.hashAndComment.get(key)])    # Add the comment as the item in the tree
            item.addChild(QtGui.QTreeWidgetItem([self.individualLogs]))     # Add the entire log as contents of the item(comment)
            self.commentTree.addTopLevelItem(item)


    def close_application(self):
        '''
        Function to close the application
        '''
        # Message box to enquire if the user wants to quit the application.
        choice = QtGui.QMessageBox.question(self, 'Quit', "Quit the application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Application closed!")
            sys.exit()
        else:
            pass
        

    def reset_all_fields(self):
        '''
        Function to reset all the fields in the application UI
        '''
        self.fileOrDirectory.setCurrentIndex(0)
        self.timeLine.setCurrentIndex(0)
        self.timeLine.setEnabled(False)
        self.pathDisplay.clear()
        self.pathDisplay.setEnabled(False)
        self.revisions.clear()
        self.revisions.setEnabled(False)
        self.commentTree.clear()
        self.errorBox.clear()


def main():
    app = QtGui.QApplication(sys.argv)
    gui = GitLog()
    gui.show()
    app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
        
