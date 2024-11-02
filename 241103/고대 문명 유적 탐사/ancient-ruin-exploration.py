import copy
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def inside(y,x):
    return 0<=y<N and 0<=x<N

N = 5


# 각도에 따른 회전 함수
def rotate(map, Y, X, angle):
    n = 3
    newA = copy.deepcopy(map)

    # 3x3 부분 추출
    threeByThree = [[map[y][x] for x in range(X - 1, X + 2)] for y in range(Y - 1, Y + 2)]

    # 각도에 따른 회전
    rotatedThreeByThree = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if angle == 90:
                rotatedThreeByThree[i][j] = threeByThree[n - 1 - j][i]
            elif angle == 180:
                rotatedThreeByThree[i][j] = threeByThree[n - 1 - i][n - 1 - j]
            elif angle == 270:
                rotatedThreeByThree[i][j] = threeByThree[j][n - 1 - i]
            else:
                rotatedThreeByThree[i][j] = threeByThree[i][j]

    # 회전된 3x3 부분을 newA에 적용
    for i in range(n):
        for j in range(n):
            newA[Y - 1 + i][X - 1 + j] = rotatedThreeByThree[i][j]

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
def writeParticles(map,pathList):
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

            for angle in [90,180,270]:
                rotatedA = rotate(a,i,j,angle)
                value,pathList = getValue(rotatedA)
                if value > 0 :
                    result.append((value,angle,i,j,pathList))

    if not result:break

    result.sort(key=lambda x:(-x[0],x[1],x[3],x[2]))
    maxValue,angle,i,j,pathList = result[0]
    # 탐사 성공! -> 유물 획득 반복
    a = rotate(a,i,j,angle)
    Kvalue = 0

    while True:
        value,pathList = getValue(a)
        if not pathList:break
        # 새로운 particle 로 채우기
        writeParticles(a,pathList)
        Kvalue += value

    if Kvalue == 0 :break

    print(Kvalue,end=' ')