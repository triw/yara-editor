# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yaraeditor.ui'
#
# Created: Sun Dec  2 10:30:50 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_YaraEditor(object):
    def setupUi(self, YaraEditor):
        YaraEditor.setObjectName(_fromUtf8("YaraEditor"))
        YaraEditor.resize(1117, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/images/logo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        YaraEditor.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(YaraEditor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.MainWidget = QtGui.QWidget(self.centralwidget)
        self.MainWidget.setObjectName(_fromUtf8("MainWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.MainWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widgetEditor = QtGui.QWidget(self.MainWidget)
        self.widgetEditor.setObjectName(_fromUtf8("widgetEditor"))
        self.horizontalLayout.addWidget(self.widgetEditor)
        self.verticalLayout.addWidget(self.MainWidget)
        self.widgetOutput = QtGui.QWidget(self.centralwidget)
        self.widgetOutput.setMaximumSize(QtCore.QSize(16777215, 110))
        self.widgetOutput.setObjectName(_fromUtf8("widgetOutput"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widgetOutput)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.outputEdit = QtGui.QTextEdit(self.widgetOutput)
        self.outputEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.outputEdit.setReadOnly(True)
        self.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        self.horizontalLayout_2.addWidget(self.outputEdit)
        self.verticalLayout.addWidget(self.widgetOutput)
        YaraEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(YaraEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        YaraEditor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(YaraEditor)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        YaraEditor.setStatusBar(self.statusbar)
        self.dockWidgetYara = QtGui.QDockWidget(YaraEditor)
        self.dockWidgetYara.setMinimumSize(QtCore.QSize(300, 208))
        self.dockWidgetYara.setObjectName(_fromUtf8("dockWidgetYara"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.widgetYara = QtGui.QWidget(self.dockWidgetContents)
        self.widgetYara.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetYara.setObjectName(_fromUtf8("widgetYara"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widgetYara)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widgetYara)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.pathYara = QtGui.QLineEdit(self.widgetYara)
        self.pathYara.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pathYara.setReadOnly(False)
        self.pathYara.setObjectName(_fromUtf8("pathYara"))
        self.verticalLayout_2.addWidget(self.pathYara)
        self.yaraTree = QtGui.QTreeView(self.widgetYara)
        self.yaraTree.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.yaraTree.setObjectName(_fromUtf8("yaraTree"))
        self.verticalLayout_2.addWidget(self.yaraTree)
        self.verticalLayout_5.addWidget(self.widgetYara)
        self.dockWidgetYara.setWidget(self.dockWidgetContents)
        YaraEditor.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetYara)
        self.dockWidgetMalware = QtGui.QDockWidget(YaraEditor)
        self.dockWidgetMalware.setMinimumSize(QtCore.QSize(310, 231))
        self.dockWidgetMalware.setObjectName(_fromUtf8("dockWidgetMalware"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widgetMalware = QtGui.QWidget(self.dockWidgetContents_2)
        self.widgetMalware.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetMalware.setObjectName(_fromUtf8("widgetMalware"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetMalware)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.widgetMalware)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.pathMalware = QtGui.QLineEdit(self.widgetMalware)
        self.pathMalware.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pathMalware.setReadOnly(False)
        self.pathMalware.setObjectName(_fromUtf8("pathMalware"))
        self.verticalLayout_3.addWidget(self.pathMalware)
        self.malwareTree = QtGui.QTreeView(self.widgetMalware)
        self.malwareTree.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.malwareTree.setObjectName(_fromUtf8("malwareTree"))
        self.verticalLayout_3.addWidget(self.malwareTree)
        self.verticalLayout_4.addWidget(self.widgetMalware)
        self.dockWidgetMalware.setWidget(self.dockWidgetContents_2)
        YaraEditor.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetMalware)
        self.dockWidgetInspector = QtGui.QDockWidget(YaraEditor)
        self.dockWidgetInspector.setObjectName(_fromUtf8("dockWidgetInspector"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents_4)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_properties = QtGui.QWidget()
        self.tab_properties.setObjectName(_fromUtf8("tab_properties"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_properties)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.treeMalwareProperties = QtGui.QTreeWidget(self.tab_properties)
        self.treeMalwareProperties.setObjectName(_fromUtf8("treeMalwareProperties"))
        self.verticalLayout_8.addWidget(self.treeMalwareProperties)
        self.tabWidget.addTab(self.tab_properties, _fromUtf8(""))
        self.tab_strings = QtGui.QWidget()
        self.tab_strings.setObjectName(_fromUtf8("tab_strings"))


        self.tabWidget.addTab(self.tab_strings, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.dockWidgetInspector.setWidget(self.dockWidgetContents_4)
        YaraEditor.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetInspector)
        self.actionNouveau = QtGui.QAction(YaraEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/images/win/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNouveau.setIcon(icon1)
        self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
        self.actionExit = QtGui.QAction(YaraEditor)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionEnregistrer = QtGui.QAction(YaraEditor)
        self.actionEnregistrer.setObjectName(_fromUtf8("actionEnregistrer"))

        self.retranslateUi(YaraEditor)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(YaraEditor)

    def retranslateUi(self, YaraEditor):
        YaraEditor.setWindowTitle(QtGui.QApplication.translate("YaraEditor", "Yara-Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("YaraEditor", "Yara Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("YaraEditor", "Malware Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.treeMalwareProperties.headerItem().setText(0, QtGui.QApplication.translate("YaraEditor", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeMalwareProperties.headerItem().setText(1, QtGui.QApplication.translate("YaraEditor", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_properties), QtGui.QApplication.translate("YaraEditor", "Tab Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_strings), QtGui.QApplication.translate("YaraEditor", "Strings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNouveau.setText(QtGui.QApplication.translate("YaraEditor", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNouveau.setShortcut(QtGui.QApplication.translate("YaraEditor", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("YaraEditor", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("YaraEditor", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer.setText(QtGui.QApplication.translate("YaraEditor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer.setShortcut(QtGui.QApplication.translate("YaraEditor", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))

import yaraeditor_rc
