'''
1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
'''
num = 16
answer = 0
while True:
    if num == 1:
        break
    if answer == 500:
        break
    if num %2 == 0:
        num //= 2
        answer += 1
    else:
        num = num * 3 + 1
        answer +=1
print(answer if answer != 500 else -1)

for i in range(500):
    num = num /2 if num % 2 ==0 else num * 3 + 1
    if num == 1:
        print(i + 1)
print(-1)