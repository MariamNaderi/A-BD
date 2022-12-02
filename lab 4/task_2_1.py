
A = list(map(float, input().split()))


def bloch_sort(A):
    if len(A) == 1:
        return [A[0]]
    elif len(A) == 0:
        return []
    elif len(A) == 2:
        if A[0] < A[1]: return A
        else: return A[::-1]
    step = (max(A) - min(A))//3
    if step == 0:
        step = 1
    B = []

    for i in range(int(min(A)), int(max(A) + 1), int(step)):
        B.append([i])

    for a in A:
        for t in range(len(B)):
            if t == len(B) - 1:
                if B[t][0] <= a:
                    B[t].append(a)
                    break
            elif B[t][0] <= a < B[t + 1][0]:
                B[t].append(a)
                break

    for k in B:
        k.pop(0)

    A = []
    for w in B:
        A += bloch_sort(w)
    return A

print(bloch_sort(A))
