# -*- coding: utf-8 -*-

from PyQt6 import QtCore, QtGui, QtWidgets


class UiMainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(710, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainMenu.sizePolicy().hasHeightForWidth())
        MainMenu.setSizePolicy(sizePolicy)
        MainMenu.setMinimumSize(QtCore.QSize(710, 560))
        MainMenu.setMaximumSize(QtCore.QSize(710, 560))
        self.autor = QtWidgets.QLabel(MainMenu)
        self.autor.setGeometry(QtCore.QRect(540, 90, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.autor.setFont(font)
        self.autor.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.autor.setObjectName("autor")
        self.change_language_bt = QtWidgets.QPushButton(MainMenu)
        self.change_language_bt.setGeometry(QtCore.QRect(560, 10, 140, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_language_bt.sizePolicy().hasHeightForWidth())
        self.change_language_bt.setSizePolicy(sizePolicy)
        self.change_language_bt.setMinimumSize(QtCore.QSize(140, 30))
        self.change_language_bt.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.change_language_bt.setFont(font)
        self.change_language_bt.setObjectName("change_language_bt")
        self.start_bt = QtWidgets.QPushButton(MainMenu)
        self.start_bt.setGeometry(QtCore.QRect(270, 470, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setUnderline(False)
        self.start_bt.setFont(font)
        self.start_bt.setObjectName("start_bt")
        self.change_name_bt = QtWidgets.QPushButton(MainMenu)
        self.change_name_bt.setGeometry(QtCore.QRect(9, 9, 140, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_name_bt.sizePolicy().hasHeightForWidth())
        self.change_name_bt.setSizePolicy(sizePolicy)
        self.change_name_bt.setMinimumSize(QtCore.QSize(140, 30))
        self.change_name_bt.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.change_name_bt.setFont(font)
        self.change_name_bt.setObjectName("change_name_bt")
        self.title = QtWidgets.QLabel(MainMenu)
        self.title.setGeometry(QtCore.QRect(20, 50, 641, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("zagolovok")
        self.introduction = QtWidgets.QTextEdit(MainMenu)
        self.introduction.setGeometry(QtCore.QRect(100, 120, 511, 331))
        self.introduction.setObjectName("introduction")

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Myers-Briggs test"))
        self.autor.setText(_translate("MainMenu", "by Cyril Grinko"))
        self.change_language_bt.setText(_translate("MainMenu", "Change language"))
        self.start_bt.setText(_translate("MainMenu", "Start"))
        self.change_name_bt.setText(_translate("MainMenu", "Change name"))
        self.title.setText(_translate("MainMenu", "Myers — Briggs Type Indicator"))
        self.introduction.setHtml(_translate("MainMenu",
                                             '<!DOCTYPE html>'
                                             '<html><head><meta name="qrichtext" content="1" charset="utf-8"/><style '
                                             'type="text/css">'
                                             'p, li { white-space: pre-wrap; }'
                                             '</style></head><body style=" font-family:"Times New Roman"; '
                                             'font-size:14pt; '
                                             'font-weight:400; font-style:normal;">'
                                             "<p>This free personality test reveals who you really are. Discover the "
                                             "16 personalities created by Myers & Briggs,"
                                             "test your personality type, and find your strengths. Then 36 questions "
                                             "await you. Try to answer honestly and don't"
                                             "worry - the test results will be available to only you.</p>"
                                             "<p>Diagnostics of types according to the Myers - Briggs system is "
                                             "designed to determine one of 16 personality types. It includes 8 scales "
                                             "combined in pairs. The purpose of typology and tests is to help a "
                                             "person determine his individual preferences by establishing which poles "
                                             "of the scales correspond to him more.<br>"
                                             "1. Scale E—I - orientation of consciousness:<br>"
                                             "Е (Еxtraversion) — orientation of consciousness outward, towards "
                                             "objects,<br>"
                                             "I (Introversion) — orientation of consciousness inward, towards the "
                                             "subject;<br>"
                                             "2. Scale S—N — way of orientation in the situation:<br>"
                                             "S (Sensing) — orientation to material information,<br>"
                                             "N (iNtuition) — orientation to intuitive information;<br>"
                                             "3. Scale T—F — decision-making basis:<br>"
                                             "T (Thinking) — logical weighing of alternatives;<br>"
                                             "F (Feeling) — decision making on an emotional basis of ethics;<br>"
                                             "4. Scale J—P — way of preparing solutions:<br>"
                                             "J (Judging) — rational preference for planning and organizing "
                                             "information in advance,<br>"
                                             "P (Perception) — irrational preference to act without detailed "
                                             "preliminary preparation, more focusing on the circumstances.<br>"
                                             "The combination of scales gives the designation of one of 16 types, "
                                             "for example: ENTP, ISFJ, etc.</p>"))