# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(400, 270)
        self.centralwidget = QtWidgets.QWidget(parent=OptionsWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 270))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(120, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.tbServer = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tbServer.setObjectName("tbServer")
        self.horizontalLayout_6.addWidget(self.tbServer)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_1.setMinimumSize(QtCore.QSize(120, 0))
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_1.addWidget(self.label_1)
        self.tbFolder = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tbFolder.setObjectName("tbFolder")
        self.horizontalLayout_1.addWidget(self.tbFolder)
        self.btBrowseFolder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btBrowseFolder.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btBrowseFolder.setObjectName("btBrowseFolder")
        self.horizontalLayout_1.addWidget(self.btBrowseFolder)
        self.horizontalLayout_1.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cbMoveFiles = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.cbMoveFiles.setObjectName("cbMoveFiles")
        self.horizontalLayout_2.addWidget(self.cbMoveFiles)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.tbUploadedFolder = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tbUploadedFolder.setObjectName("tbUploadedFolder")
        self.horizontalLayout_3.addWidget(self.tbUploadedFolder)
        self.btBrowseUploadedFolder = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btBrowseUploadedFolder.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btBrowseUploadedFolder.setObjectName("btBrowseUploadedFolder")
        self.horizontalLayout_3.addWidget(self.btBrowseUploadedFolder)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.cbAddStats = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.cbAddStats.setObjectName("cbAddStats")
        self.horizontalLayout_4.addWidget(self.cbAddStats)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btCancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btCancel.setMinimumSize(QtCore.QSize(100, 0))
        self.btCancel.setObjectName("btCancel")
        self.horizontalLayout_5.addWidget(self.btCancel)
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5.addWidget(self.widget_2)
        self.btSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btSave.setMinimumSize(QtCore.QSize(100, 0))
        self.btSave.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btSave.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btSave.setObjectName("btSave")
        self.horizontalLayout_5.addWidget(self.btSave)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout.setStretch(5, 1)
        OptionsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Options"))
        self.label_5.setText(_translate("OptionsWindow", "Server URL"))
        self.label_1.setText(_translate("OptionsWindow", "Folder"))
        self.btBrowseFolder.setText(_translate("OptionsWindow", "..."))
        self.cbMoveFiles.setText(_translate("OptionsWindow", "Move Files after Upload"))
        self.label_3.setText(_translate("OptionsWindow", "Uploaded Folder"))
        self.btBrowseUploadedFolder.setText(_translate("OptionsWindow", "..."))
        self.cbAddStats.setText(_translate("OptionsWindow", "Add Stats to Description"))
        self.btCancel.setText(_translate("OptionsWindow", "Cancel"))
        self.btSave.setText(_translate("OptionsWindow", "Save"))
