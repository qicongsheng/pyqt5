#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from ui import UIWindow
from bridge import JsBridge
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_window = UIWindow()
    js_bridge = JsBridge(ui_window.webView)
    ui_window.channel.registerObject('Bridge', JsBridge())
    sys.exit(app.exec_())
