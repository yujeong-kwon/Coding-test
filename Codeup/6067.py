import sys
input = sys.stdin.readline

n = int(input().rstrip())

if n<0 and n%2==0:
    print("A")
elif n<0 and n%2!=0:
    print("B")
elif n>0 and n%2==0:
    print("C")
else:
    print("D")