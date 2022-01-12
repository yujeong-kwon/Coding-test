#기초-입출력
#연월일 입력받아 순서 바꿔 출력하기
import sys
input = sys.stdin.readline
y, m, d = input().rstrip().split(".")
print(d, m, y, sep="-")