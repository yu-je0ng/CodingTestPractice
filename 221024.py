# 개미군단
'''
개미 군단이 사냥을 나가려고 합니다. 
개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다. 
장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 
예를 들어 체력 23의 여치를 사냥하려고 할 때, 
일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 
사냥감의 체력 hp가 매개변수로 주어질 때, 
사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.
'''
# 모스부호(1)
'''
머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다. 
그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다. 
문자열 letter가 매개변수로 주어질 때, 
letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
'''

# 가위 바위 보
def solution(rsp):
    answer = ''
    rsp = list(rsp)
    for i in rsp:
        if i ==  "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        else :
            answer += "2"
    return answer

# 구슬을 나누는 경우의 수
def solution(balls, share):
    answer = 0
    n, m1, m2 = 1, 1, 1
    for i in range(1, balls+1):
        n = n * i
    for j in range(1, (balls-share)+1):
        m1 = m1 * j
    for k in range(1, share+1):
        m2 = m2 * k
    answer = n/(m1*m2)
    return answer