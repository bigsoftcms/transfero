# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/ui_dependencies.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Depend(object):
    def setupUi(self, Depend):
        Depend.setObjectName("Depend")
        Depend.resize(400, 395)
        self.Go_label = QtWidgets.QLabel(Depend)
        self.Go_label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Go_label.setFont(font)
        self.Go_label.setObjectName("Go_label")
        self.golang_state = QtWidgets.QLabel(Depend)
        self.golang_state.setGeometry(QtCore.QRect(230, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.golang_state.setFont(font)
        self.golang_state.setObjectName("golang_state")
        self.mtp_label = QtWidgets.QLabel(Depend)
        self.mtp_label.setGeometry(QtCore.QRect(20, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mtp_label.setFont(font)
        self.mtp_label.setObjectName("mtp_label")
        self.mtp_state = QtWidgets.QLabel(Depend)
        self.mtp_state.setGeometry(QtCore.QRect(230, 70, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mtp_state.setFont(font)
        self.mtp_state.setObjectName("mtp_state")
        self.gomtpfs_label = QtWidgets.QLabel(Depend)
        self.gomtpfs_label.setGeometry(QtCore.QRect(20, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gomtpfs_label.setFont(font)
        self.gomtpfs_label.setObjectName("gomtpfs_label")
        self.go_mtpfs_state = QtWidgets.QLabel(Depend)
        self.go_mtpfs_state.setGeometry(QtCore.QRect(230, 120, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.go_mtpfs_state.setFont(font)
        self.go_mtpfs_state.setObjectName("go_mtpfs_state")
        self.check_window = QtWidgets.QCheckBox(Depend)
        self.check_window.setGeometry(QtCore.QRect(10, 360, 221, 22))
        self.check_window.setObjectName("check_window")
        self.jmtpfs_label = QtWidgets.QLabel(Depend)
        self.jmtpfs_label.setGeometry(QtCore.QRect(20, 170, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jmtpfs_label.setFont(font)
        self.jmtpfs_label.setObjectName("jmtpfs_label")
        self.jmtpfs_state = QtWidgets.QLabel(Depend)
        self.jmtpfs_state.setGeometry(QtCore.QRect(230, 170, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.jmtpfs_state.setFont(font)
        self.jmtpfs_state.setObjectName("jmtpfs_state")
        self.mtpfs_label = QtWidgets.QLabel(Depend)
        self.mtpfs_label.setGeometry(QtCore.QRect(20, 220, 91, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mtpfs_label.setFont(font)
        self.mtpfs_label.setObjectName("mtpfs_label")
        self.mtpfs_state = QtWidgets.QLabel(Depend)
        self.mtpfs_state.setGeometry(QtCore.QRect(230, 220, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mtpfs_state.setFont(font)
        self.mtpfs_state.setObjectName("mtpfs_state")
        self.label = QtWidgets.QLabel(Depend)
        self.label.setGeometry(QtCore.QRect(10, 300, 371, 18))
        self.label.setObjectName("label")
        self.check_libraries = QtWidgets.QPushButton(Depend)
        self.check_libraries.setGeometry(QtCore.QRect(263, 350, 111, 28))
        self.check_libraries.setObjectName("check_libraries")

        self.retranslateUi(Depend)
        QtCore.QMetaObject.connectSlotsByName(Depend)

    def retranslateUi(self, Depend):
        _translate = QtCore.QCoreApplication.translate
        Depend.setWindowTitle(_translate("Depend", "Dependencies"))
        self.Go_label.setText(_translate("Depend", "Golang-Go"))
        self.golang_state.setText(_translate("Depend", "TextLabel"))
        self.mtp_label.setText(_translate("Depend", "mtp-tools"))
        self.mtp_state.setText(_translate("Depend", "TextLabel"))
        self.gomtpfs_label.setText(_translate("Depend", "Go-mtpfs"))
        self.go_mtpfs_state.setText(_translate("Depend", "TextLabel"))
        self.check_window.setText(_translate("Depend", "Don\'t show this window again."))
        self.jmtpfs_label.setText(_translate("Depend", "Jmtpfs"))
        self.jmtpfs_state.setText(_translate("Depend", "TextLabel"))
        self.mtpfs_label.setText(_translate("Depend", "Mtpfs"))
        self.mtpfs_state.setText(_translate("Depend", "TextLabel"))
        self.label.setText(_translate("Depend", "Please, install all these requiered libraries for correct work"))
        self.check_libraries.setText(_translate("Depend", "Check Libraries"))
