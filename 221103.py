# 숫자 찾기
def solution(num, k):
    answer = 0
    my_list = list(str(num))
    if str(k) in my_list:
        answer = my_list.index(str(k)) + 1
    else :
        answer = -1
    return answer


# n의 배수 고르기
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

# 자릿수 더하기
def solution(n):
    answer = 0
    for i in list(str(n)) : 
        answer += int(i)
    return answer
    
# OX퀴즈
'''
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
'''