import sys
input = sys.stdin.readline

d = []
for i in range(20):
    d.append([])
    for _ in range(20):
        d[i].append(0)
# d = [[0 for j in range(20)] for i in range(20)]
n = int(input().rstrip())
for i in range(n):
    a, b = map(int, input().rstrip().split())
    d[a][b] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()
