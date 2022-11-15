# 저주의 숫자 3
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer) :
            answer += 1
    return answer

# 평행
def solution(dots):
    parallel = 0

    if (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) == (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0]): parallel += 1
    elif (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]) == (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0]): parallel += 1
    
    if parallel != 0:
        answer = 1
    else:
        answer = 0
    return answer

# 겹치는 선분의 길이
def solution(lines):
    line_list = []
    answer = 0
    for i in lines:
        print(i)
        print(type(i[0]))
        print(type(i[1]))
        for j in range(i[0], i[1]):
            # print(j)
            if j not in line_list:
                line_list.append(j)
            else:
                line_list.remove(j)
                answer += 1
    return answer

# 유한소수 판별하기
def solution(a, b):
    answer = 0
    b_num = []
    # 기약분수
    for i in range(2, min(a, b)+1):
        while(a%i ==0) & (b%i ==0):
            a = a // i
            b = b // i
    # 분모 소인수 
    for j in range(2, b+1):
        while b % j == 0:
            b = b //j
            b_num.append(j)
    # 2,5 아닌 소인수 확인
    answer = 1
    for i in b_num:
        if i not in [2,5]:
            answer += 1
            break

    return answer