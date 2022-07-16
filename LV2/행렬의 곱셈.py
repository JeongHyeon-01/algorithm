arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]


answer =[]
for i in range(len(arr1)):
    temp_li = []
    for j in range(len(arr2[0])):
        temp = 0
        for k in range(len(arr2)):
            temp += arr1[i][k] * arr2[k][j]
        temp_li.append(temp)
    answer.append(temp_li)
print(answer)
