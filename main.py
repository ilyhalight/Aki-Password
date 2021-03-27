import os
import sys
import pymysql
import time
import json

import pymysql.cursors

from loguru import logger

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from ui.ui_splashscreen import Ui_Aki_splashscreen

from ui.ui_main import Ui_Aki_main

from ui.ui_sign import Ui_Aki_sign

# GLOBALS
path_config  = './config.json'

is_config_exists = os.path.isfile('./config.json')

if is_config_exists == True:
    pass
elif is_config_exists == False:
    logger.warning('Файл конфигурации не был найден')
    logger.info('Создаём файл конфигурации...')
    with open(path_config, 'a') as config_file:
        logger.info('Записываем базовые значения в файл конфигурации')
        config_file.write('{"db_host" : "localhost", "db_user" : "root", "db_password" : " ", "db_name" : "password_manager"}')
        logger.success('Файл конфигурации был успешно создан')
        config_file.close()

with open(path_config, 'r') as config_file:
    logger.info('Загрузка конфигов...')
    try:
        _config = json.load(config_file)
    except:
        logger.critical('Не удалось загрузить конфиг')
        logger.info('Закрытие приложения...')
    finally:
        logger.success('Конфиги закружены')


counter = 0
authorized = 0

logger.info('Подключаемся к базе данных')

connection = pymysql.connect(
                            host = _config['db_host'],
                            user = _config['db_user'],
                            password = _config['db_password'],
                            database = _config['db_name']
                            )

cursor = connection.cursor()
logger.success('Подключение к базе данных установлено')

# SIGN WINDOW
class SignWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Aki_sign()
        self.ui.setupUi(self)
        self.initUi()

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.background_main.mouseMoveEvent = moveWindow

        self.show()

    def initUi(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('Aki Password')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # HIDE ELEMENTS
        self.ui.notifications_terms_of_use_close.setIcon(QtGui.QIcon("ui/icons/aki_close_notify.png"))
        self.ui.notifications_close.setIcon(QtGui.QIcon("ui/icons/aki_close_notify.png"))
        self.ui.notifications_main_background.hide()
        self.ui.notifications_terms_of_use_background.hide()
        self.ui.notifications_dark_background.hide()

        # WIDGETS
        self.ui.sign_stackedWidget.setCurrentWidget(self.ui.auth_page)

        # MAIN FRAME
        self.ui.img_logo.setIcon(QtGui.QIcon("ui/icons/aki_logo.png"))
        self.ui.btn_close.setIcon(QtGui.QIcon("ui/icons/aki_close.png"))
        self.ui.aki_copyright.setText("Aki © 2021 Все права защищены")

        # REGISTER FRAME
        self.ui.reg_login_img.setIcon(QtGui.QIcon("ui/icons/aki_user.png"))
        self.ui.reg_email_img.setIcon(QtGui.QIcon("ui/icons/aki_email.png"))
        self.ui.reg_pass_img.setIcon(QtGui.QIcon("ui/icons/aki_password.png"))
        self.ui.reg_pass_img2.setIcon(QtGui.QIcon("ui/icons/aki_password.png"))

        # AUTH FRAME
        self.ui.auth_login_img.setIcon(QtGui.QIcon("ui/icons/aki_user.png"))
        self.ui.auth_pass_img.setIcon(QtGui.QIcon("ui/icons/aki_password.png"))

        # UI FUNCTIONS
        self.ui.btn_close.clicked.connect(self.minimize)
        self.ui.reg_auth_btn.clicked.connect(self.move_to_auth)
        self.ui.auth_reg_btn.clicked.connect(self.move_to_register)
        self.ui.auth_sign.clicked.connect(self.authorize)
        self.ui.reg_sign.clicked.connect(self.registration)
        self.ui.notifications_close.clicked.connect(self.notify_close)
        self.ui.notifications_terms_of_use_close.clicked.connect(self.notify_terms_close)
        self.ui.reg_conditions.clicked.connect(self.terms_of_use_show)
        self.ui.reg_terms_of_use.clicked.connect(self.terms_of_use_show)
        self.ui.reg_terms_of_use2.clicked.connect(self.terms_of_use_show)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def minimize(self):
        self.showMinimized()

    def move_to_auth(self):
        self.ui.sign_stackedWidget.setCurrentWidget(self.ui.auth_page)
        self.setWindowTitle('Aki Sign In')

    def move_to_register(self):
        self.ui.sign_stackedWidget.setCurrentWidget(self.ui.register_page)
        self.setWindowTitle('Aki Sign Up')

    def authorize(self):
        auth_login = self.ui.auth_login.text()
        auth_pass = self.ui.auth_pass.text()
        global authorized
        if len(auth_pass) < 5 or len(auth_login) < 4 or len(auth_login) > 20 or auth_login == '' or auth_pass == '':
            self.warn_notifications('Неверный логин или пароль.')
        else:
            sql = f"SELECT password FROM aki_accounts WHERE login = '{auth_login}'"
            try:
                cursor.execute(sql)
                sql_data = cursor.fetchall()
                for row in sql_data:
                    pass_sql = row[0]
                    if auth_pass == pass_sql:
                        authorized == 1
                        # SHOW MAIN WINDOW
                        self.main = MainWindow()
                        self.main.show()

                        # CLOSE SIGN WINDOW
                        self.close()
                    else:
                        self.warn_notifications('Неверный логин или пароль.')

            except:
                connection.rollback()
                self.warn_notifications('Произошла неизвестная ошибка.')

    def registration(self):
        reg_login = self.ui.reg_login.text()
        reg_email = self.ui.reg_email.text()
        reg_pass = self.ui.reg_pass.text()
        reg_pass_2 = self.ui.reg_pass_2.text()
        if len(reg_pass) <= 4:
            self.warn_notifications('Введенный пароль слишком короткий.')
        elif len(reg_login) < 4:
            self.warn_notifications('Введенный логин слишком короткий.')
        elif len(reg_login) > 20:
            self.warn_notifications('Введенный логин не может быть больше 20 символов.')
        elif reg_pass != reg_pass_2:
            self.warn_notifications('Введенные пароли не совпадают.')
        else:
            if self.ui.reg_terms_of_use_check.isChecked():
                if '@' in reg_email:
                    sql = "INSERT INTO aki_accounts (login, password, email) VALUES (%s, %s, %s)"
                    try:
                        cursor.execute(sql, (f'{reg_login}', f'{reg_pass}', f'{reg_email}'))
                        connection.commit()
                        self.notifications('Успех.', 'Вы успешно зарегистрировались')
                        self.move_to_auth()
                    except:
                        connection.rollback()
                        self.warn_notifications('Произошла неизвестная ошибка.')
                else:
                    self.warn_notifications('Укажите ваш реальный E-mail.')
            else:
                self.warn_notifications('Для продолжения необходимо согласиться с условиями и политикой конфеденциальности.')

    def warn_notifications(self, text = "Произошла серверная ошибка. Попробуйте ещё раз"):
        self.ui.notifications_dark_background.show()
        self.ui.notifications_main_background.show()
        self.ui.notifications_up.setStyleSheet("QFrame {\n"
"    background-color: rgb(230, 52, 98);\n"
"    border:  None;\n"
"    border-radius: 10px;\n"
"}")
        self.ui.notifications_oops_text.setText('Упс! Мы столкнулись с некоторыми проблемами.')
        self.ui.notifications_text.setText(text)

    def notifications(self, text = 'Тестовое уведомление', message = "Вы успешно получили уведомление"):
        self.ui.notifications_dark_background.show()
        self.ui.notifications_main_background.show()
        self.ui.notifications_up.setStyleSheet("QFrame {\n"
"    background-color: rgb(95, 229, 50);\n"
"    border:  None;\n"
"    border-radius: 10px;\n"
"}")
        self.ui.notifications_oops_text.setText(text)
        self.ui.notifications_text.setText(message)


    def notify_close(self):
        self.ui.notifications_dark_background.hide()
        self.ui.notifications_main_background.hide()

    def notify_terms_close(self):
        self.ui.notifications_dark_background.hide()
        self.ui.notifications_terms_of_use_background.hide()

    def terms_of_use_show(self):
        self.ui.notifications_dark_background.show()
        self.ui.notifications_terms_of_use_background.show()

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Aki_main()
        self.ui.setupUi(self)
        self.initUi()

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.background_main.mouseMoveEvent = moveWindow

    def initUi(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('Aki Password')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MAIN FRAME

        self.ui.img_logo.setIcon(QtGui.QIcon("ui/icons/aki_logo.png"))
        self.ui.btn_close.setIcon(QtGui.QIcon("ui/icons/aki_close.png"))
        self.ui.main_window_copyright.setText("Aki © 2021 Все права защищены")

        self.ui.btn_delete_user.setIcon(QtGui.QIcon("ui/icons/aki_delete.png"))
        self.ui.btn_copy_data.setIcon(QtGui.QIcon("ui/icons/aki_copy.png"))

        self.ui.frame.hide()

        item = self.ui.tableWidget.item(0, 0)
        item.setText('Sitename')
        item = self.ui.tableWidget.item(0, 1)
        item.setText('Username')
        item = self.ui.tableWidget.item(0, 2)
        item.setText('Password')

        # UI FUNCTIONS
        self.ui.btn_close.clicked.connect(self.minimize)
        self.ui.reg_cancel.clicked.connect(self.hide_reg)
        self.ui.btn_add_user.clicked.connect(self.open_reg)
        self.ui.reg_sign.clicked.connect(self.add_user_to_table)

    def add_user_to_table(self):
        site_name = self.ui.new_site_name.text()
        site_user = self.ui.new_site_user.text()
        site_pass = self.ui.new_site_pass.text()

        if len(site_pass) < 5 or len(site_user) < 4:
            print('Введенный логин или пароль слишком короткий.')
        elif len(site_user) > 32:
            print('Логин не может быть больше 32 символов.')
        elif len(site_name) > 255:
            print('Адрес сайта не может быть больше 255 символов.')
        elif len(site_pass) > 255:
            print('Пароль не может быть больше 255 символов.')
        else:
            print('42')

    def hide_reg(self):
        self.ui.frame.hide()

    def open_reg(self):
        self.ui.frame.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def minimize(self):
        self.showMinimized()

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Aki_splashscreen()
        self.ui.setupUi(self)
        self.initUi()

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.ss_background.mouseMoveEvent = moveWindow

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    def initUi(self):
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('Loading...')
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MAIN FRAME

        self.ui.ss_copyright.setText("Aki © 2021 Все права защищены")

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.ss_background.setGraphicsEffect(self.shadow)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.ss_label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        #QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.ss_label_description.setText("<strong>LOADING</strong> COMMANDS"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.ss_label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.ss_progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            if authorized == 1:
                # SHOW MAIN WINDOW
                self.main = MainWindow()
                self.main.show()
            else:
                self.sign = SignWindow()
                self.sign.show()
            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())