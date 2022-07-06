cnt = 0
str(list(range(1,1001))).count('8')

print(str(list(range(1,10001))).count('8'))

for i in range(10001):
    if '8' in str(i):
        cnt +=str(i).count('8')
print(cnt)

print(str([i for i in range(10001)]).count('8'))