import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
print("%d %0.2f"%(a+b+c, (a+b+c)/3))

#잘못된 풀이
#print(a+b+c,round((a+b+c)/3,2),sep=" ")
#round 함수의 두가지 기능
# 1) 특정자리수까지의 반올림
# 2) 쓸데없이 많은 0을 1개로 줄인다 
# (2.00 이아니라 2.0으로 소수이하 0은 1개만 출력)