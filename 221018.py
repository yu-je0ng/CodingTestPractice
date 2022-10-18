# 옷가게 할인 받기
def solution(price):
    if price >= 500000:
        price = int(price * 0.8)
    elif 300000 <= price < 500000:
        price = int(price * 0.9)
    elif price >= 100000: 
        price = int(price * 0.95)
    return price

# 아이스 아메리카노
def solution(money):
    answer = []
    cup = money // 5500
    cash = money % 5500
    answer = [cup, cash]
    return answer

# 나이 출력
def solution(age):
    answer = 0
    now = 2022
    answer = now - age + 1
    return answer

# 배열 뒤집기
'''
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
'''
