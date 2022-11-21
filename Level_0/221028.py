# 컨트롤 제트
'''
숫자들이 공백으로 구분된 문자열이 주어집니다. 
문자열에 있는 숫자를 차례대로 더하려고 합니다. 
이 때 “Z”가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
숫자와 “Z”로 이루어진 문자열 s가 주어질 때, 
머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
'''


# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist : answer.append(len(i))
    return answer

# 중복된 문자 제거
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer

# 삼각형의 완성조건(1)
def solution(sides):
    answer = 0
    sides.sort()
    if sides[-1] < sum(sides[0:2]) : answer = 1
    else : answer = 2
    return answer