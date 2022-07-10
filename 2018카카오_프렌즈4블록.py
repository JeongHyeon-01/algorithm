'''
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
'''
import numpy as np

# board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# n=4
# m=5
# 찾기
def solution(m,n,board):
    answer= 0
    def find(board):
        target = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    target.update({(i,j),(i+1,j),(i,j+1),(i+1,j+1)})
        return target
    #지우기
    def remove(target,board):
        board = [list(row) for row in board]
        for loc in target:
            i, j = loc
            board[i][j] = ''
        return board
    #아래로 내리기
    def move(board):
        cnt = 0
        for i in range(m-1):
            for j in range(n):
                if board[i][j] and not board[i+1][j]:
                    board[i][j], board[i+1][j] = board[i+1][j],board[i][j]
                    cnt += 1
        return cnt, board

    while True:
        target = find(board)
        answer += len(target)
        board = remove(target,board)
        cnt = 1
        while cnt:
            cnt, board = move(board)
        if not cnt and not len(target):
            break

    return answer

testcase = [4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]]
for test in testcase:
    print(solution(n,m,board))