from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QFile, QTextStream
from ui_main_menu import UiMainMenu
from ui_question import UiQuestionwindow
from ui_results import UiResultswindow
from ui_error import UiError
from random import shuffle
import sqlite3
import sys


NUM_QUESTIONS = 36  # Глобалая переменная - количество вопросов в тесте


class MainMenu(QWidget, UiMainMenu):
    """Класс окна главного меню"""
    def __init__(self):
        """Инициализация экземпляра класса"""
        super().__init__()
        self.setupUi(self)
        self.nickname, self.ok_pressed = QInputDialog.getText(self, "Welcome!", "What is your name?")
        if not self.ok_pressed or self.nickname == '':
            self.nickname = 'Anonymous'
        self.language = "en"
        self.change_name_bt.clicked.connect(self.change_name)
        self.change_language_bt.clicked.connect(self.change_language)
        self.show()

    def change_language(self):
        """Смена языка"""
        if self.language == 'en':
            self.language, self.ok_pressed1 = QInputDialog.getItem(self, "Hello!", "Choose your language",
                                                                   ("ru", "en"), 1, False)
        elif self.language == 'ru':
            self.language, self.ok_pressed1 = QInputDialog.getItem(self, "Привет!", "Выберите язык",
                                                                   ("ru", "en"), 1, False)
        if self.language == "en":
            self.change_name_bt.setText('Change name')
            self.change_language_bt.setText('Change language')
            self.start_bt.setText('Start')
            self.autor.setText('by Cyril Grinko')
            self.title.setText('Myers — Briggs Type Indicator')
            eng_menu = QFile("html/eng_menu.html")
            eng_menu.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
            istream = QTextStream(eng_menu)
            self.introduction.clear()
            self.introduction.setHtml(istream.readAll())
            eng_menu.close()
        elif self.language == "ru":
            self.change_name_bt.setText('Сменить имя')
            self.change_language_bt.setText('Сменить язык')
            self.start_bt.setText('Начать')
            self.autor.setText('сделано Кириллом Гринько')
            self.title.setText('Диагностика типов по системе Майерс — Бриггс')
            rus_menu = QFile("html/rus_menu.html")
            rus_menu.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
            istream = QTextStream(rus_menu)
            self.introduction.clear()
            self.introduction.setHtml(istream.readAll())
            rus_menu.close()

    def change_name(self):
        """Функция осуществаляет смену имени пользователя"""
        if self.language == 'en':
            temp_nickname, self.ok_pressed2 = QInputDialog.getText(self, f"Hello, {self.nickname}!",
                                                                   "Your new name:", QLineEdit.EchoMode.Normal,
                                                                   self.nickname)
        elif self.language == 'ru':
            temp_nickname, self.ok_pressed2 = QInputDialog.getText(self, f"Привет, {self.nickname}!",
                                                                   "Ваше новое имя:", QLineEdit.EchoMode.Normal,
                                                                   self.nickname)
        if self.ok_pressed2:
            if temp_nickname == '':
                self.nickname = 'Anonymous'
            else:
                self.nickname = temp_nickname


class QuestionWindow(QWidget, UiQuestionwindow):
    """Класс окна с вопросом теста"""
    def __init__(self, menu_window):
        """
        Иницализация элемента класса

        menu_window - экземпляр класс MainMenu
        """
        super().__init__()
        self.setupUi(self)
        self.menu_window = menu_window
        self.language = ''
        self.lst = [i for i in range(1, NUM_QUESTIONS + 1)]
        self.answers = [9 for i in range(NUM_QUESTIONS)]
        shuffle(self.lst)
        self.con = sqlite3.connect("db/mbti.db")
        self.cur = self.con.cursor()
        self.num = 0
        self.change_lang_bt.clicked.connect(lambda: self.change_language(True))
        self.proceed_bt.clicked.connect(lambda: self.next_question())
        self.back_bt.clicked.connect(lambda: self.previous_question())

    def open_window(self):
        """Открывается окошко с вопросом"""
        self.language = self.menu_window.language
        self.current_num.display(self.num + 1)
        self.change_language(False)
        self.num_of_questions.display(NUM_QUESTIONS)
        if self.language == 'en':
            self.question_text.setText(self.cur.execute("""SELECT questions.eng_text FROM questions
                                                WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])
        elif self.language == 'ru':
            self.question_text.setText(self.cur.execute("""SELECT questions.rus_text FROM questions
                                                WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])
        self.back_bt.setVisible(False)
        self.menu_window.hide()
        self.show()

    def change_language(self, window_was_opened):
        """
        Смена языка

        window_was_opened - было ли открыто окно
        """
        if window_was_opened:
            if self.language == 'en':
                self.language, self.ok_pressed1 = QInputDialog.getItem(self, "Hello!", "Choose your language",
                                                                       ("ru", "en"), 1, False)
            elif self.language == 'ru':
                self.language, self.ok_pressed1 = QInputDialog.getItem(self, "Привет!", "Выберите язык",
                                                                       ("ru", "en"), 1, False)
        if self.language == 'en':
            self.proceed_bt.setText('Next')
            self.change_lang_bt.setText('Change language')
            self.back_bt.setText('Back')
            self.rB1.setText('No')
            self.rB2.setText('Prob. not')
            self.rB3.setText('Prob. yes')
            self.rB4.setText('Yes')
            self.question_text.setText(self.cur.execute("""SELECT questions.eng_text FROM questions
                                                WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])
        elif self.language == 'ru':
            self.proceed_bt.setText('Далее')
            self.change_lang_bt.setText('Сменить язык')
            self.back_bt.setText('Назад')
            self.rB1.setText('Нет')
            self.rB2.setText('Скорее нет')
            self.rB3.setText('Скорее да')
            self.rB4.setText('Да')
            self.question_text.setText(self.cur.execute("""SELECT questions.rus_text FROM questions
                                                WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])

    def next_question(self):
        """Появляется текст следующего вопроса"""
        if (self.rB1.isChecked() is False and self.rB2.isChecked() is False and self.rB3.isChecked() is False and
                self.rB4.isChecked() is False):
            self.return_error()
        else:
            if self.rB1.isChecked():
                self.answers[self.num] = -1
            elif self.rB2.isChecked():
                self.answers[self.num] = -0.5
            elif self.rB3.isChecked():
                self.answers[self.num] = 0.5
            elif self.rB4.isChecked():
                self.answers[self.num] = 1
            if self.num == NUM_QUESTIONS - 1:
                self.result_window.open_window()
            else:
                self.num += 1
                if self.answers[self.num] == -1:
                    self.rB1.setChecked(True)
                elif self.answers[self.num] == -0.5:
                    self.rB2.setChecked(True)
                elif self.answers[self.num] == 0.5:
                    self.rB3.setChecked(True)
                elif self.answers[self.num] == 1:
                    self.rB4.setChecked(True)
                elif self.answers[self.num] == 9:
                    for btn in [self.rB1, self.rB2, self.rB3, self.rB4]:
                        btn.setAutoExclusive(False)
                        btn.setChecked(False)
                        btn.repaint()
                        btn.setAutoExclusive(True)
                self.back_bt.setVisible(True)
                if self.language == 'en':
                    self.question_text.setText(self.cur.execute("""SELECT questions.eng_text FROM questions
                                                        WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])
                elif self.language == 'ru':
                    self.question_text.setText(self.cur.execute("""SELECT questions.rus_text FROM questions
                                                        WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])
                self.current_num.display(self.num + 1)

    def previous_question(self):
        """Возвращение к предыдущему вопросу (вариант ответа сохраняется)"""
        self.num -= 1
        if self.answers[self.num] == -1:
            self.rB1.setChecked(True)
        if self.answers[self.num] == -0.5:
            self.rB2.setChecked(True)
        if self.answers[self.num] == 0.5:
            self.rB3.setChecked(True)
        if self.answers[self.num] == 1:
            self.rB4.setChecked(True)
        if self.num == 0:
            self.back_bt.setVisible(False)
        if self.language == 'en':
            self.question_text.setText(self.cur.execute("""SELECT questions.eng_text FROM questions
                                                WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])
        elif self.language == 'ru':
            self.question_text.setText(self.cur.execute("""SELECT questions.rus_text FROM questions
                                                WHERE id = ?""", (self.lst[self.num],)).fetchone()[0])
        self.current_num.display(self.num + 1)

    def return_error(self):
        """При попытке перехода к следующему вопросу без ответа вылезает ошибка"""
        ew = ErrorWindow(self.language)
        ew.exec()

    def add_res_win(self, res_win):
        """Функция принимает экземпляр класса ResultWindow и создает соответствующий атрибут"""
        self.result_window = res_win


class ResultsWindow(QWidget, UiResultswindow):
    """Класс окна с результатами"""
    def __init__(self, menu_window, question_window):
        """
        Инициализация экземпляра класса

        menu_window - экземпляр класс MainMenu
        question_window - экзмепляр класса QuestionWindow
        """
        super().__init__()
        self.setupUi(self)
        self.menu_window = menu_window
        self.question_window = question_window
        self.again_bt.clicked.connect(lambda: start(self.menu_window, self.question_window, self))
        self.change_lang_bt.clicked.connect(lambda: self.change_language(True))
        self.ei, self.sn, self.tf, self.jp = 0, 0, 0, 0
        self.type = ''

    def open_window(self):
        """Открытие окошка с результатами"""
        for i in range(len(self.question_window.lst)):
            ei1, sn1, tf1, jp1 = self.question_window.cur.execute("""SELECT questions.E_I, questions.S_N, questions.T_F, 
                                                                        questions.J_P FROM questions 
                                                                        WHERE id = ?""",
                                                                  (self.question_window.lst[i],)).fetchone()
            self.ei += ei1 * self.question_window.answers[i]
            self.sn += sn1 * self.question_window.answers[i]
            self.tf += tf1 * self.question_window.answers[i]
            self.jp += jp1 * self.question_window.answers[i]
        print(self.ei, self.sn, self.tf, self.jp)
        if self.ei <= 0:
            self.type = self.type + 'e'
        else:
            self.type = self.type + 'i'
        if self.sn <= 0:
            self.type = self.type + 's'
        else:
            self.type = self.type + 'n'
        if self.tf <= 0:
            self.type = self.type + 't'
        else:
            self.type = self.type + 'f'
        if self.jp <= 0:
            self.type = self.type + 'j'
        else:
            self.type = self.type + 'p'
        print(self.type)
        self.language = self.question_window.language
        self.nickname = self.menu_window.nickname
        self.eng_name, self.eng_description = self.question_window.cur.execute("""SELECT types.eng_nickname, 
                                                                        types.eng_description FROM types
                                                                        WHERE name = ?""",
                                                                               (self.type.upper(),)).fetchone()
        self.rus_name, self.rus_description = self.question_window.cur.execute("""SELECT types.rus_nickname, 
                                                                        types.rus_description FROM types
                                                                        WHERE name = ?""",
                                                                               (self.type.upper(),)).fetchone()
        self.change_language(False)
        self.pixmap = QPixmap(f'sprites/{self.type}.png')
        self.image = QLabel(self)
        self.image.move(480, 180)
        self.image.resize(500, 500)
        self.image.setPixmap(self.pixmap)
        self.question_window.hide()
        self.show()

    def change_language(self, window_was_opened):
        """
        Смена языка

        window_was_opened - было ли открыто окно
        """
        if window_was_opened:
            if self.language == 'en':
                self.language, self.ok_pressed1 = QInputDialog.getItem(self, "Hello!", "Choose your language",
                                                                       ("ru", "en"), 1, False)
            elif self.language == 'ru':
                self.language, self.ok_pressed1 = QInputDialog.getItem(self, "Привет!", "Выберите язык",
                                                                       ("ru", "en"), 1, False)
        if self.language == 'en':
            self.change_lang_bt.setText('Change language')
            self.congrats.setText(f'Congratulations, {self.nickname}!')
            self.pers_type.setText(f'You are {self.type.upper()}')
            self.pers_name.setText(self.eng_name)
            self.pers_info.setText(self.eng_description)
            self.pers_info.setFont(QFont('Times New Roman', 12))
            self.again_bt.setText('Complete test again')
        elif self.language == 'ru':
            self.change_lang_bt.setText('Сменить язык')
            self.congrats.setText(f'Поздравляем, {self.nickname}!')
            self.pers_type.setText(f'Вы {self.type.upper()}')
            self.pers_name.setText(self.rus_name)
            self.pers_info.setText(self.rus_description)
            self.pers_info.setFont(QFont('Times New Roman', 12))
            self.again_bt.setText('Начать тест заново')


class ErrorWindow(QDialog, UiError):
    """Класс окошка ошибки"""
    def __init__(self, language):
        """
        Инициализация экземпляра класса.

        language - текущий язык теста.
        """
        super().__init__()
        self.setupUi(self)
        self.error_tip.setWordWrap(True)
        if language == 'en':
            self.error_label.setText('ERROR!')
            self.error_tip.setText('Please select one of the suggested answers and click the "Next" button')
        elif language == 'ru':
            self.error_label.setText('ОШИБКА!')
            self.error_tip.setText('Выберите один из предложенных вариантов ответа и нажмите кнопку "Далее"')


def start(prev_main_menu=None, prev_quest_win=None, prev_results_win=None):
    """
    Функция создает экземпляры MainMenu, QuestionWindow, ResultsWindow и закрывает предыдущие окна, если они были.
    
    prev_main_menu - предыдущее открытое окно главного меню (по уолчанию None)
    prev_quest_win - предыдущее открытое окно с вопрсоом (по умолчанию None)
    prev_results_win - предыдущее открытое окно результатов (по умолчанию None)
    """
    if prev_main_menu is not None and prev_quest_win is not None and prev_results_win is not None:
        prev_main_menu.close()
        prev_quest_win.close()
        prev_results_win.close()
    mw = MainMenu()
    qw = QuestionWindow(mw)
    rw = ResultsWindow(mw, qw)
    qw.add_res_win(rw)
    mw.start_bt.clicked.connect(lambda: qw.open_window())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start()
    sys.exit(app.exec())
    