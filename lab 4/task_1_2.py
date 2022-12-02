from task_1 import sort_quik
from task_1 import sort_ras
import timeit

mas = [5, 8, 2, 4, 9, 1, 7, 6, 3]

answ = input("Какую сортировку вы предпочитаете? (быстрая - 1, расчёска - 2): ")
while (answ != '1') and (answ != '2'):
    answ = input("Некорректный ввод! Введите 1 для быстрой сортировки, 2 - для сортировки расчёской")
if answ == '1':
    start = timeit.default_timer()
    sort_quik(mas)
    end = timeit.default_timer()
else:
    start = timeit.default_timer()
    sort_ras(mas)
    end = timeit.default_timer()


tm = end - start

print(tm)
