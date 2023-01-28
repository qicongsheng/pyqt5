#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QObject, pyqtSlot, QUrl


class JsBridge(QtCore.QObject):
    def __int__(self, web_view):
        self.web_view = web_view

    # pyqtSlot，网络上大多将其翻译为槽。作用是接收网页发起的信号
    @pyqtSlot()
    def changeJsValueByPy(self):
        self.web_view.page().runJavaScript('defaulitValue="value from python"')

    # 注意pyqtSlot用于把该函数暴露给js可以调用
    @pyqtSlot()
    def callPy2JsByJs1(self):
        print('中间代理')
        self.pyCalljs('py呼叫js，收到请回答')

    def pyCalljs(self, msg):
        self.web_view.page().runJavaScript("pyCalljs('%s')" % msg, self.js_callback)
        print(msg)  # 查看参数

    # 回调函数，接收js返回的值
    def js_callback(self, result):
        QMessageBox.information(None, "提示", "来自js回复：{}".format(result))
        print(result)

    # 注意pyqtSlot用于把该函数暴露给js可以调用 result=str返回的值string
    @pyqtSlot(str, result=str)
    def jsCallpy(self, text):
        QMessageBox.information(None, "提示", "来自js消息：{}".format(text))
        return 'js,py收到消息'
