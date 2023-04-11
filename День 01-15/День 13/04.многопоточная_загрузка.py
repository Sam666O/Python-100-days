"""
Python 3.10 используем многопоточность где поток как объект класса
Название файла '04.многопоточная_загрузка.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-10
"""

import threading  # подключаем модуль многопоточной работы
from random import randint  # подключаем функцию генерации целых чисел
from time import time, sleep  # подключаем модуль работы со временем

class DownloadTask(threading.Thread):  # создаем класс

    def __init__(self, filename):  # инициализация класса
        super().__init__()
        self._filename = filename

    def run(self):  # метод выполнения
        print('Начать загрузку %s...' % self._filename)  # перед загрузкой выводим сообщение на экран
        time_to_download = randint(5, 10)  # генерация случайного числа от 5 до 10
        print('Оставшееся время %d секунд.' % time_to_download)  # выводим сообщение с отображением ост. времени
        sleep(time_to_download)  # ждем это случайное время
        print('%s загрузка завершена!' % self._filename)  # выводим сообщение с отображением имени файла


def main():  # главная функция
    start = time()  # время начала выполнения программы
    # Поместите несколько задач загрузки в несколько потоков для выполнения
    # . После запуска потока он обратится к нему и выполнит
    # метод run.
    thread1 = DownloadTask('Python.pdf')  # Создаем объект потока через собственный класс потока
    thread1.start()  # начало выполнения потока
    thread2 = DownloadTask('Peking.avi')  # Создаем объект потока через собственный класс потока
    thread2.start()  # начало выполнения потока
    thread1.join()  # ожидание выполнения
    thread2.join()  # ожидание выполнения
    end = time()  # время конца выполнения программы
    print('Всего потребовалось %.3f секунд..' % (end - start))  # сообщение о окончании с вычислением общего времени
    # загрузки


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию

# Обратите внимание, что потоки, созданные с помощью threading.Thread, по умолчанию не являются потоками демона
