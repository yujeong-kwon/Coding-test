import sys
input = sys.stdin.readline

w, h, b = map(int, input().rstrip().split())

byte = w * h * b / 8 / 1024 / 1024

print("%.2f MB" % byte)