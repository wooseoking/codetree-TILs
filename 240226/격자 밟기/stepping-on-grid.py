import math

dy = [-1,1,0,0]
dx = [0,0,-1,1]
n = 5
wall = [[False]*n for _ in range(n)]
m = int(input())
for _ in range(m):
    wy,wx = map(int,input().split())
    wy-=1
    wx-=1
    wall[wy][wx] = True


def inside(y,x):
    return 0<=y<n and 0<=x<n

sry ,srx ,sby,sbx = 0,0,n-1,n-1
answer = 0
visited = [[False]*n for _ in range(n)]
def solve(ry,rx,rycnt,by,bx,bycnt):
    global answer

    if ry == sry and rx == srx and by == sby and bx == sbx and rycnt + bycnt + m == pow(n,2) - 1:
        answer +=1
        return

    for rk in range(4):
        for bk in range(4):
            nry,nrx = ry + dy[rk] , rx + dx[rk]
            nby,nbx = by + dy[bk] , bx + dx[bk]
            if not inside(nry,nrx) or not inside(nby,nbx):continue
            if visited[nry][nrx] or visited[nby][nbx]:continue
            if wall[nry][nrx] or wall[nby][nbx]:continue
            if nry == nby and nrx == nbx:
                if rycnt + bycnt + m == pow(n,2) - 1:
                    answer += 1
                continue

            visited[ry][rx] = True
            visited[by][bx] = True
            solve(nry,nrx,rycnt + 1,nby,nbx,bycnt + 1)
            visited[ry][rx] = False
            visited[by][bx] = False

solve(sry,srx,1,sby,sbx,1)
print(answer)