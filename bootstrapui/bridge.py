#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot


class JsBridge(QtCore.QObject):

    def __init__(self, web_view):
        super(JsBridge, self).__init__()
        self.web_view = web_view

    @pyqtSlot(str, result=str)
    def js_call_py(self, param):
        print("收到js传过来的值：%s" % param)
        # py_call_js
        self.web_view.page().runJavaScript('alert("python_call_js alert: hello,world！");')
        self.web_view.page().runJavaScript('pyCallJqueryFunc("msgDiv", "你好啊");')
        self.web_view.page().runJavaScript('pyCalljs("python_call_js pyCalljs: hello,hello！");', self.js_callback)
        return '我是python返回给js的值'

    # 回调函数，接收js返回的值
    def js_callback(self, result):
        print("js_callback: " + result)
