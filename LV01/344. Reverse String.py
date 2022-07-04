s = ["h","e","l","l","o"]

#s[::-1]도 가능하지만 리트코드에서 제한된다.
#1. 파이썬스럽게 풀기 299ms
print(s.reverse())



#투포인터 300ms
left, right = 0, len(s)-1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -=1
    print(s)

