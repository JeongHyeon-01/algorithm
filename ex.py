rows =  6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

#테이블 만들기
table = []
for i in range(rows):
    table.append([a for a in range(i*columns+1,(i+1)*columns+1)])

#테이블 확인
# for i in table:
#     print(i)

for query in queries:
    query = [x-1 for x in query]
    print(query)
    #끝점
    tmp = table[query[0]][query[1]]
    print(tmp)