#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
comment:

@author1: GanAH  2019/12/26.
@author2: kgiu  2019/12/26.
@version 1.0.
@contact: 2361205625@qq.com/508044404@qq.com
"""
import sys,time
from PyQt5.QtCore import QThread, pyqtSignal


class timeThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super(timeThread, self).__init__()

    def run(self):
        t = 0
        time.sleep(1)
        t = t + 1
        self.trigger.emit(t)
