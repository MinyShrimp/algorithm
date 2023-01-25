## 스택 ( Stack ) 자료구조
> 후입선출 (LIFO) <br>
> 입구와 출구가 동일한 형태로 스택을 시각화 할 수 있습니다.

### 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
* 5
* 5 2
* 5 2 3
* 5 2
* 5 2 1
* 5 2 1 4
* 5 2 1

```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 최상단 원소부터 출력
# [1, 2, 5]
print(stack[::-1])

# 최하단 원소부터 출력
# [5, 2, 1]
print(stack)
```

---

## 큐 ( Queue ) 자료구조
> 선입선출 (FIFO) <br>
> 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있습니다.

### 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
* 5
* 5 2
* 5 2 3
* 2 3
* 2 3 1
* 2 3 1 4
* 3 1 4

```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 먼저 들어온 순서대로 출력
# [3, 1, 4]
print(queue)
queue.reverse()
# 나중에 들어온 순서대로 출력
# [4, 1, 3]
print(queue)
```

---

## 재귀 함수 ( Recursive Function )
> 자기 자신을 다시 호출하는 함수를 의미합니다.

```python
def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()

recursive_function()
```

### 재귀 함수의 종료 조건
* 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 합니다.
* 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있습니다.
```python
def recursive_function(i):
    if i == 100:
        return 
    print(i, ': 재귀 함수를 호출합니다')
    recursive_function(i + 1)
    print(i, ': 재귀 함수를 종료합니다.')

recursive_function(1)
```

--- 

## 팩토리얼( factorial ) 구현 예제

```python
# 반복으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀함수로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
```