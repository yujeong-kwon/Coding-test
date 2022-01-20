import sys
input = sys.stdin.readline

n = int(input().rstrip())
#if n == 0:
#    print(False)
#else:
#    print(True)
#bool()을 이용하면 입력된 식이나 값을 평가해 불 형의 값 (T/F)을 출력해준다
print(bool(n))