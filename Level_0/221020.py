# 특정 문자열 제거하기
def solution(my_string, letter):
    answer = ''
    for i in range(0, len(my_string)):
        if letter != my_string[i]:
            answer += my_string[i]
    return answer

# 각도기
def solution(angle):
    answer = 0
    if 0 < angle < 90 :
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180 :
        answer = 3
    elif angle == 180 :
        answer = 4
    return answer

# 양꼬치
def solution(n, k):
    answer = 12000 * n + 2000 * (k - (n // 10))
    return answer

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i % 2 == 0 :
            answer += i
    return answer