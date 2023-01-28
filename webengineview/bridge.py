#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore


class JsBridge(QtCore.QObject):
    @QtCore.pyqtSlot(str, result=str)
    def test(self, message):
        print(message)
        return "ok"
