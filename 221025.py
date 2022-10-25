# 점의 위치 구하기
def solution(dot):
    answer = 0
    if dot[0] > 0 and dot[1] > 0: answer = 1
    if dot[0] < 0 and dot[1] > 0: answer = 2
    if dot[0] < 0 and dot[1] < 0: answer = 3
    if dot[0] > 0 and dot[1] < 0: answer = 4
    return answer


# 2차원으로 만들기
'''
정수 배열 num_list와 정수 n이 매개변수로 주어집니다.
num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 
2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.
'''

# 공 던지기
'''
머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다. 
공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, 
k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.
'''

# 배열 회전시키기
def solution(numbers, direction):
    answer = []
    if direction == "right" : answer = [numbers[-1]] + numbers[0:-1]
    else : answer = numbers[1:] + [numbers[0]]
    return answer 