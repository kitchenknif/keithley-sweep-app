# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Mar 25 01:58:37 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(611, 478)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.keithleyPortOpenButton = QtGui.QPushButton(self.tab)
        self.keithleyPortOpenButton.setObjectName(_fromUtf8("keithleyPortOpenButton"))
        self.gridLayout_2.addWidget(self.keithleyPortOpenButton, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.keithleyPortCloseButton = QtGui.QPushButton(self.tab)
        self.keithleyPortCloseButton.setEnabled(False)
        self.keithleyPortCloseButton.setObjectName(_fromUtf8("keithleyPortCloseButton"))
        self.gridLayout_2.addWidget(self.keithleyPortCloseButton, 1, 2, 1, 1)
        self.keithleyPortLabel = QtGui.QLabel(self.tab)
        self.keithleyPortLabel.setObjectName(_fromUtf8("keithleyPortLabel"))
        self.gridLayout_2.addWidget(self.keithleyPortLabel, 1, 3, 1, 1)
        self.keithleyPortEdit = QtGui.QLineEdit(self.tab)
        self.keithleyPortEdit.setObjectName(_fromUtf8("keithleyPortEdit"))
        self.gridLayout_2.addWidget(self.keithleyPortEdit, 1, 0, 1, 1)
        self.lddThermoPortEdit = QtGui.QLineEdit(self.tab)
        self.lddThermoPortEdit.setObjectName(_fromUtf8("lddThermoPortEdit"))
        self.gridLayout_2.addWidget(self.lddThermoPortEdit, 3, 0, 1, 1)
        self.lddThemroPortOpenButton = QtGui.QPushButton(self.tab)
        self.lddThemroPortOpenButton.setObjectName(_fromUtf8("lddThemroPortOpenButton"))
        self.gridLayout_2.addWidget(self.lddThemroPortOpenButton, 3, 1, 1, 1)
        self.lddThemroPortCloseButton = QtGui.QPushButton(self.tab)
        self.lddThemroPortCloseButton.setEnabled(False)
        self.lddThemroPortCloseButton.setObjectName(_fromUtf8("lddThemroPortCloseButton"))
        self.gridLayout_2.addWidget(self.lddThemroPortCloseButton, 3, 2, 1, 1)
        self.lddThermoLabel = QtGui.QLabel(self.tab)
        self.lddThermoLabel.setObjectName(_fromUtf8("lddThermoLabel"))
        self.gridLayout_2.addWidget(self.lddThermoLabel, 3, 3, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.measureTab = QtGui.QWidget()
        self.measureTab.setEnabled(False)
        self.measureTab.setObjectName(_fromUtf8("measureTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.measureTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.measurementButton = QtGui.QPushButton(self.measureTab)
        self.measurementButton.setObjectName(_fromUtf8("measurementButton"))
        self.horizontalLayout.addWidget(self.measurementButton)
        self.saveButton = QtGui.QPushButton(self.measureTab)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.clearDataButton = QtGui.QPushButton(self.measureTab)
        self.clearDataButton.setObjectName(_fromUtf8("clearDataButton"))
        self.horizontalLayout.addWidget(self.clearDataButton)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.frame = QtGui.QFrame(self.measureTab)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_7 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.currentLimitSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.currentLimitSpinBox.setDecimals(6)
        self.currentLimitSpinBox.setMaximum(9999.99)
        self.currentLimitSpinBox.setProperty("value", 1.0)
        self.currentLimitSpinBox.setObjectName(_fromUtf8("currentLimitSpinBox"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.FieldRole, self.currentLimitSpinBox)
        self.currentRangeSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.currentRangeSpinBox.setDecimals(6)
        self.currentRangeSpinBox.setMaximum(9999.99)
        self.currentRangeSpinBox.setProperty("value", 0.01)
        self.currentRangeSpinBox.setObjectName(_fromUtf8("currentRangeSpinBox"))
        self.formLayout_7.setWidget(2, QtGui.QFormLayout.FieldRole, self.currentRangeSpinBox)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_17)
        self.twoWireRadio = QtGui.QRadioButton(self.groupBox_3)
        self.twoWireRadio.setChecked(True)
        self.twoWireRadio.setObjectName(_fromUtf8("twoWireRadio"))
        self.senseType = QtGui.QButtonGroup(MainWindow)
        self.senseType.setObjectName(_fromUtf8("senseType"))
        self.senseType.addButton(self.twoWireRadio)
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.twoWireRadio)
        self.fourWireRadio = QtGui.QRadioButton(self.groupBox_3)
        self.fourWireRadio.setObjectName(_fromUtf8("fourWireRadio"))
        self.senseType.addButton(self.fourWireRadio)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.fourWireRadio)
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_19)
        self.numberOfSamplesSpinBox = QtGui.QSpinBox(self.groupBox_3)
        self.numberOfSamplesSpinBox.setMinimum(1)
        self.numberOfSamplesSpinBox.setProperty("value", 3)
        self.numberOfSamplesSpinBox.setObjectName(_fromUtf8("numberOfSamplesSpinBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.numberOfSamplesSpinBox)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.frame)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout_5 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_21 = QtGui.QLabel(self.groupBox_4)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_21)
        self.delayBetweenPointsCheckbox = QtGui.QDoubleSpinBox(self.groupBox_4)
        self.delayBetweenPointsCheckbox.setMinimum(0.1)
        self.delayBetweenPointsCheckbox.setProperty("value", 1.0)
        self.delayBetweenPointsCheckbox.setObjectName(_fromUtf8("delayBetweenPointsCheckbox"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.delayBetweenPointsCheckbox)
        self.legacySweepCheckbox = QtGui.QCheckBox(self.groupBox_4)
        self.legacySweepCheckbox.setObjectName(_fromUtf8("legacySweepCheckbox"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.legacySweepCheckbox)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.measureTab)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.frame_2)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_6 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.sweepStartVSpinEdit = QtGui.QDoubleSpinBox(self.groupBox)
        self.sweepStartVSpinEdit.setDecimals(6)
        self.sweepStartVSpinEdit.setMaximum(9999.99)
        self.sweepStartVSpinEdit.setProperty("value", 1e-05)
        self.sweepStartVSpinEdit.setObjectName(_fromUtf8("sweepStartVSpinEdit"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.sweepStartVSpinEdit)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.sweepEndSpinEdit = QtGui.QDoubleSpinBox(self.groupBox)
        self.sweepEndSpinEdit.setDecimals(6)
        self.sweepEndSpinEdit.setMaximum(9999.99)
        self.sweepEndSpinEdit.setProperty("value", 3.0)
        self.sweepEndSpinEdit.setObjectName(_fromUtf8("sweepEndSpinEdit"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.sweepEndSpinEdit)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.NumPointsSpinBox = QtGui.QSpinBox(self.groupBox)
        self.NumPointsSpinBox.setMinimum(1)
        self.NumPointsSpinBox.setMaximum(1000)
        self.NumPointsSpinBox.setProperty("value", 100)
        self.NumPointsSpinBox.setObjectName(_fromUtf8("NumPointsSpinBox"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.NumPointsSpinBox)
        self.LinearRadioButton = QtGui.QRadioButton(self.groupBox)
        self.LinearRadioButton.setChecked(True)
        self.LinearRadioButton.setObjectName(_fromUtf8("LinearRadioButton"))
        self.sweepShape = QtGui.QButtonGroup(MainWindow)
        self.sweepShape.setObjectName(_fromUtf8("sweepShape"))
        self.sweepShape.addButton(self.LinearRadioButton)
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.LabelRole, self.LinearRadioButton)
        self.LogRadioButton = QtGui.QRadioButton(self.groupBox)
        self.LogRadioButton.setCheckable(False)
        self.LogRadioButton.setChecked(False)
        self.LogRadioButton.setObjectName(_fromUtf8("LogRadioButton"))
        self.sweepShape.addButton(self.LogRadioButton)
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.FieldRole, self.LogRadioButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_5 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_5)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.dcRadioButton = QtGui.QRadioButton(self.groupBox_5)
        self.dcRadioButton.setChecked(True)
        self.dcRadioButton.setObjectName(_fromUtf8("dcRadioButton"))
        self.sweepType = QtGui.QButtonGroup(MainWindow)
        self.sweepType.setObjectName(_fromUtf8("sweepType"))
        self.sweepType.addButton(self.dcRadioButton)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.dcRadioButton)
        self.pulseRadioButton = QtGui.QRadioButton(self.groupBox_5)
        self.pulseRadioButton.setChecked(False)
        self.pulseRadioButton.setObjectName(_fromUtf8("pulseRadioButton"))
        self.sweepType.addButton(self.pulseRadioButton)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.pulseRadioButton)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(self.frame_2)
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.stackedWidget = QtGui.QStackedWidget(self.groupBox_6)
        self.stackedWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.dcPage = QtGui.QWidget()
        self.dcPage.setObjectName(_fromUtf8("dcPage"))
        self.formLayout_3 = QtGui.QFormLayout(self.dcPage)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.autoRangeCheckBox = QtGui.QCheckBox(self.dcPage)
        self.autoRangeCheckBox.setChecked(True)
        self.autoRangeCheckBox.setObjectName(_fromUtf8("autoRangeCheckBox"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.autoRangeCheckBox)
        self.label_12 = QtGui.QLabel(self.dcPage)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.stackedWidget.addWidget(self.dcPage)
        self.pulsePage = QtGui.QWidget()
        self.pulsePage.setObjectName(_fromUtf8("pulsePage"))
        self.formLayout_4 = QtGui.QFormLayout(self.pulsePage)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_13 = QtGui.QLabel(self.pulsePage)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtGui.QLabel(self.pulsePage)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtGui.QLabel(self.pulsePage)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_15)
        self.pulseWidthSpinEdit = QtGui.QDoubleSpinBox(self.pulsePage)
        self.pulseWidthSpinEdit.setMaximum(5.0)
        self.pulseWidthSpinEdit.setProperty("value", 5.0)
        self.pulseWidthSpinEdit.setObjectName(_fromUtf8("pulseWidthSpinEdit"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.pulseWidthSpinEdit)
        self.pulseDelaySpinEdit = QtGui.QDoubleSpinBox(self.pulsePage)
        self.pulseDelaySpinEdit.setMaximum(999.99)
        self.pulseDelaySpinEdit.setProperty("value", 200.0)
        self.pulseDelaySpinEdit.setObjectName(_fromUtf8("pulseDelaySpinEdit"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.pulseDelaySpinEdit)
        self.stackedWidget.addWidget(self.pulsePage)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.gridLayout_3.addWidget(self.frame_2, 1, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.measureTab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_3.addWidget(self.progressBar, 2, 1, 1, 1)
        self.tabWidget.addTab(self.measureTab, _fromUtf8(""))
        self.thermalTab = QtGui.QWidget()
        self.thermalTab.setEnabled(False)
        self.thermalTab.setObjectName(_fromUtf8("thermalTab"))
        self.tabWidget.addTab(self.thermalTab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Keithley Control Application", None))
        self.label.setText(_translate("MainWindow", "Keithely SourceMeter Port", None))
        self.label_3.setText(_translate("MainWindow", "LDD Port", None))
        self.keithleyPortOpenButton.setText(_translate("MainWindow", "Open Port", None))
        self.keithleyPortCloseButton.setText(_translate("MainWindow", "Close Port", None))
        self.keithleyPortLabel.setText(_translate("MainWindow", "Port Closed", None))
        self.keithleyPortEdit.setText(_translate("MainWindow", "COM3", None))
        self.lddThemroPortOpenButton.setText(_translate("MainWindow", "Open Port", None))
        self.lddThemroPortCloseButton.setText(_translate("MainWindow", "Close Port", None))
        self.lddThermoLabel.setText(_translate("MainWindow", "Port Closed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Connections", None))
        self.measurementButton.setText(_translate("MainWindow", "Start Measurement", None))
        self.saveButton.setText(_translate("MainWindow", "Save Measurement", None))
        self.clearDataButton.setText(_translate("MainWindow", "Clear", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Limits and Ranges", None))
        self.label_6.setText(_translate("MainWindow", "Current", None))
        self.label_5.setText(_translate("MainWindow", "Range, A", None))
        self.label_4.setText(_translate("MainWindow", "Limit, A", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Measurement Configuration", None))
        self.label_17.setText(_translate("MainWindow", "Sense Type", None))
        self.twoWireRadio.setText(_translate("MainWindow", "2 Wire", None))
        self.fourWireRadio.setText(_translate("MainWindow", "4 Wire", None))
        self.label_18.setText(_translate("MainWindow", "Averaging", None))
        self.label_19.setText(_translate("MainWindow", "Samples", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Other", None))
        self.label_21.setText(_translate("MainWindow", "Delay Between Points, sec", None))
        self.legacySweepCheckbox.setText(_translate("MainWindow", "Legacy Sweep", None))
        self.groupBox.setTitle(_translate("MainWindow", "General Sweep Characteristics", None))
        self.label_7.setText(_translate("MainWindow", "Sweep Start, V", None))
        self.label_8.setText(_translate("MainWindow", "Sweep End, V", None))
        self.label_9.setText(_translate("MainWindow", "Number of Points", None))
        self.LinearRadioButton.setText(_translate("MainWindow", "Linear Sweep", None))
        self.LogRadioButton.setText(_translate("MainWindow", "Logarithmic Sweep", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sweep type-specific Characteristics", None))
        self.dcRadioButton.setText(_translate("MainWindow", "DC Sweep", None))
        self.pulseRadioButton.setText(_translate("MainWindow", "Pulse Sweep", None))
        self.autoRangeCheckBox.setText(_translate("MainWindow", "Auto range", None))
        self.label_12.setText(_translate("MainWindow", "DC Sweep", None))
        self.label_13.setText(_translate("MainWindow", "Pulse Sweep", None))
        self.label_14.setText(_translate("MainWindow", "Pulse Width, ms", None))
        self.label_15.setText(_translate("MainWindow", "Pusle Delay, ms", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measureTab), _translate("MainWindow", "Measurements", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.thermalTab), _translate("MainWindow", "Thermal Control", None))

