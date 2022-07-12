# rows =  6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
#
# #테이블 만들기
# table = []
# for i in range(rows):
#     table.append([a for a in range(i*columns+1,(i+1)*columns+1)])
#
# #테이블 확인
# # for i in table:
# #     print(i)
#
# for query in queries:
#     query = [x-1 for x in query]
#     print(query)
#     #끝점
#     tmp = table[query[0]][query[1]]
#     print(tmp)

# [2,3,4,5]가 있을 때, 자기자신을 제외한 나머지 원소를 전부 곱한 값을 해당 자리에 넣어서 반환하라
s = [2,3,4,5]
for i in s:
    print(i)