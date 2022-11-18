#Сложность O(n!)
def f(n):
    num = n
    if n == 0: return 1
    for i in range(n):
        num = n * f(n - 1)
    return num