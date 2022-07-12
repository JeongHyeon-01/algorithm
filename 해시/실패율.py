n=5
stages =[2, 1, 2, 6, 2, 4, 3, 3]
'''
1: 1
2: 3
3:2
4:1
5:0
'''
# 실패율 = 도달하지못한인원/스테이지에 도달한 수
# 2/5
# 스테이지에 도달한 유저가 없는 경우


# answer = {}
# length = len(stages)
# for i in range(1,n+1):
#     if length != 0:
#         cnt = stages.count(i)
#         answer[i] = cnt/length
#
#     else:
#         answer[i] = 0
# print(sorted(answer, key=lambda x : answer[x], reverse=True))
#
#
#
#
#
#








# result = {}
# length = len(stages)
# for stage in range(1, n+1):
#     if length != 0:
#         count = stages.count(stage)
#         print(count)
#         result[stage] = count / length
#         print(result)
#         length -= count
#     else:
#         result[stage] = 0
#
# print (sorted(result, key=lambda x : result[x], reverse=True))


s = ['2 A','1 B', '4 C', '1 A']
print(sorted(s))
s.sort(key =lambda x : (x.split()[1], x.split()[0]))
print(s)