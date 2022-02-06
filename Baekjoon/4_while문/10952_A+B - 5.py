import sys
input = sys.stdin.readline
a = -1
b = -1
while a!=0 and b!=0:
    a, b = map(int,input().rstrip().split())
    if a!=0 and b!=0:
        print(a+b)