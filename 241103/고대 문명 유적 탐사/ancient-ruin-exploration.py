import copy
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<N and 0<=x<N

N = 5

# i,j 기준으로 90 회전한 배열
def rotate90(map,Y,X):
    n = 3
    newA = copy.deepcopy(map)

    threeByThree = [[0]*n for _ in range(n)]
    rotatedThreeByTree = copy.deepcopy(threeByThree)

    for y in range(Y - 1, Y + 1 + 1):
        for x in range(X -1 , X + 1 + 1):
            threeByThree[y - (Y - 1)][x - (X - 1)] = map[y][x]

    for i in range(n):
        for j in range(n):
            rotatedThreeByTree[i][j] = threeByThree[n - 1 -j][i]

    for i in range(Y - 1,Y + 1 + 1):
        for j in range(X - 1 , X + 1 + 1):
            newA[i][j] = rotatedThreeByTree[i - (Y - 1)][j - (X - 1)]


    return newA

# (i,j) 기준으로 갈 수 있는 path
def bfs(i,j,map,visited):

    q = [(i,j)]
    visited[i][j] = True
    path = []

    while q:
        y,x = q.pop(0)
        path.append([y,x])
        for k in range(4):
            ny,nx = y + dy[k],x+ dx[k]
            if not inside(ny,nx):continue
            if map[y][x] != map[ny][nx] or visited[ny][nx]:continue
            visited[ny][nx] = True
            q.append([ny,nx])

    return path

# 가치 탐색 => 맵에서 가치 리스트 반환(우선순위에 맞게)
def getValue(map):
    value = 0
    pathList = []

    v = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if v[i][j]: continue
            path = bfs(i, j, map = map, visited= v)

            if path and len(path) >= 3:
                value += len(path)
                pathList+= path

    pathList.sort(key=lambda x:(x[1],-x[0]))
    return value,pathList

# 유물 획득 (현재 맵에서 유적지 새로 쓰기)
def getParticles(map,pathList):
    global particlesIdx
    for y,x in pathList:
        map[y][x] = particles[particlesIdx]
        particlesIdx+=1

K,M = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
particles = list(map(int,input().split()))
particlesIdx = 0

# 알고리즘 시작
# K 번 반복

for _ in range(K):
    # 탐사 진행 - 현재 유물중에서 가장 큰 value 찾기 -> result = {(value,각도,i,j)}

    result = []

    for i in range(1,N-1):
        for j in range(1,N-1):
            for c in range(3):
                newA = rotate90(a,i,j)
                value,pathList = getValue(newA)
                result.append([value,c,i,j,pathList])

    if not result:break

    result.sort(key=lambda x:(-x[0],x[1],x[3],x[2]))
    Kvalue = 0
    # 탐사 성공! -> 유물 획득 반복
    value,c,i,j,pathList = result[0]
    a = rotate90(map = a,Y = i,X = j)


    while True:
        value,pathList = getValue(a)
        if not pathList:break
        # 새로운 particle 로 채우기
        getParticles(a,pathList)
        Kvalue += value

    if Kvalue == 0 :break

    print(Kvalue,end=' ')