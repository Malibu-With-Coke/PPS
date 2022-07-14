def get_num(num):
    answer = 0
    for i in range(1,num):
        if num % i == 0:
            answer+=1
            
    return answer+1

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if get_num(i)%2==0:
            answer += i
        else:
            answer -= i
    return answer