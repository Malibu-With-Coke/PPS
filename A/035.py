num = int(input())
for i in range(num):
    munza = list(map(str ,input().split()))
    result = float(munza[0])
    for j in range(1,len(munza)):
        if munza[j] == "#":
            result -= 7
        elif munza[j] == "%":
            result += 5
        elif munza[j] == "@":
            result *= 3
    print("{:.2f}".format(result))