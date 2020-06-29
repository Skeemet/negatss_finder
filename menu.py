# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\artETmétiers\_2e année\trad'ss\borgia\negatss_finder\menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(253, 226)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.UI_TEXT_POSITS = QtWidgets.QLabel(self.centralwidget)
        self.UI_TEXT_POSITS.setObjectName("UI_TEXT_POSITS")
        self.horizontalLayout.addWidget(self.UI_TEXT_POSITS)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.UI_TEXT_NEGATS = QtWidgets.QLabel(self.centralwidget)
        self.UI_TEXT_NEGATS.setObjectName("UI_TEXT_NEGATS")
        self.horizontalLayout_2.addWidget(self.UI_TEXT_NEGATS)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.UI_TEXT_TOTAL = QtWidgets.QLabel(self.centralwidget)
        self.UI_TEXT_TOTAL.setObjectName("UI_TEXT_TOTAL")
        self.horizontalLayout_3.addWidget(self.UI_TEXT_TOTAL)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.UI_BUTTON_FIND = QtWidgets.QPushButton(self.centralwidget)
        self.UI_BUTTON_FIND.setObjectName("UI_BUTTON_FIND")
        self.gridLayout.addWidget(self.UI_BUTTON_FIND, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 253, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Total posit\'ss"))
        self.UI_TEXT_POSITS.setText(_translate("MainWindow", "...."))
        self.label_2.setText(_translate("MainWindow", "Total négat\'ss"))
        self.UI_TEXT_NEGATS.setText(_translate("MainWindow", "...."))
        self.label_3.setText(_translate("MainWindow", "Total Borgia"))
        self.UI_TEXT_TOTAL.setText(_translate("MainWindow", "...."))
        self.UI_BUTTON_FIND.setText(_translate("MainWindow", "Recherche négat\'ss"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

