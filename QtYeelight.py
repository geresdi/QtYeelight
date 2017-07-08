import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QGroupBox
from PyQt5.QtGui import QIcon
from YeelightControl import YeelightControl as y

 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.yeelight = y()
        self._discovered = False
        self._connected = False
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('PyQt5 Yeelight control')
        self.setGeometry(0, 0, 640, 480)
        self.setWindowIcon(QIcon('yeelight.png'))
        self.createlayout()        
        self.discoverbutton.clicked.connect(self.discover_click)
        self.connectbutton.clicked.connect(self.connect_click)
        '''
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,20)
        self.textbox.setReadOnly(True)
        '''
        self.show()
    
    def createlayout(self):
        self.ipbox = QLabel(self)
        self.refreshbox = QLabel(self)
        self.idbox = QLabel(self)
        self.modelbox = QLabel(self)
        self.versionbox = QLabel(self)
        self.discoverbutton = QPushButton('Discover', self)
        self.discoverbutton.setToolTip('Discover Yeelight device')
        self.connectbutton = QPushButton('Connect', self)
        self.connectbutton.setToolTip('Connect to the discovered Yeelight device')
        self.connectbutton.setEnabled(False)
        self.boxgroup = QGroupBox()

        self.ipbox.setText('IP address and port: ')
        self.refreshbox.setText('Refresh rate: ')
        self.modelbox.setText('Yeelight model: ')
        self.idbox.setText('Lamp ID: ')
        self.versionbox.setText('Firmware version: ')
        
        layout = QVBoxLayout()
        layout.addWidget(self.discoverbutton)
        layout.addWidget(self.connectbutton)
        layout.addWidget(self.ipbox)
        layout.addWidget(self.refreshbox)
        layout.addWidget(self.modelbox)
        layout.addWidget(self.idbox)
        layout.addWidget(self.versionbox)
        self.setLayout(layout)

    def discover_click(self):
        if self.yeelight.discover():
            self._discovered = True
            self.ipbox.setText('IP address and port: '+ self.yeelight.ip + ':' + str(self.yeelight.port))
            self.refreshbox.setText('Refresh rate: ' + str(self.yeelight.refresh) + ' s')
            self.modelbox.setText('Yeelight model: ' + self.yeelight.model)
            self.idbox.setText('Lamp ID: ' + str(self.yeelight.id))
            self.versionbox.setText('Firmware version: ' + str(self.yeelight.version))
            self.connectbutton.setEnabled(True)
        else:
            self.connectbutton.setEnabled(False)
            
    def connect_click(self):
        if not self._connected:
            if self.yeelight.connect():
                self.connectbutton.setText('Disconnect')
                self.connectbutton.setToolTip('Disconnect from the Yeelight device')
        else:
            if self.yeelight.disconnect():
                self.connectbutton.setText('Connect')
                self.connectbutton.setToolTip('Connect to the discovered Yeelight device')    

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())