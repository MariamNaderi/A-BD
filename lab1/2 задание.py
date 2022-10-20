import numpy as np

def vvod_Matrizi(с):
    A = []
    s = input(с)
    while s != '':
        A.append(list(map(int, s.split())))
        s = input()
    return np.array([l for l in A])

def tran(A):
    return A.transpose()

def umnog(A, B):
    return np.dot(A, B)

def rang(A):
    return np.linalg.matrix_rank(A)

A = vvod_Matrizi('Введите матрицу, если вы закончили, то нажмите ENTER \n')
print("Транспонированная матрица:")
print(tran(A))
print('Ранг матрицы:', rang(A))
print('Умножения двух матриц:')
print(umnog(vvod_Matrizi('Введите матрицу 1, если вы закончили, то нажмите ENTER \n'),
                   vvod_Matrizi('Введите матрицу 2, если вы закончили, то нажмите ENTER \n')))
