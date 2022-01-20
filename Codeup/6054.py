import sys
input = sys.stdin.readline

a, b = map(int,input().rstrip().split())
#if a and b == True:
#    print(True)
#else:
#    print(False)
print(bool(a) and bool(b))