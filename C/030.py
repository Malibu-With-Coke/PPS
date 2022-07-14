n = int(input())
m = int(input())

up = (m-n) + (n-1)
down = n-1

x = up
y = down

for i in range(up-1, up-down, -1):
    up *= i
for i in range(down-1, 1, -1):
    down *= i

if down==0:
    print(1)
else:
    print(int(up/down))