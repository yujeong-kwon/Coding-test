import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

#if a != b:
#    print(True)
#else:
#    print(False)


if not a == b:
    print(True)
else: 
    print(False)