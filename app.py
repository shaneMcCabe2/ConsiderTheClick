import sys #handles exit status of application


from PyQt5 import QtWidgets, QtSql, QtGui # widget creation, sql db connecion, gui features
from PyQt5.QtWidgets import (
QApplication, # to create application instances
QLabel, # displays text
QWidget, # create application GUI
QDesktopWidget, # to manipulate GUI relative to desktop
QMainWindow # window creation
)

# create app and define GUI parameters
# Create DB connection
# create form to pass quotes to DB
# display quotes

# define parent class Window
class Window(QMainWindow):
    def __init__(self, parent=None):
        # super can be used to refer to parent classes without explicit naming
        super(Window, self).__init__(parent)
        # set window parameters
        self.setWindowTitle('Consider the click. Time is your most valuable currency.')
        self.setMinimumWidth(int(resolution.width() / 3))
        self.setMinimumHeight(int(resolution.height() / 3))

# create the database to host quotes
def createDB():
    # set db as sqlite3
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('quotes.db')

    # error message if db connection is closed
    if not db.open():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error in Database Creation")
        retval = msg.exec_()
        return False

    # create table quotes
    query = QtSql.QSqlQuery()
    query.exec_("DROP TABLE IF EXISTS posts; CREATE TABLE quotes (id INTEGER PRIMARY KEY AUTOINCREMENT, quote VARCHAR(1000), author VARCHAR(100));")
    query.exec_("INSERT INTO quotes VALUES ('testQuote', 'testAuthor')")
    return True


# define main function
if __name__ == "__main__":

    # create app instance
    app = QApplication(sys.argv)

    createDB()

    # get desktop info, call Window class, and place window in center of screen
    desktop = QApplication.desktop()
    resolution = desktop.availableGeometry()
    app_window = Window()
    app_window.show()
    app_window.move(resolution.center() - app_window.rect().center())
    sys.exit(app.exec_())
