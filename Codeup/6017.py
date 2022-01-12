#기초-입출력
#문자 1개 입력받아 그대로 출력하기

import sys
input = sys.stdin.readline

str = input().rstrip()
print(str,str,str, sep=" ")