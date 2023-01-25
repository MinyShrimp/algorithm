# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다.
# 이때, 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 
# 예를 들어 `K1KA5CB7`이라는 값이 들어오면 `ABCKK13`을 출력합니다.

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

print( solution("K1KA5CB7") ) # ABCKK13
print( solution("AJKDLSI412K4JSJ9D") ) # ADDIJJJKKLSS20