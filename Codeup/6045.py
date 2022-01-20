import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
print("%d %0.2f"%(a+b+c, (a+b+c)/3))
#print(a+b+c,round((a+b+c)/3,2),sep=" ")
#잘못된 풀이  round에 대해 정리