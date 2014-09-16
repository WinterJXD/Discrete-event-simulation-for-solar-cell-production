# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 18:00:48 2014

@author: rnaber
"""

from __future__ import division
from PyQt4 import QtGui

class ConnectionSettingsDialog(QtGui.QDialog):
    def __init__(self, _parent, _batchconnection):
        super(QtGui.QDialog, self).__init__(_parent)
        # create dialog screen for changing two connection parameters
        
        self.parent = _parent
        self.batchconnection = _batchconnection
        self.setWindowTitle(self.tr("Available settings"))
        vbox = QtGui.QVBoxLayout()

        title_label = QtGui.QLabel(self.tr("Edit settings:"))
        vbox.addWidget(title_label)             
        
        hbox = QtGui.QHBoxLayout()
        label = QtGui.QLabel("transport_time")
        self.spinbox0 = QtGui.QSpinBox()
        self.spinbox0.setAccelerated(True)
        self.spinbox0.setMaximum(999999999)
        self.spinbox0.setValue(self.batchconnection[2])
        self.spinbox0.setObjectName("Time for one transport")
        if (self.batchconnection[2] >= 100):
            self.spinbox0.setSingleStep(100)
        elif (self.batchconnection[2] >= 10):
            self.spinbox0.setSingleStep(10) 
        hbox.addWidget(label)
        hbox.addWidget(self.spinbox0)  
        vbox.addLayout(hbox)

        hbox = QtGui.QHBoxLayout()
        label = QtGui.QLabel("time_per_unit")
        self.spinbox1 = QtGui.QSpinBox()
        self.spinbox1.setAccelerated(True)
        self.spinbox1.setMaximum(999999999)
        self.spinbox1.setValue(self.batchconnection[3])
        self.spinbox1.setObjectName("Time added for each added batch")
        if (self.batchconnection[3] >= 100):
            self.spinbox1.setSingleStep(100)
        elif (self.batchconnection[3] >= 10):
            self.spinbox1.setSingleStep(10) 
        hbox.addWidget(label)
        hbox.addWidget(self.spinbox1)  
        vbox.addLayout(hbox)

        buttonbox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.read)
        buttonbox.rejected.connect(self.reject)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

    def read(self):
        # read contents of each widget
        # update settings in batchconnection
        self.batchconnection[2] = int(self.spinbox0.text())
        self.batchconnection[3] = int(self.spinbox1.text())        
        self.parent.statusBar().showMessage(self.tr("Connection settings updated"))
        self.accept()