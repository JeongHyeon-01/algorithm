import re
s = "A man, a plan, a canal: Panama"
# 리스트 사용 317 ms
strs = []
for i in s:
    if i.isalnum():
        strs.append(i.lower())
while len(strs) > 1:
    if strs.pop() != strs.pop(0):
        print(False)

print(True)






#re모듈 사용 52ms
# s = s.lower()
# s = re.sub('[^a-z0-9]','',s)
#
# if s == s[::-1]:
#     print(True)