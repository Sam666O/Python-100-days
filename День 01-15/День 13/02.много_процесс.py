"""
Python 3.10 Используйте класс Process для создания нескольких процессов
Название файла '02.много_процесс.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-04-11
"""

# Результат выполнения следующей программы может подтвердить, что родительский процесс скопировал процесс и его
# структуру данных при создании дочернего процесса
# Каждый процесс имеет собственное независимое пространство памяти, поэтому обмен данными между процессами может
# осуществляться только через IPC
import random   # подключаем функцию генерации целых чисел
from multiprocessing import Process, Queue, current_process  # работа с множеством процессов
from time import sleep  # функция ожидания


def sub_task(content, counts):  # функция выполнения задания (на входе 2 аргумента строка и число)
    print(f'PID: {current_process().pid}')  # выводим номер процесса
    counter = 0  # создаем переменную равную 0
    while counter < counts:  # цикл пока число меньше принятого аргумента (от 5 до 10 сгенир. ниже)
        counter += 1  # увеличиваем значение перемнной на 1
        print(f'{counter}: {content}')  # печать числа и строки
        sleep(0.01)  # время ожидания - сотая секунда


def main():  # главная функция
    number = random.randrange(5, 10)  # генерация случайного числа от 5 до 10 присваиваем переменной number
    Process(target=sub_task, args=('Ping', number)).start()  # создаем и запускаем процесс, указываем имя запускаемой
    # функции, а также передаваемые аргументы, строку и число
    Process(target=sub_task, args=('Pong', number)).start()  # создаем и запускаем процесс, указываем имя запускаемой
    # функции, а также передаваемые аргументы, строку и число


if __name__ == '__main__':  # если запущена это программа как главная
    main()  # запускаем главную функцию
