import sys
input = sys.stdin.readline

d = []

d = [[0 for i in range(20)] for j in range(20)]

for i in range(19):
    a = input().rstrip().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

n = int(input().rstrip())
for i in range(n):
    a, b = map(int, input().rstrip().split())
    for j in range(1, 20):
        if d[j][b] == 0 :
            d[j][b] = 1
        else:
            d[j][b] = 0

        if d[a][j] == 0:
            d[a][j] = 1
        else:
            d[a][j] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()