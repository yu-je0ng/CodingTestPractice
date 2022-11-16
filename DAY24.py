# 치킨 쿠폰
def solution(chicken):
    answer = 0
    coupon = chicken
    
    # 10마리 이하일때
    if chicken < 10 :
        return answer
    else :
        # 쿠폰이 10개 이상이 아닐때 까지
        while coupon >= 10:
            eat = coupon // 10
            # 쿠폰을 통해 먹은 치킨
            answer += eat
            # 남은 쿠폰 + 서비스치킨으로 발급된 쿠폰
            coupon = coupon%10 + eat
            
    return answer 

# 이진수 더하기
'''
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

'''

# A로 B만들기
def solution(before, after):
    answer = 0
    a = sorted(list(after))
    b = sorted(list(before))
    if a == b : 
        return 1
    else: return 0



# k의 개수
def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        if str(k) in str(num) :
            answer += str(num).count(str(k))
    return answer