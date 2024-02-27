n = int(input())
points = []
for _ in range(n):
    x,y = map(int,input().split())
    points.append([x,y])


visited = [False]*n
def canGo(fx,fy,tx,ty):
    return fx == tx or fy == ty

# 0 ,1, 2, 3
def getDirection(fx,fy,tx,ty):
    if tx == fx and fy < ty:return 0
    elif fy == ty and fx < tx:return 1
    elif tx == fx and fy > ty : return 2
    elif fy == ty and tx < fx : return 3

ans = 0
res = []
def solve(curx,cury,directionFrom,depth):
    global ans

    if depth == n:
        if canGo(curx,cury,0,0) and directionFrom != getDirection(curx,cury,0,0):
            ans += 1
        return

    for i in range(n):
        if visited[i]:continue
        tox,toy = points[i]
        nextDirection = getDirection(curx, cury, tox, toy)
        if not canGo(curx,cury,tox,toy):continue

        if directionFrom == -1 or directionFrom != nextDirection:
            visited[i] = True
            solve(tox, toy, nextDirection, depth + 1)
            visited[i] = False



solve(0,0,directionFrom= -1,depth= 0)
print(ans)