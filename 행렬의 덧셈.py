arr1, arr2 = [[1,2],[2,3]],[[3,4],[5,6]]

for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        arr1[i][j] += arr2[i][j]
print(arr1)