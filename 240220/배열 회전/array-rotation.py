n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def circle(y, x, n, m):
    if n <= 0 or m <= 0: return

    elements = []
    y1,x1,y2,x2 = y,x,y + n - 1, x + m - 1

    for j in range(x1,x2):
        elements.append(a[y1][j])

    for i in range(y1,y2):
        elements.append(a[i][x2])

    for j in range(x2,x1,-1):
        elements.append(a[y2][j])

    for i in range(y2,y1,-1):
        elements.append(a[i][x1])


    elements = elements[1:] + elements[:1]
    idx = 0

    for j in range(x1, x2):
        a[y1][j] = elements[idx]
        idx+=1

    for i in range(y1, y2):
        a[i][x2] = elements[idx]
        idx += 1

    for j in range(x2, x1, -1):
        a[y2][j] = elements[idx]
        idx += 1

    for i in range(y2, y1, -1):
        a[i][x1] = elements[idx]
        idx += 1

    circle(y + 1, x + 1, n - 2, m - 2)

for _ in range(k):
    circle(0, 0, n, m)

for rows in a:
    print(*rows, sep=' ')