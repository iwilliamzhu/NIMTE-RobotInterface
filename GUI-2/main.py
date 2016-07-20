from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import gui2
class Signals(QtWidgets.QMainWindow, gui2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Signals, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.stackedWidget.setPage1)
        self.pushButton_2.clicked.connect(self.stackedWidget.setPage2)

    def changeFrame1(self):
        #self.stack.setCurrentWidget(self.mapScreen)
        self.stackedWidget.clicked.connect(stack.setPage1)
    def changeFrame2(self):
        #self.stack.setCurrentWidget(self.propertyScreen)
        self.stackedWidget.clicked.connect(stack.setPage2)
    

#Code to add Images
'''
self.label.setPixmap(QtGui.QPixmap('98C4CeMr.jpg'))
self.label.setScaledContents(True)
self.label_2.setPixmap(QtGui.QPixmap('PpgMdkJr.jpg'))
self.label_2.setScaledContents(True)

'''


def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = Signals()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app






if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
