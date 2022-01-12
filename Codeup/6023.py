#기초-입출력
#시분초 입력받아 분만 출력하기

import sys
input = sys.stdin.readline

h, m, s = input().rstrip().split(":")
print(m)