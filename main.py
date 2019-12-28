#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
comment: 主函数

@author: @一直憨憨一直爽！@哈哈哈哈哈 @kgiu @GanAH @嗷呜不是喵呜！  2019/12/12.
@version 1.0.
@contact: 4564893112@qq.com
"""
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from window import window
from PyQt5.QtWidgets import QApplication, QMainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    # 界面重构存储区域
    ui = window.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())