import sys
input = sys.stdin.readline

a, m, d, n = map(int, input().rstrip().split())

for _ in range(n-1):
    a = a * m + d

print(a)