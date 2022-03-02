#재귀 - 팩토리얼 구하기
import sys 
input = sys.stdin.readline

n = int(input().rstrip())

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(n))
