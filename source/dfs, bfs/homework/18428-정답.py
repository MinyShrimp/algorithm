# https://www.youtube.com/watch?v=PqzyFDUnbrY&list=PLRx0vPvlEmdBFBFOoK649FlEMouHISo8N&index=3
# 01:55:00

# 문제 해결 아이디어
# * 장애물을 정확히 3개 설치하는 모든 경우를 확인하며, 
#   매 경우마다 모든 학생을 감시로부터 피하도록 할 수 있는지의 여부를 출력합니다.
# * 복도의 크기는 N x N 이며, N은 최대 6입니다. 
#   따라서 장애물을 정확히 3개 설치하는 모든 조합의 수는 최악의 경우 36C3 입니다.
# * 경우의 수가 10,000 이하이므로, 모든 조합을 고려하여 완전 탐색을 수행해 해결할 수 있습니다.
#     * 모든 조합을 찾을 때에는 DFS/BFS를 이용하거나 조합 계산 라이브러리를 사용합니다.

# 조합을 뽑아내는 함수
from itertools import combinations

# 복도의 크기
n = int(input())
# 복도 정보 ( N x N )
board = []
# 모든 선생님 위치 정보
teachers = []
# 모든 빈 공간 위치 정보
spaces = []

# 복도 정보 입력 받기
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시 진행
# 학생 발견 = True / 미 발견 = False
def watch(x, y, direction):
    # 왼쪽 방향
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향
    elif direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향
    elif direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향
    elif direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

# 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부
find = False

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물들을 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

# 결과 출력
print('YES' if find else 'NO')
