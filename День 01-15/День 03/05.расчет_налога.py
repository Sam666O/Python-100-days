"""
Введите ежемесячный размер Вашей зарплаты и выплату по социальной страховке и в фонд, чтобы рассчитать
подоходный налог с населения.
Примечание: при написании этого кода новый метод расчета НДФЛ еще не выдавался.
Название файла '05.расчет_налога.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-11-04
"""

salary = float(input('Введите зарплату в этом месяце: '))
insurance = float(input('Введите выплату по страховке и фонд бедных котят: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1600:
    rate = 0.02
    deduction = 0
elif diff < 5500:
    rate = 0.13
    deduction = 127
elif diff < 8030:
    rate = 0.24
    deduction = 555
elif diff < 34500:
    rate = 0.28
    deduction = 1055
elif diff < 63000:
    rate = 0.42
    deduction = 2755
elif diff < 75000:
    rate = 0.32
    deduction = 3500
else:
    rate = 0.39
    deduction = 8500
tax = abs(diff * rate - deduction)
print('Подоходный налог с населения: %.2f рублей' % tax)
print('Фактический доход: %.2f рублей' % (diff + 3500 - tax))
