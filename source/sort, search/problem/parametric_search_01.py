# * 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했습니다.
#   오늘은 떡볶이 떡을 만드는 날입니다.
#   동빈이네 떡볶이 떡은 재밌게도 덕뽁이 떡의 길이가 일정하지 않습니다.
#   대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.
# * 절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단합니다.
#   높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다.
# * 예를 들어 높이가 19, 14, 10, 17cm 인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것입니다.
#   잘린 떡의 길이는 차례대로 4, 0, 0, 2cm 입니다. 손님은 6cm 만큼의 길이를 가져갑니다.
# * 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

# 손님에게 줄 길이 구하기
def get_height(datas, height):
    sum_height = 0
    for d in datas:
        sum_height += max(0, d - height)
    return sum_height

def binary_search(datas, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    height = get_height(datas, mid)
    
    if height == target:
        return mid
    elif height < target:
        return binary_search(datas, target, left, mid - 1)
    else:
        return binary_search(datas, target, mid + 1, right)

def solution():
    n, m = map(int, input().split())
    rices = list(map(int, input().split()))

    max_h = max(rices)
    return binary_search(rices, m, 0, max_h)

print( solution() )