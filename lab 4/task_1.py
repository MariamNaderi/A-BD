import random

def sort_quik(lst):
    if len(lst) <= 1:
        return lst
    else:
        k = random.choice(lst)
        more = []
        less = []
        eq = []
        for i in lst:
            if i < k:
                less.append(i)
            elif i > k:
                more.append(i)
            else:
                eq.append(i)
        return sort_quik(less) + eq + sort_quik(more)


def sort_ras(lst):
    k = round(len(lst)/1.247) - 1
    while k >= 1:
        for i in range(len(lst) - k):
            if lst[i] > lst[i + k]:
                t = lst[i]
                lst[i] = lst[i + k]
                lst[i + k] = t
        if k == 1:
            break
        k = round((k + 1)/1.247) - 1
    return lst


def mainn():
    a = input("Введите числа: ")
    mas = []
    while a != '':
        mas.append(int(a))
        a = input()

    print(sort_ras(mas))
    print(sort_quik(mas))

mainn()
