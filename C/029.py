# a, b, c = map(int, input('숫자 두 개를 입력하세요: ').split())

# num = 0 
# while(True):
#     num+= 1
#     if a + b * num < c * num:
#         print(num)
#         break


a, b, c = map(int, input().split())

if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)