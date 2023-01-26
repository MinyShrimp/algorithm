# 퀵 정렬

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