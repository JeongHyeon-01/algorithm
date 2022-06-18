n=3
m=12
"""
최대공약수
n = 1,3
m = 1,2,3,4,6,12
GDC = 3

최소 공배수
n = 3 6  9 12 
m = 12
LCM = 12
"""

def gdc(x,y):
    while y :
        x,y = y, x % y
    return x

def lcm(x,y):
    return x*y // gdc(x,y)

def solution(n, m):
    return [gdc(n,m),lcm(n,m)]