from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import gui1
class Signals(QtWidgets.QMainWindow, gui1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Signals, self).__init__(parent)
        self.setupUi(self)





def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = Signals()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app






if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
