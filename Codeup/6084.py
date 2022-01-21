import sys
input = sys.stdin.readline

h, b, c, s = map(float, input().rstrip().split())

byte = h * b * c * s / 8 / 1024 / 1024

print(format(float(byte),".1f"), "MB")
