import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = map(int, input().rstrip().split())
cnt = 0
for i in nums:
    error = 0
    if i > 1:
        for j in range(2, i): #2부터 i-1까지
            if i % j == 0:
                error += 1
        if error == 0:
            cnt += 1 #error가 없으면 소수
    #i가 1이면 그냥 패스 
print(cnt)
 

 #복습