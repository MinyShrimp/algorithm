# N x M 크기의 얼음 틀이 있습니다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 갯수를 구하는 프로그램을 작성하세요.
# 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.
# 
# | Input | output |
# | ----- | ------ |
# | 4 5   | 3      |
# | 00110 |        |
# | 00011 |        |
# | 11111 |        |
# | 00000 |        |

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