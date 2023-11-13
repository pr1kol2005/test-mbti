# -*- coding: utf-8 -*-

from PyQt6 import QtCore, QtGui, QtWidgets


class UiResultswindow(object):
    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResultsWindow.sizePolicy().hasHeightForWidth())
        ResultsWindow.setSizePolicy(sizePolicy)
        ResultsWindow.setMinimumSize(QtCore.QSize(1000, 800))
        ResultsWindow.setMaximumSize(QtCore.QSize(1000, 800))
        self.congrats = QtWidgets.QLabel(ResultsWindow)
        self.congrats.setGeometry(QtCore.QRect(0, 0, 891, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.congrats.setFont(font)
        self.congrats.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.congrats.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.congrats.setObjectName("congrats")
        self.pers_type = QtWidgets.QLabel(ResultsWindow)
        self.pers_type.setGeometry(QtCore.QRect(0, 60, 891, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pers_type.setFont(font)
        self.pers_type.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pers_type.setObjectName("pers_type")
        self.pers_name = QtWidgets.QLabel(ResultsWindow)
        self.pers_name.setGeometry(QtCore.QRect(0, 120, 891, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pers_name.setFont(font)
        self.pers_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pers_name.setObjectName("pers_name")
        self.pers_info = QtWidgets.QTextEdit(ResultsWindow)
        self.pers_info.setGeometry(QtCore.QRect(60, 180, 391, 601))
        self.pers_info.setObjectName("pers_info")
        self.again_bt = QtWidgets.QPushButton(ResultsWindow)
        self.again_bt.setGeometry(QtCore.QRect(480, 700, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.again_bt.setFont(font)
        self.again_bt.setObjectName("again_bt")
        self.change_lang_bt = QtWidgets.QPushButton(ResultsWindow)
        self.change_lang_bt.setGeometry(QtCore.QRect(800, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.change_lang_bt.setFont(font)
        self.change_lang_bt.setObjectName("change_lang_bt")

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("ResultsWindow", "Myers-Briggs test"))
        self.congrats.setText(_translate("ResultsWindow", "Поздравляем, nickname!"))
        self.pers_type.setText(_translate("ResultsWindow", "Вы personality_type"))
        self.pers_name.setText(_translate("ResultsWindow", "personality_name"))
        self.pers_info.setHtml(_translate("ResultsWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                                           "/><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'MS Shell Dlg "
                                                           "2\'; font-size:8.25pt; font-weight:400; "
                                                           "font-style:normal;\">\n"
                                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                           "-qt-block-indent:0; text-indent:0px;\"><br "
                                                           "/></p></body></html>"))
        self.again_bt.setText(_translate("ResultsWindow", "Начать заново"))
        self.change_lang_bt.setText(_translate("ResultsWindow", "Сменить язык"))
