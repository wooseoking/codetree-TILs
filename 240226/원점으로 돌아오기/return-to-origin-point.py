n = int(input())
points = []
for _ in range(n):
    x,y = map(int,input().split())
    points.append([x,y])

visited = [False]*n

def canGoNext(x,y,nx,ny):
    return x == nx or y == ny

ans = 0
def solve(x,y,cnt):
    global ans
    if cnt == n:
        if canGoNext(x,y,0,0):
            ans +=1
        return

    for i in range(n):
        if visited[i]:continue
        nx,ny = points[i]
        if canGoNext(x,y,nx,ny):
            visited[i] = True
            solve(nx,ny,cnt + 1)
            visited[i] = False

solve(0,0,0)
print(ans)