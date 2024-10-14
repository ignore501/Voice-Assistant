import sys      # Для доступа к командной строке
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication
from main import eva_run


# Наследуем класс от QMainWindow для настройки окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.the_button_is_checked = True

        self.setWindowTitle('EVA')      # Обучаемый голосовой ассистент

        button = QPushButton('Click Here!')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        # button.released.connect(self.the_button_was_released)
        # button.setChecked(self.the_button_is_checked)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print('CLICKED!')
        eva_run()

    def the_button_was_toggled(self, checked):
        # print('CHECKED?', checked)
        self.button_is_checked = checked

        # print(self.button_is_checked)

    # def the_button_was_released(self):
    #     self.button_is_checked = self.button.isChecked()


# Приложению нужен ТОЛЬКО один экземпляр QApplication
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не использовать аргументы командной строки,
# QApplication([]) тоже работает
app = QApplication(sys.argv)

# Создаем виджет QT - окно.
window = MainWindow()
window.show()       # ВАЖНО: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()


# Приложение не доберётся сюда, пока вы не выйдете и цикл
# событий не остановится.
