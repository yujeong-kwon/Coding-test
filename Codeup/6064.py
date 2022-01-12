import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
print((a if (a<b) else b) if ((a if (a<b) else b)<c) else c)