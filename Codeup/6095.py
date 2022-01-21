import sys
input = sys.stdin.readline

d = []
for i in range(20):
    d.append([0])
    for _ in range(20):
        d[i].append(0)

n = int(input().rstrip())
for i in range(n):
    a, b = map(int, input().rstrip().split())

