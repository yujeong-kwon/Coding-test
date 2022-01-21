import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
#print("%d\n%d\n%d\n%d\n%d"%(a+b,a-b,a*b,a/b,a%b))
#print(format(float(a)/float(b), ".2f"))
print(a+b,a-b,a*b,a//b,a%b,round(a/b,2),sep="\n")
