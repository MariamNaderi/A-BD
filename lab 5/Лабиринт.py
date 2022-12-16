
import turtle

def draw_stena(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.backward(20)
    turtle.right(90)
    turtle.backward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()

def draw_prohod(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.backward(20)
    turtle.right(90)
    turtle.backward(20)
    turtle.left(90)
    turtle.forward(20)

def draw_lab(B, lenB, lenstr):
    x, y = -10*lenstr, 10*lenB + 20
    turtle.tracer(0, 0)
    for i in range(lenB):
        x = -10*lenstr
        y -= 20
        for t in range(lenstr):
            if B[i][t] == 1:
                draw_stena(x, y)
            else:
                draw_prohod(x, y)
            x += 20

def draw_way(lenB, lenstr, putb):
    x, y = -10 * lenstr - 20, 10 * lenB
    turtle.tracer(1)
    turtle.penup()
    turtle.goto(x, y - putb[0][0] * 20 - 10)
    turtle.pendown()
    turtle.color('red')
    for h in putb:
        turtle.goto(x + 20 * h[1] + 10, y - h[0] * 20 - 10)


def readFile(B):
    F = open('ladirint.txt', encoding="utf8")
    c = F.readline()
    while c:
        B.append(list(map(int, c.split())))
        c = F.readline()
    F.close()
    return B

def vxod(B, lenB):
    vxodi = []
    for t in range(lenB):
        if B[t][0] == 0:
            vxodi.append((t, 0))
    return vxodi

def vixod(B, lenB, lenstr):
    vixodi = []
    for t in range(lenB):
        if B[t][lenstr - 1] == 0:
            vixodi.append((t, lenstr - 1))
    return vixodi

def main(A, B, l):
    s = []
    for e in l:
        x = e[0]
        y = e[1]
        p = A[x][y]
        if  x - 1 >= 0 and B[x - 1][y] == 0 and A[x - 1][y] == 0:
            A[x - 1][y] = p + 1
            s.append((x - 1, y))
        if  x + 1 < 15 and B[x + 1][y] == 0 and A[x + 1][y] == 0:
            A[x + 1][y] = p + 1
            s.append((x + 1, y))
        if  y - 1 >= 0 and B[x][y - 1] == 0 and A[x][y - 1] == 0:
            A[x][y - 1] = p + 1
            s.append((x, y - 1))
        if  y + 1 < 15 and B[x][y + 1] == 0 and A[x][y + 1] == 0:
            A[x][y + 1] = p + 1
            s.append((x, y + 1))
    return A, s

def f():
    A = []
    B = []

    B = readFile(B)
    lenB = len(B)
    lenstr = len(B[0])

    starts = vxod(B, lenB)
    start = len(starts)
    if start > 1:
        start = 'Какой вход из ' + str(start) + ' вам нужен?\n'
        start = starts[int(input(start)) - 1]
    else:
        start = starts[0]
    for p in range(lenB):
        A.append([0] * lenstr)
    A[start[0]][start[1]] = 1
    s = [start]

    while s:
        A, s = main(A, B, s)

    return A, B, start, lenB, lenstr

def itog(A, ends):
    end = len(ends)
    if end > 1:
        end = 'Какой выход из ' + str(end) + ' вам нужен?\n'
        end = ends[int(input(end)) - 1]
    else:
        end = ends[0]

    k = A[end[0]][end[1]]
    putb = [end]
    x, y = end[0], end[1]
    while k > 1:
        if x - 1 >= 0 and A[x - 1][y] == k - 1:
            putb.append((x - 1, y))
            k -= 1
            x -= 1
        elif x + 1 < 15 and A[x + 1][y] == k - 1:
            putb.append((x + 1, y))
            k -= 1
            x += 1
        elif y - 1 >= 0 and A[x][y - 1] == k - 1:
            putb.append((x, y - 1))
            k -= 1
            y -= 1
        elif y + 1 < 15 and A[x][y + 1] == k - 1:
            putb.append((x, y + 1))
            y += 1
            k -= 1

    return putb[::-1]



A, B, starts, lenB, lenstr = f()
ends = vixod(B, lenB, lenstr)

putb = itog(A, ends)

if len(putb) == 1:
    print('Выхода нет')
else:
    print('Координаты:', putb, len(putb))
    draw_lab(B, lenB, lenstr)
    draw_way(lenB, lenstr, putb)
    turtle.done()