# https://www.youtube.com/watch?v=PqzyFDUnbrY&list=PLRx0vPvlEmdBFBFOoK649FlEMouHISo8N&index=3
# 01:47:00

from collections import deque

# 도시의 갯수, 도로의 갯수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, input().split())
graph = [ [] for _ in range(N + 1) ]

# 모든 도로 정보 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * ( N + 1 )
distance[X] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색( BFS ) 수행
q = deque([X])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)