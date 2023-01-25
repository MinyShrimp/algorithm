# 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
# 
# 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다.
# 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
# 
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 갯수를 구하세요.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.
# 
# | Input  | output |
# | ------ | ------ |
# | 5 6    | 10     |
# | 101010 |        |
# | 111111 |        |
# | 000001 |        |
# | 111111 |        |
# | 111111 |        |

from collections import deque

# 이동할 네 가지 방향 정의
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(graph, N, M, x, y):
    queue = deque()
    queue.append((x, y))

    # Queue가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N - 1][M - 1]

def solution(N, M, grid):
    graph = []
    for row in grid.split('\n'):
        graph.append( list(map(int, list(row))) )

    return bfs(graph, N, M, 0, 0)

print( solution(5, 6, "101010\n111111\n000001\n111111\n111111") )