def solution(x):
    answer = True

    xs = str(x)

    s = 0
    for i in range(len(xs)):
        s += int(xs[i])

    if x % s == 0:
        answer = True
    else:
        answer = False

    return answer