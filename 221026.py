# 주사위의 개수
def solution(box, n):
    answer = 1
    for i in box:
        answer *= (i//n)
    return answer

# 합성수 찾기
def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0 : cnt += 1
        if cnt >= 3 : answer += 1
    return answer

# 최대값 만들기(1)
def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    answer = numbers[-1] * numbers[-2]
    return answer

# 팩토리얼
'''
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
정수 n이 주어질 때 
다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
(i! ≤ n , 0 < n ≤ 3,628,800)
'''