# 문자열안에 문자열
def solution(str1, str2):
    answer = 0
    if str2 in str1 : answer = 1
    else : answer = 2
    return answer

# 제곱수 판별하기
'''
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, 
n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
'''

# 세균 증식
'''
어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
'''

# 문자열 정렬하기
def solution(my_string):
    answer = ''.join(sorted(my_string.lower()))
    return answer