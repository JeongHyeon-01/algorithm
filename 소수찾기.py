'''
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
'''
n = 10
'''
2,3,5,7
'''
count = 0
for n in range(2, n + 1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        count += 1
print(count)

num = set(range(2, n + 1))
print(num)

for i in range(2, n + 1):
    print(i)
    if i in num:
        num -= set(range(2 * i, n + 1, i))
        print(set(range(2 * i, n + 1, i)))

print(len(num))