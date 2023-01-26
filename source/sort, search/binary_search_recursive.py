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

n, target = list(map(int, input().split()))
datas = list(map(int, input().split()))

print( binary_search(datas, target, 0, n - 1) )