#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
from ui import UIWindow
from bridge import JsBridge
import sys
import os

if __name__ == '__main__':
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--foo-arg=foo-value --bar-arg=bar-value"
    app = QApplication(sys.argv)
    ui_window = UIWindow(title='qics Qt5 Demo', html="/assets/html/index.html")
    js_bridge = JsBridge(ui_window.webView)
    ui_window.channel.registerObject('JsBridge', js_bridge)
    sys.exit(app.exec_())
