#그리디 - 동전
import sys 
input = sys.stdin.readline

n, k = map(int,input().rstrip().split())
money=[]
for _ in range(n):
    num = int(input())
    money.append(num)

cnt = 0


for i in range(len(money), 0, -1):
    cnt += k // money[i-1]
    k = k % money[i-1]
    
print(cnt)


#  if K == 0 :
#    break
#  count += (K // i)
#  K %= i
