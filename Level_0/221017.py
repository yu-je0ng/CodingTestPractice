# 피자 나눠 먹기(1)
def solution(n):
    answer = 0
    if n%7 == 0:
        answer = n // 7
    else:
        answer = (n//7) + 1
    return answer


# 피자 나눠 먹기(2)
'''
머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 
피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
'''

# 피자 나눠 먹기(3)
def solution(slice, n):
    piz = 1
    while (slice * piz) < n :
        piz += 1
    return piz

# 배열의 평균값
def solution(numbers):
    return sum(numbers)/len(numbers)