# 가까운 수
def solution(array, n):
    answer = ''
    abs_list = []
    array = sorted(array)
    for i in array:
        abs_list.append(abs(i - n)) 
    answer = array[abs_list.index(min(abs_list))]
    return answer

# 369게임
def solution(order):
    answer = 0
    syg = ["3", "6", "9"]
    for i in str(order):
        if i in syg:
            answer += 1
    return answer

# 암호해독
def solution(cipher, code):
    answer = ''.join(cipher[i] for i in range(code-1, len(cipher), code))
    # for i in range(code-1, len(cipher), code):
    #     print(cipher[i])
    #     print(i)
    return answer

# 대문자와 소문자
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        if i.islower():
            answer += i.upper()
    return answer