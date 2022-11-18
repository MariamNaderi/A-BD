
#сложность O(nlogn)

def sliyanSort(A, B):
    C = []
    ia = 0
    ib = 0
    while ia < len(A) and ib < len(B):
        if A[ia] <= B[ib]:
            C.append(A[ia])
            ia += 1
        else:
            C.append(B[ib])
            ib += 1
    C += A[ia:]
    C += B[ib:]
    return C

def mainn(F):
    if len(F) == 1 or len(F) == 0:
        return F
    else:
        mid = (len(F)) // 2
        l = mainn(F[:mid])
        r = mainn(F[mid:])
        return sliyanSort(l, r)
