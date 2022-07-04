numbers = [5,0,2,7]
li = []
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        print(i,j)
        li.append(numbers[i]+numbers[j])

print(set(li))
