import re
s = "A man, a plan, a canal: Panama"






#re모듈 사용 52ms
s = s.lower()
s = re.sub('[^a-z0-9]','',s)

if s == s[::-1]:
    print(True)