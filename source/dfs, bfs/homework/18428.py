# https://www.acmicpc.net/problem/18428
# 감시 피하기
#
# NxN 크기의 복도가 있다. 
# 복도는 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다. 
# 현재 몇 명의 학생들은 수업시간에 몰래 복도로 빠져나왔는데, 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.
# 
# 각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 
# 단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다. 
# 또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.
# 
# 다음과 같이 3x3 크기의 복도의 정보가 주어진 상황을 확인해보자. 
# 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다. 
# 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S, 장애물이 존재하는 칸은 O로 표시하였다. 
# 아래 그림과 같이 (3,1)의 위치에는 선생님이 존재하며 (1,1), (2,1), (3,3)의 위치에는 학생이 존재한다. 
# 그리고 (1,2), (2,2), (3,2)의 위치에는 장애물이 존재한다. 
# 
# S O □
# S O □
# T O S
# 
# 이 때 (3,3)의 위치에 존재하는 학생은 장애물 뒤편에 숨어 있기 때문에 감시를 피할 수 있다. 
# 하지만 (1,1)과 (2,1)의 위치에 존재하는 학생은 선생님에게 들키게 된다.
# 
# 학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 한다. 
# 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산하고자 한다. 
# NxN 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하시오.

# 조합을 뽑아내는 함수
from itertools import combinations

def watch(board, x, y, dir, N):
    # 왼쪽
    if dir == 0:
        while x >= 0:
            if board[y][x] == 'S':
                return True
            elif board[y][x] == 'O':
                return False
            x -= 1
    # 오른쪽
    elif dir == 1:
        while x < N:
            if board[y][x] == 'S':
                return True
            elif board[y][x] == 'O':
                return False
            x += 1
    # 위
    elif dir == 2:
        while y >= 0:
            if board[y][x] == 'S':
                return True
            elif board[y][x] == 'O':
                return False
            y -= 1
    # 아래
    else:
        while y < N:
            if board[y][x] == 'S':
                return True
            elif board[y][x] == 'O':
                return False
            y += 1
    return False

# 학생 발견 = True,
# 미 발견 = False
def process(board, tp, N):
    for x, y in tp:
        for i in range(4):
            if watch(board, x, y, i, N):
                return True
    return False

def solution():
    # 입력 받기
    N = int(input())

    # 복도 정보, 선생님 위치, 빈 공간 위치
    board, tp, sp = [], [], []
    for i in range(N):
        board.append(list(input().split()))
        for j in range(N):
            if board[i][j] == 'T':
                tp.append((j, i))
            elif board[i][j] == 'X':
                sp.append((j, i))

    # 모든 경우의 수 확인
    # 모든 빈 공간에 3개의 장애물 설치
    for data in combinations(sp, 3):
        # 장애물 설치
        for x, y in data:
            board[y][x] = 'O'

        # 검사
        if not process(board, tp, N):
            return True

        # 설치된 장애물 제거
        for x, y in data:
            board[y][x] = 'X'
    
    return False

print( 'YES' if solution() else 'NO' )