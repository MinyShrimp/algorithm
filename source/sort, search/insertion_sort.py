# 삽입 정렬

datas = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(datas)):
    for j in range(i, 0, -1):
        if datas[j] < datas[j - 1]:
            datas[j], datas[j - 1] = datas[j - 1], datas[j]
        else:
            break

print(datas)