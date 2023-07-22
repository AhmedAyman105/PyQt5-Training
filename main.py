import sys
import typing 
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi


# UI file use XML language to convert drag and drop to machine language

# Main Class of welcome screen
class WelcomeScreen(QtWidgets.QDialog) :
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi('welcomescreen.ui',self)

# Application
app = QtWidgets.QApplication(sys.argv)

welcome = WelcomeScreen()

# Enable us to move between multiple screens smoothly 
widget = QtWidgets.QStackedWidget()

# Fixed width & height for the application
widget.setFixedHeight(800)
widget.setFixedWidth(1200)

# add the welcome screen to the stacked widget
widget.addWidget(welcome)


# display the widget
widget.show()



# Launch the application => Main Loop
app.exec_()