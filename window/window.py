# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
"""
comment:

@author1: @一直憨憨一直爽！@哈哈哈哈哈 @kgiu @GanAH @嗷呜不是喵呜！  2019/12/26.
@version 1.0.
@contact: 2361205625@qq.com/508044404@qq.com
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from splinter.browser import Browser
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_7.addWidget(self.line_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(13, 15, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_5.addWidget(self.line_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_user = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_user.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_user.setSizePolicy(sizePolicy)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.horizontalLayout.addWidget(self.lineEdit_user)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_passwd = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.lineEdit_passwd.setFont(font)
        self.lineEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.horizontalLayout_2.addWidget(self.lineEdit_passwd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_fromStation = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_fromStation.setObjectName("lineEdit_fromStation")
        self.horizontalLayout_3.addWidget(self.lineEdit_fromStation)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_targetStation = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_targetStation.setObjectName("lineEdit_targetStation")
        self.horizontalLayout_4.addWidget(self.lineEdit_targetStation)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.trainNumber = QtWidgets.QSpinBox(self.groupBox_2)
        self.trainNumber.setObjectName("trainNumber")
        self.horizontalLayout_6.addWidget(self.trainNumber)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_Time = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_Time.setReadOnly(True)
        self.lineEdit_Time.setObjectName("lineEdit_Time")
        self.horizontalLayout_5.addWidget(self.lineEdit_Time)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.tickit_type_conboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.tickit_type_conboBox.setObjectName("tickit_type_conboBox")
        self.tickit_type_conboBox.addItem("")
        self.tickit_type_conboBox.addItem("")
        self.tickit_type_conboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.tickit_type_conboBox)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.seat_comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.seat_comboBox.setObjectName("seat_comboBox")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.seat_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.seat_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.lineEdit_email = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_email.setCursorPosition(0)
        self.lineEdit_email.setDragEnabled(False)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_9.addWidget(self.lineEdit_email)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.lineEdit_emailpasswd = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_emailpasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_emailpasswd.setObjectName("lineEdit_emailpasswd")
        self.horizontalLayout_10.addWidget(self.lineEdit_emailpasswd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_5.addWidget(self.line_6)
        spacerItem1 = QtWidgets.QSpacerItem(371, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_11.addWidget(self.pushButton_2)
        self.button_go = QtWidgets.QPushButton(self.centralwidget)
        self.button_go.setIconSize(QtCore.QSize(180, 70))
        self.button_go.setAutoRepeat(False)
        self.button_go.setAutoExclusive(True)
        self.button_go.setObjectName("button_go")
        self.horizontalLayout_11.addWidget(self.button_go)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.timeLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.timeLCD.setObjectName("timeLCD")
        self.horizontalLayout_7.addWidget(self.timeLCD)
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setObjectName("dial")
        self.horizontalLayout_7.addWidget(self.dial)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setStyleSheet("font: 75 9pt \"Adobe Caslon Pro Bold\";")
        self.calendarWidget.setMaximumDate(QtCore.QDate(2020, 2, 29))
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_6.addWidget(self.calendarWidget)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(46)
        sizePolicy.setVerticalStretch(46)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("./source/loadi.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setWordWrap(False)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_12.addWidget(self.line_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.textEdit_statis = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_statis.setObjectName("textEdit_statis")
        self.verticalLayout.addWidget(self.textEdit_statis)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionh = QtWidgets.QAction(MainWindow)
        self.actionh.setObjectName("actionh")
        self.actionwhiua = QtWidgets.QAction(MainWindow)
        self.actionwhiua.setObjectName("actionwhiua")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.actioncomment = QtWidgets.QAction(MainWindow)
        self.actioncomment.setObjectName("actioncomment")
        self.actionout = QtWidgets.QAction(MainWindow)
        self.actionout.setObjectName("actionout")
        self.actionji = QtWidgets.QAction(MainWindow)
        self.actionji.setObjectName("actionji")
        self.menu.addAction(self.actionh)
        self.menu.addSeparator()
        self.menu.addAction(self.actionwhiua)
        self.menu.addAction(self.actionout)
        self.menu_2.addAction(self.actionhelp)
        self.menu_2.addAction(self.actionji)
        self.menu_3.addAction(self.actioncomment)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.buy_Ticket = Buy_Tickets()
        self.lineEdit_user.textEdited['QString'].connect(self.textEdit_statis.setText)
        self.trainNumber.valueChanged['QString'].connect(self.textEdit_statis.append)
        self.tickit_type_conboBox.currentIndexChanged['QString'].connect(self.textEdit_statis.append)
        self.seat_comboBox.currentTextChanged['QString'].connect(self.textEdit_statis.append)
        self.lineEdit_Time.textChanged['QString'].connect(self.textEdit_statis.append)
        self.calendarWidget.selectionChanged.connect(self.show_time)
        self.button_go.clicked.connect(self.buttonAction)
        # self.button_go.clicked.connect(self.timeLCD.value)
        self.buy_Ticket.infoEmit.connect(self.setTicketsInfo)
        self.dial.sliderMoved['int'].connect(self.timeLCD.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "12306自动化订票"))
        self.centralwidget.setWindowIcon(QtGui.QIcon("./source/logo.png"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">自动化订购车票</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">操作区</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "必选操作"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">账号:</p></body></html>"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "12306账户，不会储存及收集个人信息"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">密码:</p></body></html>"))
        self.lineEdit_passwd.setPlaceholderText(_translate("MainWindow", "12306密码"))
        self.label_4.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">始发站cookies:</p></body></html>"))
        self.lineEdit_fromStation.setPlaceholderText(_translate("MainWindow", "请咨询"))
        self.label_5.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">终点站cookies:</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>列车号：</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>乘车日期：</p></body></html>"))
        self.lineEdit_Time.setPlaceholderText(_translate("MainWindow", "点击右侧日历获取"))
        self.label_13.setText(_translate("MainWindow", "票型："))
        self.tickit_type_conboBox.setItemText(0, _translate("MainWindow", "看天意"))
        self.tickit_type_conboBox.setItemText(1, _translate("MainWindow", "成人票"))
        self.tickit_type_conboBox.setItemText(2, _translate("MainWindow", "学生票"))
        self.label_14.setText(_translate("MainWindow", "座次："))
        self.seat_comboBox.setItemText(0, _translate("MainWindow", "看天意"))
        self.seat_comboBox.setItemText(1, _translate("MainWindow", "商务座"))
        self.seat_comboBox.setItemText(2, _translate("MainWindow", "一等座"))
        self.seat_comboBox.setItemText(3, _translate("MainWindow", "硬卧"))
        self.seat_comboBox.setItemText(4, _translate("MainWindow", "二等座"))
        self.seat_comboBox.setItemText(5, _translate("MainWindow", "硬座"))
        self.seat_comboBox.setItemText(6, _translate("MainWindow", "软座"))
        self.seat_comboBox.setItemText(7, _translate("MainWindow", "软卧"))
        self.seat_comboBox.setItemText(8, _translate("MainWindow", "高级软卧"))
        self.seat_comboBox.setItemText(9, _translate("MainWindow", "动卧"))
        self.seat_comboBox.setItemText(10, _translate("MainWindow", "无座"))
        self.label_11.setText(_translate("MainWindow", "乘员信息[身份证无需填写，但要保证12306有注册信息]"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "乘员"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "身份证号"))
        self.groupBox.setTitle(_translate("MainWindow", "邮件通知【非必须】"))
        self.label_15.setText(_translate("MainWindow", "邮箱："))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "暂时支持QQ邮箱通知"))
        self.label_17.setText(_translate("MainWindow", "防伪码："))
        self.lineEdit_emailpasswd.setPlaceholderText(_translate("MainWindow", "QQ邮箱生成的授权码，无需密码！"))
        self.button_go.setText(_translate("MainWindow", "走你"))
        self.label_12.setText(_translate("MainWindow", "耗时:"))
        self.label_16.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">时间选择与监测</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "图表检测模块"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">网络监测</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">状态监测</p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "菜单(&F)"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.menu_3.setTitle(_translate("MainWindow", "版本信息(&I)"))
        self.actionh.setText(_translate("MainWindow", "参数"))
        self.actionwhiua.setText(_translate("MainWindow", "退出系统"))
        self.actionhelp.setText(_translate("MainWindow", "使用帮助(必看)"))
        self.actioncomment.setText(_translate("MainWindow", "版本检查更新(&A)"))
        self.actionout.setText(_translate("MainWindow", "out"))
        self.actionji.setText(_translate("MainWindow", "激活"))
        self._setTable()

    def _setTable(self):
        """
        # 表格初始化信息，设定初始cookies
        """
        for i in range(3):
            for j in range(2):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem("None"))
        self.lineEdit_fromStation.setText('%u6B66fgfdf%9%2FHH[示例cookies]')
        self.lineEdit_targetStation.setText('%u5dfgf7B81%2CDGH[示例cookies]')

    def show_time(self):
        """
        将用户点击的时间输出到对话框内

        :return: None
        """
        year = self.calendarWidget.selectedDate().year()
        month = self.calendarWidget.selectedDate().month()
        day = self.calendarWidget.selectedDate().day()
        timeText = str(year) + "-" + str(month).rjust(2, "0") + "-" + str(day).rjust(2, "0")
        self.textEdit_statis.append("乘车时间：")
        self.lineEdit_Time.setText(timeText)

    def timeCatch(self, year, month, day):
        """
        时间判断
        <p>判断所选时间与当前时间的大小，不能预定小于当前日期的车票
        :param year: 年
        :param month: 月
        :param day: 日
        :return: if Time selected bigger than now time  return True , else False
        """
        nowTime = datetime.datetime.now()
        nowYear = nowTime.year
        nowMonth = nowTime.month
        nowDay = nowTime.day
        if nowYear < 2019:
            return "系统时间错误，请配准系统时间：北京标准格里利时！"
        elif nowYear < year:
            return True
        elif nowYear == year:
            if nowMonth < month:
                return True
            elif nowMonth == month:
                if nowDay <= day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def setTicketsInfo(self, strInfo):
        """
        外部信息输出槽函数
        :param strInfo: str infomation
        :return: None
        """
        self.textEdit_statis.append(strInfo)

    def buttonAction(self):
        """
        按钮执行逻辑
        :return:
        """
        try:
            user = self.lineEdit_user.text().replace(" ", "")
            passwd = self.lineEdit_passwd.text().replace(" ", "")
            startStation = self.lineEdit_fromStation.text().replace(" ", "")
            endStation = self.lineEdit_targetStation.text().replace(" ", "")
            trainNumber = int(self.trainNumber.text())
            emailUser = self.lineEdit_email.text().replace(" ", "")
            emailPassword = self.lineEdit_emailpasswd.text().replace(" ", "")
            xb = [self.seat_comboBox.currentText()]
            pz = [self.tickit_type_conboBox.currentText()]
            trainTime = self.lineEdit_Time.text()

            if trainTime != "":
                timeList = trainTime.split("-")
                timeJudge = self.timeCatch(int(timeList[0]), int(timeList[1]), int(timeList[2]))
            else:
                self.showMsg("W", "时间未选择！")
            passengers = []
            for i in range(3):
                strPass = self.tableWidget.item(i, 0).text()
                # print(strPass)
                if strPass != "None":
                    passengers.append(strPass.replace(" ", ""))
            if user == "":
                self.showMsg("W", "警告，账户为空！")
            elif passwd == "":
                self.showMsg("W", "警告,密码为空！")
            elif timeJudge is not True:
                print(timeJudge)
                self.showMsg("W", "时间选择早于当天时刻！\n错误信息：" + str(timeJudge))
            elif startStation == "" or endStation == "":
                self.showMsg("W", "站点信息不全！")
            elif len(passengers) == 0:
                self.showMsg("W", "乘车人信息缺失！！")
            else:
                # 乘客名，比如passengers = ['XXX', 'XXX']
                # 学生票需注明，注明方式为：passengers = ['XXX(学生)', 'XXX']
                # 日期，格式为：'2018-01-20'
                # 出发地(需填写cookie值)
                """
                需要完善
                """
                if emailUser == "" and emailPassword == "":
                    reply = self.showMsg("I", "通知邮箱信息未添加，请确认返回填写(Yes)或忽略(No)？")
                    if reply == 65536:
                        self.buy_Ticket.setRequestData(user, passwd, trainNumber, passengers, trainTime, startStation,
                                                       endStation, xb,
                                                       pz)
                        a = self.buy_Ticket.start_buy()
                        self.textEdit_statis.append(a)
                    else:
                        self.textEdit_statis.append(
                            "<font color='red' size='6'><red>请按照指引添加通知邮箱！\n 帮助链接：https://未完成哦.com</font>")
                else:
                    self.buy_Ticket.setRequestData(user, passwd, trainNumber, passengers, trainTime, startStation,
                                                   endStation, xb,
                                                   pz)
                    a = self.buy_Ticket.start_buy()
                    self.textEdit_statis.append(a)
                    if a == "Get" and emailUser != "" and emailPassword != "":
                        self.mail(self)

        except Exception as eall:
            self.textEdit_statis.append("异常操作！可能中断执行，如遇暂停较久，请稍等片刻....\n")
            self.textEdit_statis.append("出错，错误信息：" + eall.args.__str__())
            self.showMsg("I", eall.args.__str__())

    def _setTicketInfo(selfuser, passwd, trainNumber, passengers, trainTime, startStation, endStation, xb,
                       pz):
        pass

    def showMsg(self, type, value):
        """
        弹窗提示
        :param type:
        :param value:
        :return:
        """
        try:  # 防止弹窗
            self.messageBox = QtWidgets.QMessageBox
            if type == "I":
                reply = self.messageBox.information(self.centralwidget, "【☠说༺༒༻明☠】", value,
                                                    self.messageBox.Yes | self.messageBox.No, self.messageBox.Yes)
                # print(reply)
                return reply
            elif type == "W":
                self.messageBox.warning(self.centralwidget, "【异常༺༒༻警告】", value)
            self.messageBox.show()
        except Exception:
            self.textEdit_statis.append("消息提示框操作提示：" + Exception.args.__str__())

    def mail(self, my_sender, my_passwd):
        """
        订票成功，短信通知
        :param my_sender:
        :param my_passwd:
        :return:
        """
        ret = True
        the_receiver = my_sender
        try:
            messageTheme = "12306Tickets 订票通知"
            messageText = "您的12306Tickets半自动订票任务成功，请于30分钟以内前往12306官网进行支付！"

            msg = MIMEText(messageText, 'plain', 'utf-8')
            msg['From'] = formataddr(["12306 Tickets", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["FK", the_receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = messageTheme  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [the_receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            self.textEdit_statis.append("邮件发送系统异常：" + e.args.__str__())
            ret = False
        if ret:
            return 1
        else:
            return 0


class Buy_Tickets(QtCore.QObject):
    infoEmit = QtCore.pyqtSignal(str)
    # 定义实例属性，初始化
    username = None
    passwd = None
    order = None
    passengers = None
    dtime = None
    starts = None
    ends = None
    xb = None
    pz = None

    def __init__(self):
        super(Buy_Tickets, self).__init__(parent=None)

        self.login_url = 'https://kyfw.12306.cn/otn/login/init'

        # self.initMy_url = 'https://kyfw.12306.cn/otn/index/initMy12306' # 个人中心
        self.initMy_url = 'https://kyfw.12306.cn/otn/view/index.html'  # 进入个人中心验证是否登录成功
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.driver_name = 'chrome'
        self.executable_path = './source/chromedriver.exe'

    def setRequestData(self, username, passwd, order, passengers, dtime, starts, ends, xb, pz):
        """
        适应信息发射绑定而作的无奈之举
        :param username: u
        :param passwd: 
        :param order: 
        :param passengers: 
        :param dtime: 
        :param starts: 
        :param ends: 
        :param xb: 
        :param pz: 
        :return: 
        """
        self.username = username
        self.passwd = passwd
        # 车次，0代表所有车次，依次从上到下，1代表所有车次，依次类推
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        self.xb = xb
        self.pz = pz

    # 登录功能实现
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill('loginUserDTO.user_name', self.username)
        # sleep(1)
        self.driver.fill('userDTO.password', self.passwd)
        # sleep(1)
        self.infoEmit.emit(str(datetime.datetime.now())+'请手动点击验证码登录...\n')

        while True:
            if self.driver.url != self.initMy_url:
                self.infoEmit.emit(str(datetime.datetime.now())+"登录验证：" + self.driver.url+"\n")
                sleep(1.2)
            else:
                self.infoEmit.emit("登录验证成功，手动操作部分完成，正在退出登录操作.\n即将进入自动订票，请稍后....\n")
                break

    # 买票功能实现
    def start_buy(self):
        try:

            self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
            # 窗口大小的操作
            self.driver.driver.set_window_size(700, 500)
            self.login()
            self.driver.visit(self.ticket_url)
            try:
                self.infoEmit.emit(str(datetime.datetime.now())+"——————开始进行购票——————\n")
                # 加载查询信息
                self.driver.cookies.add({"_jc_save_fromStation": self.starts})
                self.driver.cookies.add({"_jc_save_toStation": self.ends})
                self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
                self.driver.reload()
                count = 0
                if self.order != 0:
                    while self.driver.url == self.ticket_url:
                        self.driver.find_by_text('查询').click()
                        count += 1
                        self.infoEmit.emit('第%d次点击查询...\n' % count)
                        try:
                            self.driver.find_by_text('预订')[self.order - 1].click()
                            sleep(1.5)
                        except Exception as e:
                            print(e)
                            self.infoEmit.emit('预订失败...')
                            continue
                else:
                    while self.driver.url == self.ticket_url:
                        self.driver.find_by_text('查询').click()
                        count += 1
                        self.infoEmit.emit('第%d次点击查询...' % count)
                        try:
                            for i in self.driver.find_by_text('预订'):
                                i.click()
                                sleep(1)
                        except Exception as e:
                            self.infoEmit.emit(e)
                            self.infoEmit.emit('预订失败...')
                            continue
                self.infoEmit.emit('开始预订...')
                sleep(1)
                self.infoEmit.emit('开始选择用户...')
                for p in self.passengers:

                    self.driver.find_by_text(p).last.click()
                    sleep(0.5)
                    if p[-1] == ')':
                        self.driver.find_by_id('dialog_xsertcj_ok').click()
                self.infoEmit.emit('提交订单...')

                """
                # 毒案
                """
                sleep(1)
                if self.pz[0] != "看天意":
                    self.driver.find_by_text(self.pz).click()
                sleep(1)
                if self.xb[0] != "看天意":
                    self.driver.find_by_text(self.xb).click()
                sleep(1)

                self.driver.find_by_id('submitOrder_id').click()
                sleep(2)
                self.infoEmit.emit('确认选座...')
                self.driver.find_by_id('qr_submit_id').click()
                self.infoEmit.emit('预订成功!!')
                return "Get"
            except Exception as e:
                self.infoEmit.emit(e.args.__str__())

        except Exception as e:
            return e.args.__str__()
