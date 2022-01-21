import sys
input = sys.stdin.readline

str = int(input().rstrip())

if str//3 == 1:
    print("spring")
elif str//3 == 2:
    print("summer")
elif str//3 == 3:
    print("fall")
else:
    print("winter")
