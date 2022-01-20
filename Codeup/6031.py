import sys
input = sys.stdin.readline

num = int(input().rstrip())
print(chr(num))

#chr()는 정수값->문자, ord()는 문자->정수값 형태로 바꿔주는 기능