# 정렬 & 이진 탐색

## 정렬 ( Sorting )
> 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말합니다.
> 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됩니다.

|           | 최선의 경우 | 보통의 경우 | 최악의 경우 |                    특징                    |
| --------- | ----------- | ----------- | ----------- | ------------------------------------------ |
| 선택 정렬 | N^2         | N^2         | N^2         | 아이디어가 매우 간단                       |
| 삽입 정렬 | N           | N^2         | N^2         | 데이터가 거의 정렬되어 있을 때는 가장 빠름 |
| 퀵 정렬   | NlogN       | NlogN       | N^2         | 대부분의 경우에 가장 적합하며, 충분히 빠름 |

### 선택 정렬 ( selection sort )
> 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
* 시간 복잡도 : O( N^2 )

```python
datas = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(datas)):
    min_index = i
    for j in range(i + 1, len(datas)):
        if datas[min_index] > datas[j]:
            min_index = j
    datas[i], datas[min_index] = datas[min_index], datas[i]

print(datas)
```

### 삽입 정렬 ( insertion sort )
> 처리되지 않은 데이터를 하나씩 골라 적정한 위치에 삽입
* 시간 복잡도 : O( N^2 )

```python
datas = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(datas)):
    for j in range(i, 0, -1):
        if datas[j] < datas[j - 1]:
            datas[j], datas[j - 1] = datas[j - 1], datas[j]
        else:
            break

print(datas)
```

### 퀵 정렬 ( quick sort )
> 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
* 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나입니다.
* 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘입니다.
* 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정합니다.
* 시간 복잡도 : O( NlogN )

```python
# 일반적인 퀵 정렬

datas = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(datas, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 기준보다 큰 데이터를 찾을 때까지 반복
        while left <= end and datas[left] <= datas[pivot]:
            left += 1
        # 기준보다 작은 데이터를 찾을 때까지 반복
        while right > start and datas[right] >= datas[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 기준 데이터를 교체
        if left > right:
            datas[right], datas[pivot] = datas[pivot], datas[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            datas[left], datas[right] = datas[right], datas[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부븐에서 각각 정렬 수행
    quick_sort(datas, start, right - 1)
    quick_sort(datas, right + 1, end)

quick_sort(datas, 0, len(datas) - 1)
print(datas)
```

```python
# 파이썬의 장점을 살린 퀵 정렬

datas = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(datas):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(datas) <= 1:
        return datas
    
    # 기준은 첫 번째 원소
    pivot = datas[0]
    # 기준을 제외한 리스트
    tail = datas[1:]

    # 분할된 왼쪽 부분 ( 기준보다 작거나 같은 값 )
    left_side = [ x for x in tail if x <= pivot ]
    # 분할된 오른쪽 부분 ( 기준보다 큰 값 )
    right_side = [ x for x in tail if x > pivot ]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행후, 전체 리스트 반환
    return quick_sort(left_side) + [ pivot ] + quick_sort(right_side)

print(quick_sort(datas))
```

---
## 정렬 문제

### 문 1
* 동빈이는 두 개의 배열 A와 B를 가지고 있습니다.
  두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
* 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 
  바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 의미합니다.
* 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며,
  여러분은 동빈이를 도와야합니다.
* N, K, 배열 A, 배열 B의 정보가 주어졌을 때, 
  최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.

### 답 1
* 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소과 교체합니다.
* 배열 A는 오름차순, 배열 B는 내림차순으로 정렬합니다.
* 두 배열의 인덱스를 차례로 확인하면서, A의 원소가 B의 원소보다 작은 경우에만 교체합니다.
* 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, NlogN 알고리즘을 사용해야합니다.
```python
def solution():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 오름차순 정렬
    A.sort()
    # 내림차순 정렬
    B.sort(reverse=True)

    # 첫 번째 인덱스부터 확인하여 두 배열의 원소를 최대 K번 비교
    for i in range(K):
        # A의 원소가 B의 원소보다 작은 경우 교체
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break

    return sum(A)

print( solution() )
```

---

## 이진 탐색 ( Binary Search )
> 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
* 시간복잡도 : O( logN )

```python
# 이진 탐색 ( 재귀 함수 )
def binary_search(datas, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if datas[mid] == target:
        return mid
    # 중간점의 값보다 작은 경우 왼쪽 확인
    elif datas[mid] > target:
        return binary_search(datas, target, start, mid - 1)    
    # 중간점의 값보다 큰 경우 오른쪽 확인
    else:
        return binary_search(datas, target, mid + 1, end)
```

```python
# 이진 탐색 ( 반복문 )
def binary_search(datas, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우 중간점 인덱스 반환
        if datas[mid] == target:
            return mid
        # 중간점의 값보다 작은 경우 왼쪽 확인
        elif datas[mid] > target:
            end = mid - 1
        # 중간점의 값보다 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return -1
```

### 파이썬 이진 탐색 라이브러리

|                    |                                                                      |
| ------------------ | -------------------------------------------------------------------- |
| bisect_left(a, x)  | 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 위치를 반황   |
| bisect_right(a, x) | 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 위치를 반환 |

```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print( bisect_left(a, x) )  # 2
print( bisect_right(a, x) ) # 4
```

```python
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 갯수를 반환하는 함수
def count_by_range(datas, left_value, right_value):
    left_index = bisect_left(datas, left_value)
    right_index = bisect_right(datas, right_value)
    return right_index - left_index

datas = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(datas, 4, 4)) # 2
print(count_by_range(datas, -1, 3)) # 6
```

---

## 파라메트릭 서치 ( Parametric Search )
> 최적화 문제를 결정 문제('예' 혹은 '아니요')로 바꾸어 해결하는 기법
>   * 예시 : 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
* 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있습니다.

### 문제
* 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다.
  오늘은 떡볶이 떡을 만드는 날입니다.
  동빈이네 떡볶이 떡은 재밌게도 덕뽁이 떡의 길이가 일정하지 않습니다.
  대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.
* 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단합니다.
  높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다.
* 예를 들어 높이가 19, 14, 10, 17cm 인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것입니다.
  잘린 떡의 길이는 차례대로 4, 0, 0, 2cm 입니다. 손님은 6cm 만큼의 길이를 가져갑니다.
* 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

### 답안
* 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정하면 됩니다.
* '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 조건의 만족 여부에 따라서 탐색 범위를 좁혀서 해결할 수 있습니다.
* 절단기의 높이는 0부터 10억까지의 정수 중 하나입니다.
    * 이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 합니다.