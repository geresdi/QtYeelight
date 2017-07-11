import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, 
                             QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox,
                             QSlider)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
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
        self.setGeometry(320, 240, 320, 240)
        self.setWindowIcon(QIcon('yeelight.png'))
        self.createlayout()        
        self.discoverbutton.clicked.connect(self.discover_click)
        self.connectbutton.clicked.connect(self.connect_click)
        self.togglebutton.clicked.connect(self.toggle_click)
        self.powerbutton.clicked[bool].connect(self.power_click)
        self.brightslider.valueChanged[int].connect(self.bright_changed)
        self.ctslider.valueChanged[int].connect(self.ct_changed)
        self.rslider.valueChanged[int].connect(self.rgb_changed)
        self.gslider.valueChanged[int].connect(self.rgb_changed)
        self.bslider.valueChanged[int].connect(self.rgb_changed)
        
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
        self.togglebutton = QPushButton('Toggle', self)
        self.togglebutton.setToolTip('Toggle power state')
        self.togglebutton.setEnabled(False)
        self.powerbutton = QPushButton('Turn on')
        self.powerbutton.setEnabled(False)
        self.powerbutton.setCheckable(True)
        
        self.brightlabel = QLabel(self)
        self.brightlabel.setText('Brightness: ')
        self.brightlabel.setToolTip('Range 1 to 100, only enabled if power is on')
        self.brightslider = QSlider(Qt.Horizontal, self)
        self.brightslider.setMinimum(1)
        self.brightslider.setMaximum(100)
        self.brightslider.setValue(1)
        self.brightslider.setEnabled(False)
        self.brightslider.setToolTip('Range 1 to 100, only enabled if power is on')
        brightlayout = QHBoxLayout()
        brightlayout.addWidget(self.brightlabel)
        brightlayout.addWidget(self.brightslider)

        self.ctlabel = QLabel(self)
        self.ctlabel.setText('Color temperature: ')
        self.ctlabel.setToolTip('Range 1700 to 6500, only enabled if power is on')
        self.ctslider = QSlider(Qt.Horizontal, self)
        self.ctslider.setMinimum(1700)
        self.ctslider.setMaximum(6500)
        self.ctslider.setValue(1700)
        self.ctslider.setEnabled(False)
        self.ctslider.setToolTip('Range 1700 to 6500, only enabled if power is on')
        ctlayout = QHBoxLayout()
        ctlayout.addWidget(self.ctlabel)
        ctlayout.addWidget(self.ctslider)
        
        self.rgblabel = QLabel(self)
        self.rgblabel.setText('RGB color settings')
        
        self.rlabel = QLabel(self)
        self.rlabel.setText('Red component: ')
        self.rlabel.setToolTip('Range 0 to 255, only enabled if power is on')
        self.rslider = QSlider(Qt.Horizontal, self)
        self.rslider.setMinimum(0)
        self.rslider.setMaximum(255)
        self.rslider.setValue(0)
        self.rslider.setEnabled(False)
        self.rslider.setToolTip('Range 0 to 255, only enabled if power is on')
        rlayout = QHBoxLayout()
        rlayout.addWidget(self.rlabel)
        rlayout.addWidget(self.rslider)

        self.glabel = QLabel(self)
        self.glabel.setText('Green component: ')
        self.glabel.setToolTip('Range 0 to 255, only enabled if power is on')
        self.gslider = QSlider(Qt.Horizontal, self)
        self.gslider.setMinimum(0)
        self.gslider.setMaximum(255)
        self.gslider.setValue(0)
        self.gslider.setEnabled(False)
        self.gslider.setToolTip('Range 0 to 255, only enabled if power is on')
        glayout = QHBoxLayout()
        glayout.addWidget(self.glabel)
        glayout.addWidget(self.gslider)
        
        self.blabel = QLabel(self)
        self.blabel.setText('Blue component: ')
        self.blabel.setToolTip('Range 0 to 255, only enabled if power is on')
        self.bslider = QSlider(Qt.Horizontal, self)
        self.bslider.setMinimum(0)
        self.bslider.setMaximum(255)
        self.bslider.setValue(0)
        self.bslider.setEnabled(False)
        self.bslider.setToolTip('Range 0 to 255, only enabled if power is on')
        blayout = QHBoxLayout()
        blayout.addWidget(self.blabel)
        blayout.addWidget(self.bslider)
        

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
        layout.addWidget(self.togglebutton)
        layout.addWidget(self.powerbutton)
        layout.addLayout(brightlayout)
        layout.addLayout(ctlayout)
        layout.addWidget(self.rgblabel)
        layout.addLayout(rlayout)
        layout.addLayout(glayout)
        layout.addLayout(blayout)
        
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
                self.togglebutton.setEnabled(True)
                self.powerbutton.setEnabled(True)
                self._connected = True
        else:
            if self.yeelight.disconnect():
                self.connectbutton.setText('Connect')
                self.connectbutton.setToolTip('Connect to the discovered Yeelight device') 
                self.togglebutton.setEnabled(False)
                self.powerbutton.setEnabled(False) 
                self._connected = False  

    def toggle_click(self):
        self.yeelight.toggle()
        self.powerbutton.setChecked(not self.powerbutton.isChecked())
        if self.powerbutton.isChecked():
            self.powerbutton.setText('Turn off')
            self.brightslider.setEnabled(True)
            self.ctslider.setEnabled(True)
            self.rslider.setEnabled(True)
            self.gslider.setEnabled(True)
            self.bslider.setEnabled(True)
        else:
            self.powerbutton.setText('Turn on')
            self.brightslider.setEnabled(False)
            self.ctslider.setEnabled(False)
            self.rslider.setEnabled(False)
            self.gslider.setEnabled(False)
            self.bslider.setEnabled(False)
        
    def power_click(self, val):
        if val:
            self.yeelight.powered = True
            self.powerbutton.setText('Turn off')
            self.brightslider.setEnabled(True)
            self.ctslider.setEnabled(True)
            self.rslider.setEnabled(True)
            self.gslider.setEnabled(True)
            self.bslider.setEnabled(True)
        else:
            self.yeelight.powered = False
            self.powerbutton.setText('Turn on')
            self.brightslider.setEnabled(False)
            self.ctslider.setEnabled(False)
            self.rslider.setEnabled(True)
            self.gslider.setEnabled(True)
            self.bslider.setEnabled(True)
            
    def bright_changed(self, val):
        self.yeelight.brightness = val
        
    def ct_changed(self, val):
        self.yeelight.temperature = val
        
    def rgb_changed(self, val):
        self.yeelight.rgb = [self.rslider.value(), self.gslider.value(), self.bslider.value()]
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())