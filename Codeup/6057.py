import sys
input = sys.stdin.readline

a, b = map(int,input().strip().split())

if bool(a) == bool(b):
    print(True)
else:
    print(False) 

#print((bool(a) and bool(b)) or (not bool(a) and not bool(b)))
#print(bool(a)==bool(b))