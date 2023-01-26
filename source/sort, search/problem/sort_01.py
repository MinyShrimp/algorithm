# * 동빈이는 두 개의 배열 A와 B를 가지고 있습니다.
#   두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
# * 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 
#   바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 의미합니다.
# * 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며,
#   여러분은 동빈이를 도와야합니다.
# * N, K, 배열 A, 배열 B의 정보가 주어졌을 때, 
#   최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.

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