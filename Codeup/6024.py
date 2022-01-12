#기초-입출력
#단어 2개 입력받아 이어 붙이기

import sys
input = sys.stdin.readline

x, y = input().rstrip().split(" ")
print(x, y, sep='')