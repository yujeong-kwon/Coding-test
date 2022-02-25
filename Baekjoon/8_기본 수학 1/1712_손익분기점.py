import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())


if b >= c:
    print(-1)
else:
    print(int(a/(c-b))+1)    

#수학은 다 복습,,