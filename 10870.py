import sys 
input = sys.stdin.readline

n = int(input().rstrip())

def fibo(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibo(num-2) + fibo(num-1)

print(fibo(n))