# Imports
import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
import sqlite3

# UI file use XML language to convert drag and drop to machine language

# Main Class of welcome screen
class WelcomeScreen(QtWidgets.QDialog) :
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi(r'UI\welcomescreen.ui',self)
        self.login.clicked.connect(self.gotologin)
        self.create_account.clicked.connect(self.gotosignup)

    def gotologin(self) :
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotosignup(slelf) :
        signup = SignUP()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)



# Login Screen class
class LoginScreen(QtWidgets.QDialog): 
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi(r'UI\login.ui',self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login2.clicked.connect(self.loginfunc)

    def loginfunc(self):
        
        user = self.emailfield.text()
        password = self.passwordfield.text()
        
        if len(user) == 0 or len(password) == 0 :
            
            self.placeholder.setText("Please Fill All Fields")
        else:
            conn = sqlite3.connect('data.db')
            cr = conn.cursor()
            try :
                query = f'SELECT password FROM users where username="{user}"'
                cr.execute(query)
                dbpass = cr.fetchone()
                # print(dbpass) => ('1234',)
                if dbpass[0] == password :
                    print("Login Success") 
                    self.placeholder.setText("")  
                else :
                    self.placeholder.setText("Invalid user name or password")
            except Exception as e :
                self.placeholder.setText("User Not Found")

class SignUP(QtWidgets.QDialog):
    def __init__(self):
        super(SignUP,self).__init__()
        loadUi(r'UI\createacc2.ui',self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.gotoprofile)
        
    
    def gotoprofile(self):
        user = self.emailfield.text().strip()
        password = self.passwordfield.text().strip()
        cpassword = self.confirmpasswordfield.text().strip()
        
        if len(user) == 0 or len(password) == 0 or (cpassword) == 0 :
            self.placeholder.setText('Please Fill All Fields')
        elif password != cpassword :
            self.placeholder.setText("Password doesn't Match")
        else:
            try :
                conn = sqlite3.connect('data.db')
                cur = conn.cursor()
                user_info = [user,password]
                
                # Add to data base
                cur.execute("insert into users (username,password) values (?,?)",user_info)

                conn.commit()
                conn.close()
            
                self.placeholder.setText('')
                print('Login Success')
                
                qpp = Profile()
                widget.addWidget(qpp)
                widget.setCurrentIndex(widget.currentIndex()+1)
            except Exception as e :
                self.placeholder.setText("User name is not available")

class Profile(QtWidgets.QDialog):
    def __init__(self):
        super(Profile,self).__init__()
        loadUi(r'UI\app.ui',self)


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
widget.setCurrentIndex(0)

# display the widget
widget.show()

# Launch the application => Main Loop
app.exec_()