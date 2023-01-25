# 당신은 음식점의 계산을 도와주는 점원입니다.
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재한다고 가정합니다.
# 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요.
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.

def solution(N):
    answer = 0
    coins = [500, 100, 50, 10]

    for coin in coins:
        answer += N // coin
        N %= coin
        
    return answer

print( solution(1260) )