# -*- coding: utf-8 -*-

from PyQt6 import QtCore, QtGui, QtWidgets


class UiError(object):
    def setupUi(self, error):
        error.setObjectName("error")
        error.resize(400, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(error.sizePolicy().hasHeightForWidth())
        error.setSizePolicy(sizePolicy)
        error.setMinimumSize(QtCore.QSize(400, 240))
        error.setMaximumSize(QtCore.QSize(400, 240))
        self.error_label = QtWidgets.QLabel(error)
        self.error_label.setGeometry(QtCore.QRect(10, 10, 381, 131))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setItalic(False)
        self.error_label.setFont(font)
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.error_label.setObjectName("error_label")
        self.error_tip = QtWidgets.QLabel(error)
        self.error_tip.setGeometry(QtCore.QRect(0, 130, 401, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_tip.sizePolicy().hasHeightForWidth())
        self.error_tip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.error_tip.setFont(font)
        self.error_tip.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_tip.setObjectName("error_tip")

        self.retranslateUi(error)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "error"))
        self.error_label.setText(_translate("error", "ERROR!"))
        self.error_tip.setText(_translate("error", 'Please select one of the suggested answers and click the "Next" '
                                                   'button'))
