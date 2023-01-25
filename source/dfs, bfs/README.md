## DFS, BFS
> 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말합니다.
> 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있습니다.
> DFS/BFS는 코딩 테스트에서 **매우 자주 등장하는 유형**이므로 반드시 숙지해야 합니다.

## 깊이 우선 탐색 ( DFS - Depth First Search )
> 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘입니다.
> DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
> 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
> 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리를 합니다.
> 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
> 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

```python
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 ( 1차원 리스트 )
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 실행 결과
# 1 2 7 6 8 3 4 5
```

## 너비 우선 탐색 ( Breadth First Search )
> 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.
> 큐 자료구조를 이용하며, 구제적인 동작 과정은 다음과 같습니다.
> 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 합니다.
> 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 합니다.
> 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

```python
from collections import deque

def bfs(graph, start, visited):
    # 큐 ( Queue ) 구현을 위해 deque 라이브러리를 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = ' ')

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 ( 1차원 리스트 )
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

# 실행 결과
# 1 2 3 8 7 4 5 6 
```

---

### 문 1
* N x M 크기의 얼음 틀이 있습니다.
* 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
* 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
* 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 갯수를 구하는 프로그램을 작성하세요.
* 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

| Input | output |
| ----- | ------ |
| 4 5   | 3      |
| 00110 |        |
| 00011 |        |
| 11111 |        |
| 00000 |        |

### 답 1
* DFS, BFS 모두 해결할 수 있습니다.
* 일단 앞에서 배운 대로 얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링 할 수 있습니다.

* DFS를 활용하는 알고리즘은 다음과 같습니다.
    1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
    2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있습니다.
    3. 모든 노드에 대하여 1 ~ 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트합니다.

```python
def dfs(graph, N, M, x, y):
    # 주어진 범위를 벗어난 경우, 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    # 현재 노드를 방문했다면, 즉시 종료
    if graph[x][y] != 0:
        return False
    
    # 해당 노드 방문 처리
    graph[x][y] = 1

    # 상, 하, 좌, 우 모두 재귀적으로 호출
    dfs(graph, N, M, x - 1, y)
    dfs(graph, N, M, x + 1, y)
    dfs(graph, N, M, x, y - 1)
    dfs(graph, N, M, x, y + 1)
    return True

def solution(N, M, grid):
    graph = []
    for row in grid.split('\n'):
        graph.append( list(map(int, list(row))) )
    
    # 모든 위치에 대하여 방문하기
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(graph, N, M, i, j):
                result += 1
    
    return result

print( solution(4, 5, "00110\n00011\n11111\n00000") )
```

---

### 문 2
* 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다.
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
* 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다.
미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
* 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 갯수를 구하세요.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

| Input  | output |
| ------ | ------ |
| 5 6    | 10     |
| 101010 |        |
| 111111 |        |
| 000001 |        |
| 111111 |        |
| 111111 |        |

### 답 2
* BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색합니다.
* 상하좌우로 연결된 모든 노드로의 거리가 1로 동일합니다.
    * 따라서 (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있습니다.

```python
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
```