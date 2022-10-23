# 배열 자르기
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer

# 외계행성의 나이
def solution(age):
    answer = ''
    char = 'abcdefghij'
    age = list(str(age))
    for i in age :
        answer += char[int(i)]
    return answer

# 진료순서 정하기
def solution(emergency):
    answer = []
    for i in emergency:
        idx = 1
        for j in emergency:
            if i < j:
                idx += 1
        answer.append(idx)
    return answer 

# 순서쌍의 개수
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += 1
    return answer