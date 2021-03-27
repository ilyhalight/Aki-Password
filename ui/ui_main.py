# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Aki_main(object):
    def setupUi(self, Aki_main):
        Aki_main.setObjectName("Aki_main")
        Aki_main.resize(961, 578)
        Aki_main.setStyleSheet("QMainWindow {\n"
"    border: none;\n"
"    border-radius: 25px\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Aki_main)
        self.centralwidget.setObjectName("centralwidget")
        self.background_main = QtWidgets.QFrame(self.centralwidget)
        self.background_main.setGeometry(QtCore.QRect(10, 10, 941, 561))
        self.background_main.setStyleSheet("QFrame {\n"
"    background-color:rgb(24, 24, 24);\n"
"    color:rgb(177, 177, 177);\n"
"    border-radius:  20px\n"
"}")
        self.background_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_main.setObjectName("background_main")
        self.poloska = QtWidgets.QFrame(self.background_main)
        self.poloska.setGeometry(QtCore.QRect(0, 50, 941, 1))
        self.poloska.setStyleSheet("QFrame {\n"
"    background-color:rgb(33, 33, 33);\n"
"}")
        self.poloska.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.poloska.setFrameShadow(QtWidgets.QFrame.Plain)
        self.poloska.setObjectName("poloska")
        self.btn_close = QtWidgets.QPushButton(self.background_main)
        self.btn_close.setGeometry(QtCore.QRect(910, 15, 16, 16))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    background: transparent\n"
"}")
        self.btn_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/aki_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QtCore.QSize(13, 13))
        self.btn_close.setObjectName("btn_close")
        self.img_logo = QtWidgets.QPushButton(self.background_main)
        self.img_logo.setGeometry(QtCore.QRect(20, 15, 24, 24))
        self.img_logo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.img_logo.setStyleSheet("QPushButton {\n"
"    background: transparent\n"
"}")
        self.img_logo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/aki_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.img_logo.setIcon(icon1)
        self.img_logo.setIconSize(QtCore.QSize(18, 18))
        self.img_logo.setObjectName("img_logo")
        self.logo_text = QtWidgets.QLabel(self.background_main)
        self.logo_text.setGeometry(QtCore.QRect(45, 20, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.logo_text.setFont(font)
        self.logo_text.setStyleSheet("QLabel {\n"
"    color: #fff\n"
"}")
        self.logo_text.setObjectName("logo_text")
        self.main_window_copyright = QtWidgets.QLabel(self.background_main)
        self.main_window_copyright.setGeometry(QtCore.QRect(40, 530, 851, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.main_window_copyright.setFont(font)
        self.main_window_copyright.setStyleSheet("")
        self.main_window_copyright.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.main_window_copyright.setObjectName("main_window_copyright")
        self.label = QtWidgets.QLabel(self.background_main)
        self.label.setGeometry(QtCore.QRect(46, 73, 881, 31))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.background_main)
        self.frame_3.setGeometry(QtCore.QRect(170, 110, 651, 423))
        self.frame_3.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(0, -10, 651, 423))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 177, 177, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tableWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Acrom")
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: transparent;\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: transparent;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: transparent;\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: transparent;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #fff;\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: transparent;\n"
"    max-width: 30px;\n"
"    border: 1px solid transparent;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid transparent;\n"
"    border-right: 1px solid transparent;\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: transparent;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid transparent;\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Acrom")
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Acrom")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Acrom")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Acrom")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Acrom")
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Acrom")
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Acrom")
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.btn_copy_pass = QtWidgets.QPushButton(self.frame_3)
        self.btn_copy_pass.setGeometry(QtCore.QRect(560, 30, 21, 21))
        self.btn_copy_pass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_pass.setStyleSheet("QPushButton {\n"
"    background: transparent\n"
"}")
        self.btn_copy_pass.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/aki_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_copy_pass.setIcon(icon2)
        self.btn_copy_pass.setObjectName("btn_copy_pass")
        self.btn_delete_user = QtWidgets.QPushButton(self.frame_3)
        self.btn_delete_user.setGeometry(QtCore.QRect(590, 30, 21, 21))
        self.btn_delete_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete_user.setToolTipDuration(-1)
        self.btn_delete_user.setStyleSheet("QPushButton {\n"
"    background: transparent\n"
"}")
        self.btn_delete_user.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/aki_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete_user.setIcon(icon3)
        self.btn_delete_user.setObjectName("btn_delete_user")
        self.btn_add_user = QtWidgets.QPushButton(self.frame_3)
        self.btn_add_user.setGeometry(QtCore.QRect(530, 360, 56, 56))
        self.btn_add_user.setMinimumSize(QtCore.QSize(56, 56))
        self.btn_add_user.setMaximumSize(QtCore.QSize(56, 56))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        font.setPointSize(56)
        self.btn_add_user.setFont(font)
        self.btn_add_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_user.setStyleSheet("QPushButton {\n"
"    border-radius: 26px;\n"
"    background-color: rgb(44, 49, 60);\n"
"    border: 5px solid rgb(39, 44, 54);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    color: #3ca24f\n"
"}")
        self.btn_add_user.setObjectName("btn_add_user")
        self.frame = QtWidgets.QFrame(self.background_main)
        self.frame.setGeometry(QtCore.QRect(80, 60, 741, 471))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color:rgba(24, 24, 24, 0.7);\n"
"    color:rgb(177, 177, 177);\n"
"    border-radius:  20px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 741, 41))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.new_site_name = QtWidgets.QLineEdit(self.frame)
        self.new_site_name.setGeometry(QtCore.QRect(230, 130, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        self.new_site_name.setFont(font)
        self.new_site_name.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: #0e0e0e;\n"
"    border-radius: 7px;\n"
"    color: #fff\n"
"}")
        self.new_site_name.setInputMask("")
        self.new_site_name.setObjectName("new_site_name")
        self.new_site_user = QtWidgets.QLineEdit(self.frame)
        self.new_site_user.setGeometry(QtCore.QRect(230, 210, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        self.new_site_user.setFont(font)
        self.new_site_user.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: #0e0e0e;\n"
"    border-radius: 7px;\n"
"    color: #fff\n"
"}")
        self.new_site_user.setInputMask("")
        self.new_site_user.setObjectName("new_site_user")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(230, 110, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(230, 190, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.new_site_pass = QtWidgets.QLineEdit(self.frame)
        self.new_site_pass.setGeometry(QtCore.QRect(230, 290, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        self.new_site_pass.setFont(font)
        self.new_site_pass.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    background-color: #0e0e0e;\n"
"    border-radius: 7px;\n"
"    color: #fff\n"
"}")
        self.new_site_pass.setInputMask("")
        self.new_site_pass.setObjectName("new_site_pass")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(230, 270, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.reg_sign = QtWidgets.QPushButton(self.frame)
        self.reg_sign.setGeometry(QtCore.QRect(230, 360, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        self.reg_sign.setFont(font)
        self.reg_sign.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reg_sign.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 10.5px;\n"
"    background-color: rgb(230, 52, 98)\n"
"}")
        self.reg_sign.setObjectName("reg_sign")
        self.reg_cancel = QtWidgets.QPushButton(self.frame)
        self.reg_cancel.setGeometry(QtCore.QRect(380, 360, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Acrom")
        self.reg_cancel.setFont(font)
        self.reg_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reg_cancel.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 10.5px;\n"
"    background-color: rgb(108, 109,112);\n"
"}")
        self.reg_cancel.setObjectName("reg_cancel")
        Aki_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Aki_main)
        QtCore.QMetaObject.connectSlotsByName(Aki_main)

    def retranslateUi(self, Aki_main):
        _translate = QtCore.QCoreApplication.translate
        Aki_main.setWindowTitle(_translate("Aki_main", "MainWindow"))
        self.logo_text.setText(_translate("Aki_main", "Aki"))
        self.main_window_copyright.setText(_translate("Aki_main", "Aki © 2021 Все права защищены"))
        self.label.setText(_translate("Aki_main", "СОХРАНЕННЫЕ ПАРОЛИ"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Aki_main", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Aki_main", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Aki_main", "Сайт"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Aki_main", "Имя пользователя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Aki_main", "Пароль"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Aki_main", "Site"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Aki_main", "User"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Aki_main", "Pass"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btn_add_user.setText(_translate("Aki_main", "+"))
        self.label_2.setText(_translate("Aki_main", "Создать новый логин"))
        self.new_site_name.setPlaceholderText(_translate("Aki_main", "https://www.example.com"))
        self.new_site_user.setPlaceholderText(_translate("Aki_main", "username"))
        self.label_3.setText(_translate("Aki_main", "Адрес веб-сайта"))
        self.label_4.setText(_translate("Aki_main", "Имя пользователя"))
        self.new_site_pass.setPlaceholderText(_translate("Aki_main", "password"))
        self.label_5.setText(_translate("Aki_main", "Пароль"))
        self.reg_sign.setText(_translate("Aki_main", "Сохранить"))
        self.reg_cancel.setText(_translate("Aki_main", "Отмена"))
