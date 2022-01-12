#기초-입출력
#단어 1개 입력받아 나누어 출력하기
import sys
input = sys.stdin.readline
x = input().rstrip()
for i in range (len(x)):
    print(x[i])