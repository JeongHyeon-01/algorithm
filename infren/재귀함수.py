#1 ~ N까지의 합과 곱
n=100
x = 0

import time
#1~ N까지 합
start = time.time()
for i in range(1,n+1):
    x += i
end = time.time()
print(f"{x},{end - start:.5f} sec")
#시그마 정의 를 이용
start = time.time()
x = n*(n+1)//2
end = time.time()
print(f"{x},{end - start:.5f} sec")
#1~N까지의 곱
start = time.time()
for i in range(1,n+1):
    x *= i
print(f"{x},{end - start:.5f} sec")
end = time.time()
x = n*(n+1)//2