#재귀 - 팩토리얼 구하기
import sys 
input = sys.stdin.readline

n = int(input().rstrip())

def fac(num):
    if(num==0):
        return 1
    
    else:
        return num * fac(num-1)
    

print(fac(n))
