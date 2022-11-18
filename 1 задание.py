import timeit

start = timeit.default_timer()
p = input()
A = list(map(int, p.split()))
B = list(map(int, p.split()))
l = len(A)
for o in range(l - 1):
    for i in range(0, l - 1 - o):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]

print(*A)
end = timeit.default_timer()
print(end - start)
#Сложность: O(2n)

start1 = timeit.default_timer()
B.sort()
print(*B)
end1 = timeit.default_timer()
print(end1 - start1)
print((end - start) / (end1 - start1))

#Сложность: О(nlogn)
