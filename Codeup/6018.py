#기초 - 입출력
# 시간 입력받아 그대로 출력하기
import sys
input = sys.stdin.readline

time = input()
h, m = time.split(sep=":")
print(h, m, sep = ":")
#print에서 sep을 주면 그 값을 사이에 두고 값을 출력
