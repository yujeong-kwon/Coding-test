import sys
input = sys.stdin.readline

str = ord(input().rstrip())
a = ord("a")
while a <= str:
    print(chr(a), end=" ")
    a = a + 1