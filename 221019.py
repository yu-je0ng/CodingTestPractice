# 문자열 뒤집기
def solution(my_string):
    answer = my_string[::-1]
    return answer

# 직각삼각형 출력하기
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end="")
    print("")

# 짝수 홀수 개수
def solution(num_list):
    answer = []
    odd , even = 0 , 0
    for i , j in enumerate(num_list):
        if j % 2 == 0 :
            even += 1
        else:
            odd += 1
    answer=[even, odd]
    return answer

# 문자열 반복 출력하기 
'''
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''
