import sys
input = sys.stdin.readline

n = int(input().rstrip())
i = 2
while n != 1:
    if n %  i == 0:
        n = n / i
        print(i)
    else: 
        i += 1
    
    #복습