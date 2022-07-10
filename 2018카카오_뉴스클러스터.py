from collections import Counter

def solution(str1,str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    str1_li = []
    str2_li = []

    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_li.append(str1_low[i]+str1_low[i+1])

    for i in range(len(str2_low)-1):
        if str2_low[i].isalpha() and str2_low[i+1].isalpha():
            str2_li.append(str2_low[i]+str2_low[i+1])

    Counter1 = Counter(str1_li)
    Counter2 = Counter(str2_li)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter)==0:
        return 65536
    else:
        return int(len(inter)/len(union)*65536)
testcase =[
    ['FRANCE','french'],
    ['handshake',	'shake hands'	],
    ['aa1+aa2',	'AAAA12']
]

for str1, str2 in testcase:
    print(solution(str1, str2))