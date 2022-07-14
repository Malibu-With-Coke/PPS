def cut(s, l):
    t = ''
    i = 0
    while len(s) > 0:
        ch = s[:l]
        cnt = 1
        while True:
            if ch == s[l * (cnt): l * (cnt + 1)]:
                cnt += 1
            else:
                break
        s = s[l*cnt:]
        if cnt != 1:
            t += str(cnt) + ch
        else:
            t += ch
    return len(t)

def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        v = cut(s, i)
        if answer > v:
            answer = v
    return answer