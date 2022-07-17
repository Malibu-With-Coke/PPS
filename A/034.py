list1 = []
for i in range(10):
    num = int(input())%42
    if num not in list1:
        list1.append(num)
print(len(list1))