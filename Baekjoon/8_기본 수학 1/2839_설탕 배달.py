import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0

while n >= 0:
    if n % 5 == 0:
        cnt += (n//5)
        print(cnt)
        break
    n -= 3
    cnt += 1 
    #5의 배수가 될 때까지 설탕-3, 봉지+1
else:
    print(-1)
    #while-else 문