"""
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수,
solution을 완성해주세요.
"""
def solution(num):
    return "Even" if num % 2 ==0 or num==0 else "Odd"