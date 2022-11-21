# 두 수의 나눗셈

def solution(num1, num2):
    answer = int((num1/ num2) * 1000)
    return answer

# 숫자 비교하기

def solution(num1, num2):
    if num1 == num2 :
        return 1
    else :
        return -1


# 분수의 덧셈

'''
첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''




# 배열 두 배 만들기

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(number*2)
    return answer
