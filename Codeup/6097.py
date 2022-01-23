import sys
input = sys.stdin.readline

h ,w = map(int, input().rstrip().split())
data = [[0 for i in range(w+1)] for j in range(h+1)]
#w만큼이 h번 반복
n = int(input().rstrip())
for _ in range(n):
    l, d, x, y = map(int, input().rstrip().split())
    for i in range(l):
        if d == 0:
            data[x][y+i] = 1
        if d == 1:
            data[x+i][y] = 1

for i in range(1,h+1):
    for j in range(1, w+1):
        print(data[i][j], end=" ")
    print()

h,w = map(int, input().rstrip().split() )


