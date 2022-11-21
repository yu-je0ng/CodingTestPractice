# 문자열 밀기
'''
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, 
A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
'''

# 종이 자르기
def solution(M, N):
    answer = (M-1) + (M*(N-1))
    return answer

# 연속된 수의 합
'''
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 
정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
'''

# 다음에 올 숫자
def solution(common):
    answer = 0
    # 등차수열
    if (common[1] - common[0]) == (common[2] - common[1]):
        answer = common[-1] + (common[1] - common[0])
    # 등비수열
    else :
        answer = common[-1] * (common[1]/common[0])
    return answer