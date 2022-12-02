from math import log2, ceil

A = list(map(float, input().split()))

def piramid_sort(A):
    if len(A) == 1: return A
    B = []
    ryad = ceil(log2(len(A) + 1))

    for m in range(ryad):
        B.append(A[:2**m])
        A = A[2**m:]
        
    for q in range(2**(ryad-1) - len(B[-1])): B[-1].append(-float('inf'))

    while B[0][0] != -float('inf'):
        for i in range(len(B) - 2, -1, -1):
            for t in range(len(B[i])):
                if B[i][t] < B[i + 1][t * 2]:
                    B[i][t], B[i + 1][t * 2] = B[i + 1][t * 2], B[i][t]
                if B[i][t] < B[i + 1][t * 2 + 1]:
                    B[i][t], B[i + 1][t * 2 + 1] = B[i + 1][t * 2 + 1], B[i][t]

        A.append(B[0][0])
        B[0][0] = -float('inf')

        for y in range(len(B[-1]) - 1, -1, -1):
            B[0][0], B[-1][y] = B[-1][y], B[0][0]
        if len(B) > 1 and max(B[-1]) == -float('inf'): B.pop(-1)
    return A[::-1]

print(piramid_sort(A))
