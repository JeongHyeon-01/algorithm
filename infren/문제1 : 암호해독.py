'''
모든 알고리즘을 해독할 수 있는 알고리즘 7 원석를 보유한 알고리즘 제왕 파이와 썬은 죽기 전, 이 보물에 '암호'를 걸어 세계 어딘가에 묻어놨다고 공표하였다. 그가 남긴 문자는 아래와 같다
섬으로 향하라!

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(1)와 달(0),
Code의 세상 안으로!(En-Coding)
'''
# ord() : 문자 -> 숫자
# chr() : 숫자 -> 문자
text = [
'   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   '
]
l = []
for i in text:
    l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

print(''.join(l))

print(''.join([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text]))

s = [i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]
print(list(map(lambda x:chr(int(x, 2)),s)))

def f(x):
    return chr(int(x, 2))
print(list(map(f,s)))