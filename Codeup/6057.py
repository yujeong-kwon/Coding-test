import sys
input = sys.stdin.readline

a, b = map(int,input().strip().split())

if bool(a) == bool(b):
    print(True)
else:
    print(False) 