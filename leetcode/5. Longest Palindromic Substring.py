s = "babad"
answer = ""
#
if len(s) <= 1:
    print(s)

i, l = 0, 0
for j in range(len(s)):
    if s[j - l: j + 1] == s[j - l: j + 1][::-1]:
        i, l = j - l, l + 1
    elif j - l > 0 and s[j - l - 1: j + 1] == s[j - l - 1: j + 1][::-1]:
        i, l = j - l - 1, l + 2
print(s[i: i + l])

# def expend(left:int, right:int):
#     while left >=0 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#         print(s[left + 1:right])
#
#     if len(s)<2 or s == s[::-1]:
#         print(s)
#
#
# )