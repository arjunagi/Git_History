Files in the application:
-------------------------
git_log_ui.ui - The .ui file generated as the output of Qt Designer
git_log_ui.py - The ui file converted to python
git_log.py    - The file with the main implementation. This inherits the ui file.
  
How to run the application:
---------------------------
Make sure all the above files are in the same directory and Pyqt4 is installed.
The application can be run using the command:

		python git_log.py

Application Layout:
-------------------
The application containst the following fields/widgets. You can hover the mouse over each field in the app UI to learn more about its functionality.
1. Select File or Directory
2. Display the path of selected file or directory
3. Search based on timeline
4. Seach using revision(s)
5. Tree widget to display the history logs
6. Error box (read only)
7. Reset all fields
8. Quit


How to use the application:
---------------------------
1. From the drop down menu, select if you want to view the history of a file or a directory. Then, select the desire file/directory. The path of the selected file/directory will be displayed in a text box on the top.

IMPORTANT: 
- Select files/directory from a git repository. If you select files which are not in a git repo, an error will be shown.
- The other fields are enabled only after a file/directory is chosen!

2. You can either select the timeline from the drop down menu or type the revisions(comma separated) in the text box. The search for history will be made for this time line or for these revisions.

3. The result will be displayed in the tree widget. The items in the tree will be comments and its respective logs will be displayed under it.

4. Errors, if any, will be displayed in the error box.

5. You can continue using the application even if you encounter an error.

6. Use "Reset All Fields" button to start fresh.

7. Use the "Quit" button to exit the app.
