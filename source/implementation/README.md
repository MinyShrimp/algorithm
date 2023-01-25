## 구현 문제 ( Implementation )
> 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭

* 예시
    * 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
    * 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
    * 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
    * 적절한 라이브러리를 찾아서 사용해야 하는 문제

* 프로그래밍에서의 좌표계는 일반적인 대수학에서의 좌표계와 다른 의미를 가질 때가 많습니다.
    * 일반적으로 알고리즘 문제에서의 2차원 공간은 **행렬(Matrix)**의 의미로 사용됩니다.

* 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됩니다.
```python
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

# 다음 위치
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
```

---

### 문 1
> 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시작 중에서 <br>
> 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
> 
> 예를 들어, 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다. <br>
> * 00시 00분 03초
> * 00시 13분 30초
> 
> 반면에, 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각입니다. <br>
> * 00시 02분 55초
> * 01시 27분 45초

### 답 1
* 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제입니다.
* 하루는 86,400초이므로, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86,400가지입니다.
* 따라서 단순히 시작을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됩니다.
* 이러한 유형은 완전 탐색(Brute Forcing) 문제 유형이라고 불립니다.
    * 가능한 경우의 수를 모두 검사해보는 탐색 방법을 의미합니다.
```python
def solution(N):
    answer = 0

    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    answer += 1

    return answer
```

---

### 문 2
> 여행가 A는 N x N 크기의 정사각형 공간 위에 서있습니다. <br>
> 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다. <br>
> 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다. <br>
> 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다. <br>
> 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다. <br>
> 
> 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있습니다. <br>
> 각 문자의 의미는 다음과 같습니다.
> * L : 왼쪽으로 한 칸 이동
> * R : 오른쪽으로 한 칸 이동
> * U : 위로 한 칸 이동
> * D : 아래로 한 칸 이동

> 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다.
> 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됩니다.

### 답 2
* 요구사항대로 충실히 구현하면 되는 문제입니다.
* 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션(Simulation) 유형으로도 분류되며 구현이 중요한 대표적인 문제 유형입니다.
    * 다만, 알고리즘 교재나 문제 풀이 사이트에 따라서 다르게 일컬을 수 있으므로, <br>
    코딩 테스트에서의 시뮬레이션 유형, 구현 유형, 완전 탐색 유형은 서로 유사한 점이 많다는 정도로만 기억합시다.
```python
def solution(N, moves):
    moves = moves.split(" ")
    d = { 'R': [1, 0], 'L': [-1, 0], 'U': [0, -1], 'D': [0, 1] }
    x, y = 0, 0

    for move in moves:
        dx = x + d[move][0]
        dy = y + d[move][1]

        if dx >= 0 and dy >= 0 and dx < N and dy < N:
            x, y = dx, dy

    return "{} {}".format(x + 1, y + 1)
```

---

### 문 3
> 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다. <br>
> 이때, 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
>
> 예를 들어 `K1KA5CB7`이라는 값이 들어오면 `ABCKK13`을 출력합니다.

### 답 3
* 요구사항대로 충실히 구현하면 되는 문제입니다.
* 문자열이 입력되었을 때 문자를 하나씩 확인합니다.
    * 숫자인 경우 따로 합계를 계산합니다.
    * 알파벳인 경우 별도의 리스트에 저장합니다.
* 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답니다.

```python
def solution(S):
    number = 0
    alphabet = []

    for c in S:
        if c >= '0' and c <= '9':
            number += int(c)
        else:
            alphabet.append(c)

    alphabet = ''.join(sorted(alphabet))
    return alphabet + str(number)
```