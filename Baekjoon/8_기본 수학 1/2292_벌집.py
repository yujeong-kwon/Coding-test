import sys
input = sys.stdin.readline

n = int(input())
num = 1 #벌집 수 
cnt = 1

while n > num:
    num += 6 * cnt  #벌집 6 배수로 증가
    cnt += 1 #반복하는 횟수(겹 수)
    
print(cnt)