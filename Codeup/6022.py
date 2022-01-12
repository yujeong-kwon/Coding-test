#기초-입출력
#연월일 입력받아 나누어 출력하기
import sys 
input = sys.stdin.readline
date = input().rstrip()
print(date[:2], date[2:4], date[4:], sep=" ")