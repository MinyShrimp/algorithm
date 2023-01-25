# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기
#
# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 
# 모든 도로의 거리는 1이다.
# 
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

# |  input  | output |
# | ------- | ------ |
# | 4 4 2 1 | 4      |
# | 1 2     |        |
# | 1 3     |        |
# | 2 3     |        |
# | 2 4     |        |

from collections import deque

def bfs(graph, N, X, K):
    answer = []
    queue = deque([X])

    dist = [0] * N
    dist[X - 1] = 1

    while queue:
        now = queue.popleft()

        for i in graph[now - 1]:
            if dist[i - 1] != 0:
                continue

            queue.append(i)
            dist[i - 1] = dist[now - 1] + 1
            if dist[i - 1] == K + 1:
                answer.append(i)
    
    return answer

# 입력
N, M, K, X = list(map(int, input().split()))
graph = [ [] for _ in range(N) ]
for i in range(M): 
    a, b = map(int, input().split())
    graph[a - 1].append(b)

# 탐색
answer = bfs(graph, N, X, K)
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    print('\n'.join(map( lambda x: str(x), answer )))