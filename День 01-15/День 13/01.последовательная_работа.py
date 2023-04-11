"""
Python 3.10 Эта прогррама показывает (имитирует) выполнение нескольких последовательных задач загрузки,
идущих одна за одной. Иммитация потому, что на самом деле ничего не загружается, а время загрузки генерируется
случайно модулем `random` функцией генерации целых чисел `randint`
Название файла '01.последовательная_работа.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-10
"""

from random import randint  # подключаем функцию генерации целых чисел
from time import time, sleep  # подключаем модуль работы со временем


def download_task(filename):  # функция-имитация загрузки файла (на входе имя файла)
    print('Начать загрузку %s...' % filename)  # перед загрузкой выводим сообщение на экран
    time_to_download = randint(5, 10)  # генерация случайного числа от 5 до 10
    sleep(time_to_download)  # ждем это случайное время
    print('Загрузка завершена! Потребовалось %d секунд' % time_to_download)  # выводим сообщение с отображением времени


def main():  # главная функция
    start = time()  # учитываем время начала программы, значение присваеиваем переменной
    download_task('Django.pdf')  # запускаем функцию загрузки файла Django.pdf
    download_task('PyTorch.epub')  # запускаем функцию загрузки файла PyTorch.epub
    end = time()  # учитываем время конца программы, значение присваеиваем переменной
    print('Всего заняло% .2f секунд.' % (end - start))  # сообщение о окончании с вычислением общего времени загрузки


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
