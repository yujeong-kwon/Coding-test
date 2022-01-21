import sys
input = sys.stdin.readline

a, b = map(int,input().strip().split())

if bool(a) == 0 and bool(b) == 0:
    print(True)
else:
    print(False)

#print(not(bool(a) or bool(b)))
