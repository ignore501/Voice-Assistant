import sys      # Для выхода из приложения
import speech_recognition as sr     # Перевод речи в текст
import pyttsx3      # Перевод текста в речь
from dialogflow_text import dialog_flow_answer
import keyboard
# Инициализация голоса
# Инициализируем модуль pyttsx3 и настраиваем голос,
# где rate - количество слов в минуту, volume - громкость (от 0 до 1).
# Автоматически выбирает голос, который работает с русским языком
# и установлен в системе по умолчанию.
eva = pyttsx3.init()
eva.setProperty('rate', 208)
eva.setProperty('volume', 1)

# Инициализация микрофона
recognizer = sr.Recognizer()
microphone = sr.Microphone()


def speak(what):    # Функция текст в голос, в параметр "what" передаем текст
    eva.say(what)
    eva.runAndWait()
    eva.stop()


def text_from_microphone():     # Функция распознования голоса
    # Запись микрофона
    with microphone as source:
        print('>> Я слушаю')
        recognizer.adjust_for_ambient_noise(source)
        # Слушаем только 5 секунд
        audio = recognizer.listen(source, phrase_time_limit=5)
        # Возвращаем текст, преобразуем с помощью Vosk (работает офлайн)
        recognized_txt = recognizer.recognize_vosk(audio, language='ru')
        print(recognized_txt)
        # print(recognized_txt)
        return recognized_txt


def try_again():
    print('>> Повторите, пожалуйста!')
    speak('Повторите, пожалуйста!')


def command_handler(text):      # Прослушивание команд
    if 'ева' in text:
        speak('Слушаю вас, мой господин')
        text = text_from_microphone()
    answer = dialog_flow_answer(text)
    if answer[0]:
        print(f'>> {answer[0]}')
        speak(answer[0])
    else:
        try_again()

    if answer[1] == 'smalltalk.greetings.bye':
        sys.exit()


# Основная функция работы
def eva_run():
    print('>> Обучаемый голосовой ассистент EVA <<')
    speak('Обучаемый голосовой ассистент ЕВА. Слушаю Вас')
    print('*' * 39)
    keyboard.wait('`')
    while True:
        try:
            command_handler(text_from_microphone().lower())
        except sr.UnknownValueError:
            try_again()
        print('*' * 39)


# eva_run()

# speak('Привет мир!')
