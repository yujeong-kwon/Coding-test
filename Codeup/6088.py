import sys
input = sys.stdin.readline

a, d, n = map(int,input().rstrip().split())

print(a + (n-1) * d)