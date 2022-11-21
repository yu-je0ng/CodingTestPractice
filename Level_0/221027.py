# 모음 제거
def solution(my_string):
    vow = ['a', 'e', 'i', 'o', 'u']
    for i in vow:
        my_string = my_string.replace(i, '')
    return my_string

# 문자열 정렬하기(1)
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdecimal() : answer.append(int(i))
    answer.sort()
    return answer

# 숨어있는 숫자의 덧셈(1)
def solution(my_string):
    answer = 0
    list = sorted([int(i) for i in my_string if i.isdigit()])
    for i in list:
        answer += i
    return answer


# 소인수분해
'''
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
따라서 12의 소인수는 2와 3입니다. 
자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''