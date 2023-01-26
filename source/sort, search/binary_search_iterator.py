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

n, target = list(map(int, input().split()))
datas = list(map(int, input().split()))

print( binary_search(datas, target, 0, n - 1) )