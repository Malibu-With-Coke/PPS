import sys
input = sys.stdin.readline
result = 0
max_result = 0
for i in range(4):
    a, b = map(int, input().split())
    result -= a
    result += b
    max_result = max(max_result, result)
print(max_result)