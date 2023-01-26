# https://www.youtube.com/watch?v=PqzyFDUnbrY&list=PLRx0vPvlEmdBFBFOoK649FlEMouHISo8N&index=3
# 01:49:00

from collections import deque

n, k = map(int, input().split())
# 전체 보드 정보를 담는 리스트
# 바이러스에 대한 정보를 담는 리스트
graph, data = [], []

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스의 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기
# ( 낮은 번호의 바이러스가 먼저 증식하므로 )
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 너비 우선 탐색 ( BFS ) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx < n and 0 <= ny < n:
            # 아직 방문하지 않은 경우
            if graph[nx][ny] == 0:
                # 그 위치에 바이러스 넣기
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])