s = [1,3,4,8,13,17,20]
a = []
m = max(s)
idx = 0
for i in range(len(s)-1):
    if m > s[i+1] - s[i]:
        idx = i
        m = s[i+1] -s[i]

print(s[idx], s[idx+1])

ss = [3,4,8,13,17,20]
print(sorted(list(zip(s,ss)), key=lambda i :i[1]-i[0]))
