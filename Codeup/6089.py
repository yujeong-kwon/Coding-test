import sys
input = sys.stdin.readline

a, r, n = map(int, input().rstrip().split())

for _ in range(n-1):
    a *= r

print(a)