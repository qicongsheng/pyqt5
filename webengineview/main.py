#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from ui import UIWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = UIWindow()
    sys.exit(app.exec_())
