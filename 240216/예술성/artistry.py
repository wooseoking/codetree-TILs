import itertools
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def init():
    groupMatrix = [[0] * n for _ in range(n)]
    groupNumbersCount = dict()
    visited = [[False] * n for _ in range(n)]
    z = 0

    # bfs 를 통한 grounNumber 개수 구하기
    def bfs(y, x, groupNumber, z, groupMatrix):
        visited[y][x] = True
        q = deque()
        q.append([y, x])

        cnt = 0

        while q:
            y, x = q.popleft()
            cnt += 1
            groupMatrix[y][x] = z
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if not inside(ny, nx): continue
                if visited[ny][nx]: continue
                if a[ny][nx] != groupNumber: continue
                q.append([ny, nx])
                visited[ny][nx] = True

        return cnt

    for i in range(n):
        for j in range(n):
            groupNumber = a[i][j]
            if visited[i][j]: continue
            cnt = bfs(i, j, groupNumber, z,groupMatrix)
            groupNumbersCount[z] = (cnt, groupNumber)
            z += 1


    return groupMatrix,groupNumbersCount


def inside(y, x):
    return 0 <= y < n and 0 <= x < n


def rotateCross():
    m = n//2
    garo = []
    sero = []
    for j in range(n):
        garo.append(a[m][j])
    for i in range(n):
        sero.append(a[i][m])

    for j in range(n):
        a[m][j] = sero[j]

    garo.reverse()
    for i in range(n):
        a[i][m] = garo[i]

def rotateRectangle(y,x,l):
    tmp = [[0]*l for _ in range(l)]
    rotatedTmp = [[0]*l for _ in range(l)]
    for i in range(y,y + l):
        for j in range(x,x+l):
            tmp[i-y][j-x] = a[i][j]

    for i in range(l):
        for j in range(l):
            rotatedTmp[i][j] = tmp[l-1-j][i]

    for i in range(y,y+l):
        for j in range(x,x+l):
            a[i][j] = rotatedTmp[i - y][j - x]


def rotateAllRectangle():
    m = n//2
    points = [(0,0),(0,m+1),(m+1,0),(m + 1,m+1)]

    for point in points:
        y,x = point
        l = (n - 1) // 2
        rotateRectangle(y,x,l)

def rotate():
    rotateCross()
    rotateAllRectangle()

def getHarmony(g1,g2,groupNumbersCount,groupMatrix):
    g1cnt = groupNumbersCount[g1][0]
    g1Number = groupNumbersCount[g1][1]

    g2cnt = groupNumbersCount[g2][0]
    g2Number = groupNumbersCount[g2][1]

    return (g1cnt + g2cnt) * g1Number * g2Number * getBorder(g1,g2,groupMatrix)
def getBorder(g1,g2,groupMatrix):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if groupMatrix[i][j] == g1:
                for k in range(4):
                    ny,nx = i + dy[k],j+dx[k]
                    if not inside(ny,nx):continue
                    if groupMatrix[ny][nx] == g2:
                        cnt+=1
    return cnt



answer = 0

# for rows in groupMatrix:
#     print(*rows,sep= ' ')
# print('--------------------')
for _ in range(4):
    total = 0
    groupMatrix, groupNumbersCount = init()
    gLists = list(groupNumbersCount.keys())
    for s in itertools.combinations(gLists,2):
        g1,g2 = s
        harmony = getHarmony(g1,g2,groupNumbersCount,groupMatrix)
        total += harmony
    rotate()
    answer += total
print(answer)