import sys
input = sys.stdin.readline

r, g, b = map(int, input().rstrip().split())

cnt = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            cnt += 1

print(cnt)

#print(r*g*b)