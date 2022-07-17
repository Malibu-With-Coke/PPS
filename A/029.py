door = int(input())
first = int(input())

for i in range(door-1):
    if door >= 6:
        print("Love is open door")
        break
    else:
        first = 1 - first
        print(first)