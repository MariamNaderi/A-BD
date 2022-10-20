import timeit
import numpy as np
np.set_printoptions (precision = 2)


def vvod_Matrizi(c):
    A = []
    s = input(c)
    while s != '':
        A.append(list(map(int, s.split())))
        s = input()
    return A

def my_code(p):
    start = timeit.default_timer()
    def vivod(A):
        for i in A:
            print(i)

    def transpon(A):
        B = []
        for i in range(len(A[0])):
            B.append(list(x[i] for x in A))
        return B

    def mini_mat(A, a, b):
        s = []
        for i in range(len(A)):
            for t in range(len(A[0])):
                if i != a and t != b:
                    s.append(A[i][t])
        return s

    def alg_dopol(A):
        A_souz = []
        for i in range(len(A)):
            m = []
            for t in range(len(A[0])):
                m.append(((-1)**(i+t))*det(mini_mat(A, i, t)))
            A_souz.append(m)
        return A_souz

    def det(A):
        if len(A) == 3:
            return A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] \
                   + A[1][0]*A[2][1]*A[0][2] - A[0][2]*A[1][1]*A[2][0] \
                   - A[0][1]*A[1][0]*A[2][2] - A[0][0]*A[1][2]*A[2][1]
        else:
            return A[0]*A[3] - A[1]*A[2]

    def delen(A, b):
        C = []
        for i in range(len(A)):
            C.append([0] * len(A[0]))
        for t in range(len(C)):
            for o in range(len(C[0])):
                C[t][o] = '{:.2f}'.format(A[t][o] / b)
        return C

    def obrat(A):
        if not det(A):
            return 'Определитель равен нулю, нельзя определить обратную матрицу'
        return delen(transpon(alg_dopol(A)), det(A))

    vivod(obrat(p))
    end = timeit.default_timer()
    print('Время работы кода:', '{:.10e}'.format((end - start)*((10)**(-3))), 'секунд \n')

def code_np(p):
    start2 = timeit.default_timer()
    def obratnay(A):
        return np.linalg.inv(A)
    print(obratnay(p))
    end2 = timeit.default_timer()
    print('Время работы кода:', '{:.10e}'.format((end2 - start2)*((10)**(-3))), 'секунд')

h = vvod_Matrizi('Введите матрицу, если вы закончили, то нажмите ENTER \n')
my_code(h)
code_np(h)
