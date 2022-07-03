d = [1,3,2,5,4]
budget= 9
print(d.sort())
d.sort()
print(sum(d))
print(d[-1])
while sum(d) > budget:
    d.pop()
    print(d.pop())
print(len(d))