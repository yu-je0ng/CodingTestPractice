# 직사각형 넓이 구하기

## 문제

2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 `dots`가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요

```
[[1, 1], [2, 1], [2, 2], [1, 2]]	1
[[-1, -1], [1, 1], [1, -1], [-1, 1]]	4
```

## 답안

```
def solution(dots):
    dots.sort()
    answer = (dots[0][1]-dots[1][1]) * (dots[0][0]-dots[3][0])
    return answer
```



# 캐릭터 좌표 구하기

## 문제

머쓱이는 RPG게임을 하고 있습니다. 게임에는 `up`, `down`, `left`, `right` 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 예를 들어 [0,0]에서 `up`을 누른다면 캐릭터의 좌표는 [0, 1], `down`을 누른다면 [0, -1], `left`를 누른다면 [-1, 0], `right`를 누른다면 [1, 0]입니다. 머쓱이가 입력한 방향키의 배열 `keyinput`와 맵의 크기 `board`이 매개변수로 주어집니다. 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.

-   **[0, 0]은 `board`의 정 중앙에 위치합니다. 예를 들어 `board`의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.**

| ["left", "right", "up", "right", "right"] | [11, 11] | [2, 1]  |
| ----------------------------------------- | -------- | ------- |
| ["down", "down", "down", "down", "down"]  | [7, 9]   | [0, -4] |



## 오답

-   맵의 크기 고려하지 않음

```py
def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i == 'up': answer[1] += 1
        elif i == 'down' : answer[1] -= 1
        elif i == 'left' : answer[0] -= 1
        elif i == 'right' : answer[0] +=1
    return answer
```



## 답안

-   board 를 고려
    -   캐릭터는 정중앙에서 위치해서 이동을 시작하기 때문에 캐릭터가 움직을 수 있는 최대 범위를 구하기 위해서는 주어진 값에서 2를 나눠줘야함. 
    -   또한 홀수 값이 있을 수 있기 때문에 나눠준 값의 몫만을 취해야 됨.

```py
def solution(keyinput, board):
    answer = [0,0]
    max_w = board[0]//2
    max_h = board[1]//2
    for i in keyinput:
        if i == "up" and answer[1] < max_h:
            answer[1] +=1
        elif i == "down" and answer[1] > -max_h:
            answer[1] -= 1
       	elif i == "left" and answer[0] > -max_w:
            answer[0] -= 1
        elif i == "right" and answer[0] < max_w:
            answer[0] += 1
    return answer
```



# 최대값 만들기(2)

## 문제

정수 배열 `numbers`가 매개변수로 주어집니다. `numbers`의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

| [1, 2, -3, 4, -5]         | 15   |
| ------------------------- | ---- |
| [0, -31, 24, 10, 1, 9]    | 240  |
| [10, 20, 30, 5, 5, 20, 5] | 600  |



## 답안

```
def solution(numbers):
    sort_num = sorted(numbers)
    if sort_num[0]*sort_num[1] < sort_num[-1]*sort_num[-2]:
        return sort_num[-1]*sort_num[-2]
    else : return sort_num[0]*sort_num[1]
```

### 코드 단순화

```
def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
```



# 다항식 더하기

## 문제

한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 `polynomial`이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

| polynomial   | result   |
| ------------ | -------- |
| "3x + 7 + x" | "4x + 7" |
| "x + x + x"  | "3x"     |

입출력 예 #1

-   "3x + 7 + x"에서 동류항끼리 더하면 "4x + 7"입니다.

입출력 예 #2

-   "x + x + x"에서 동류항끼리 더하면 "3x"입니다.



## 접근

-   x의 계수와 상수항을 나눠줘야 한다고 생각함.

    ```
    def solution(polynomial):
        answer = ''
        x_list = []
        num_list = []
        poly_list = polynomial.split("+")
        
        for i in poly_list :
            if 'x' in i : x_list.append(i)
            elif i.isdigit()  : num_list.append(i)
        
        for j in x_list:
            print(j)
        
        return x_list, num_list
    ```

    