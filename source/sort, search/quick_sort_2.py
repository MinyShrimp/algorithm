# 퀵 정렬 ( 파이써닉 )

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