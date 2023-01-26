# https://www.acmicpc.net/problem/18405
# 경쟁적 전염
#
# NxN 크기의 시험관이 있다. 
# 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 
# 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.
# 
# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 
# 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
# 
# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 
# 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 
# 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.
# 
# 예를 들어 다음과 같이 3x3 크기의 시험관이 있다고 하자. 
# 서로 다른 1번, 2번, 3번 바이러스가 각각 (1,1), (1,3), (3,1)에 위치해 있다. 
# 이 때 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보자.

from pprint import pprint
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(grid, graph, visited, N, S):
    # 총 반복 횟수
    for _ in range(S):
        # K 번 반복
        for i, queue in enumerate(graph):
            tmp_queue = deque()
            while queue:
                p = queue.popleft()

                # 4방향 탐색
                for x, y in zip(dx, dy):
                    _x = p[0] + x
                    _y = p[1] + y
                    # 보드를 넘어간 경우 패스
                    if _x < 0 or _x >= N or _y < 0 or _y >= N:
                        continue
                    # 이미 방문한 경우 패스
                    if visited[_y][_x] == 1:
                        continue
                    # 큐에 넣기
                    visited[_y][_x] = 1
                    grid[_y][_x] = i + 1
                    tmp_queue.append([_x, _y])
            graph[i] = tmp_queue

def solution():
    N, K = list(map(int, input().split()))
    grid = [ list(map(int, input().split())) for _ in range(N) ]
    S, X, Y = list(map(int, input().split()))

    visited = [ [0] * N for _ in range(N) ]
    graph = [ deque() for _ in range(K) ]

    # graph 배열
    # [0] => [ [0, 0] ]
    # [1] => [ [2, 0] ]
    # [2] => [ [0, 2] ]
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                graph[ grid[i][j] - 1 ].append([j, i])
                visited[i][j] = 1

    bfs(grid, graph, visited, N, S)

    # return grid[Y - 1][X - 1]
    return grid[X - 1][Y - 1]

print( solution() )