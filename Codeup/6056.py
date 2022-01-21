import sys
input = sys.stdin.readline

a, b = map(int,input().rstrip().split())

print((bool(a) and not(bool(b))) or (not(bool(a)) and bool(b)))