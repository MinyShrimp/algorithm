# 선택 정렬 

datas = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(datas)):
    min_index = i
    for j in range(i + 1, len(datas)):
        if datas[min_index] > datas[j]:
            min_index = j
    datas[i], datas[min_index] = datas[min_index], datas[i]

print(datas)
