# 7의 개수
def solution(array):
    answer = str(array).count("7")
    return answer

# 잘라서 배열로 저장하기
'''
문자열 my_str과 n이 매개변수로 주어질 때, 
my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.
'''

# 중복된 숫자 개수
## 방법1
def solution(array, n):
    answer = 0
    for i in array: 
        if i == n: 
            answer +=1
    return answer

## 방법2
def solution(array, n):
    return array.count(n)

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height: answer += 1
    return answer