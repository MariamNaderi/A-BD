
#Сложность O(3logn)

def f(A, o):
    i = 0
    r = len(A)
    while i < r - 1:
        s = (r + i) // 2
        if o < A[s]:
            r = s
        else: i = s
    print(r)

f([8, 9, 40], 40)
f([8, 9, 40], 40)
f([8, 9, 40], 40)
