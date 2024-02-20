n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def circle(y, x, n, m):
    if n <= 0 or m <= 0: return

    elements = []
    indexes = []

    y1,x1,y2,x2 = y,x,y + n - 1, x + m - 1

    for j in range(x1,x2):
        elements.append(a[y1][j])
        indexes.append((y1,j))

    for i in range(y1,y2):
        elements.append(a[i][x2])
        indexes.append((i,x2))

    for j in range(x2,x1,-1):
        elements.append(a[y2][j])
        indexes.append((y2,j))

    for i in range(y2,y1,-1):
        elements.append(a[i][x1])
        indexes.append((i,x))

    elements = elements[1:] + elements[:1]
    idx = 0

    for (i,j),element in zip(indexes,elements):
        a[i][j] = element
    
    circle(y + 1, x + 1, n - 2, m - 2)

for _ in range(k):
    circle(0, 0, n, m)

for rows in a:
    print(*rows, sep=' ')