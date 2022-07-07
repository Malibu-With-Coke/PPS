n = int(input())
m = int(input())

graph = [[]*n for i in range(n+1)] # 이차원 배열 선언 array = [[0]*n for i in range(m)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)

def dfs(start):
    global cnt  # 글로벌 변수 사용.
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)

# https://application-s.tistory.com/42 (일차원 배열 선언 및 초기화)
# https://infinitt.tistory.com/106 (이차원 배열 선언)
# https://wikidocs.net/62 (전역 변수)