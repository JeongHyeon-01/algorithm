# print(bin(9))
# print(bin(30))
# print(bin(9)+bin(30))
#
# print(bin(9 | 30)[2:].replace('1','#').replace('0','#'))

arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
n=5
for i, j  in zip(arr1, arr2):
    print(bin(i | j)[2:].zfill(n).replace('1','#').replace('0',' '))
    # print(bin(i | j)[2:].zfill(n))

'''
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1,arr2):
        answer.append(bin(i|j)[2:].zfill(n).replace('1','#').replace('0',' '))
    return answer
'''