
def vvod_Matrizi(c):
    A = []
    s = input(c)
    while s != '':
        A.append(list(map(int, s.split())))
        s = input()
    return A

def transpon(A):
    B = []
    for i in range(len(A[0])):
        B.append(list(x[i] for x in A))
    return B

def umnog(A, B):
    if len(A[0]) != len(B):
        return 'Невозможно перемножить матрицы'
    C = []
    for i in range(len(A)):
        C.append([0]*len(B[0]))
    for t in range(len(C)):
        for o in range(len(C[0])):
            for y in range(len(B)):
                C[t][o] += A[t][y]*B[y][o]
    return C

def nol_vniz(A, x):
    r = [0 if A[t][x] == 0 else 1 for t in range(len(A))]
    if A[x][x] == 0 and sum(r[x+1:]) != 0:
        l = len(r) - 1
        while r[l] == 0:
            l -= 1
        A[x], A[l] = A[l], A[x]
    return A

def obnulenie(a, b, x):
    if a[x] == 0:
        return b
    else:
        z = b[x]
        for l in range(x, len(a)):
            b[l] = b[l] * a[x] - a[l] * z
    return b

def ne_nol_strok(A):
    return sum([0 if all(r == 0 for r in A[t]) else 1 for t in range(len(A))])

def rang(A):
    for i in range(min(len(A[0]), len(A) - 1)):
        A = nol_vniz(A, i)
        for t in range(i + 1, len(A)):
            A[t] = obnulenie(A[i], A[t], i)
    return ne_nol_strok(A)

def vivod_matr(B):
    for t in range(len(B)):
        print(*B[t])

A = vvod_Matrizi('Введите матрицу, если вы закончили, то нажмите ENTER \n')
print("Транспонированная матрица:")
vivod_matr(transpon(A))
print('Ранг матрицы:', rang(A))
print('Умножения двух матриц:')
vivod_matr(umnog(vvod_Matrizi('Введите матрицу 1, если вы закончили, то нажмите ENTER \n'),
                   vvod_Matrizi('Введите матрицу 2, если вы закончили, то нажмите ENTER \n')))