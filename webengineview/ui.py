#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDesktopWidget


class UIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.JavascriptEnabled, True)
        self.channel = QWebChannel(self.webView.page())
        self.webView.page().setWebChannel(self.channel)
        layout = QVBoxLayout()
        layout.addWidget(self.webView)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.resize(900, 600)
        self.setWindowTitle('Qics QWebEngineView')
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.show()
        html_path = QtCore.QUrl.fromLocalFile(QDir.currentPath() + "/assets/index.html")
        self.webView.load(html_path)


