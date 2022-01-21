import sys
input = sys.stdin.readline

string = list(input().rstrip().split())
print(string[0]*int(string[1]))

#w, n = input().rstrip().split()
#print(w * int(n))