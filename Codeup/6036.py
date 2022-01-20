import sys
input = sys.stdin.readline

string = list(input().rstrip().split())
print(string[0]*int(string[1]))