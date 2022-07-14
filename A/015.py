sum = 0;
for num in map(int, input().split()):
    sum += num**2
print(sum % 10)​