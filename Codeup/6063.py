import sys
input = sys.stdin.readline

a, b = map(int,input().rstrip().split())
print(a if (a>b) else b)