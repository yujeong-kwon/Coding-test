#기초-입출력
#주민번호 입력받아 형태 바꿔 출력하기
import sys
input = sys.stdin.readline
num1, num2 = input().rstrip().split("-")
print(num1, num2, sep="")
