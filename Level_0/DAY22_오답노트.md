# 저주의 숫자 3

## 문제

3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.

| 10진법 | 3x 마을에서 쓰는 숫자 |
| ------ | --------------------- |
| 1      | 1                     |
| 2      | 2                     |
| 3      | 4                     |
| 4      | 5                     |
| 5      | 7                     |
| 6      | 8                     |
| 7      | 10                    |

정수 `n`이 매개변수로 주어질 때, `n`을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.

##### 입출력 예

| n    | result |
| ---- | ------ |
| 15   | 25     |
| 40   | 76     |



## 답안

```py
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer) :
            answer += 1
    return answer
```

- 언더 스코어 사용해서 n의 길이 만큼 for문 실행.

  - answer += 1을 통해 숫자 1씩 더하면서 카운트

  - 단, answer의 값이 3의 배수이거나 3일때 아니게 될때까지 while문으로 answer을 더해줌.

    | n = 6 | for          | while       | answer |
    | ----- | ------------ | ----------- | ------ |
    | 1     | answer += 1  | pass        | 1      |
    | 2     | answer += 1  | pass        | 2      |
    | 3     | answer += 1  | answer +=1  | 4      |
    | 4     | answer += 1  | pass        | 5      |
    | 5     | answer += 1  | answer +=1  | 7      |
    | 6     | answer += 1  | pass        | 8      |
    | 7     | answer + = 1 | answer += 1 | 10     |

    



# 평행

## 문제

점 네 개의 좌표를 담은 이차원 배열  `dots`가 다음과 같이 매개변수로 주어집니다.

- [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

##### 입출력 예

| dots                              | result |
| --------------------------------- | ------ |
| [[1, 4], [9, 2], [3, 8], [11, 6]] | 1      |
| [[3, 5], [4, 1], [2, 4], [5, 10]] | 0      |



## 답안

```py
def solution(dots):
    parallel = 0

    if (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) == (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0]): parallel += 1
    elif (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]) == (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0]): parallel += 1
    
    if parallel != 0:
        answer = 1
    else:
        answer = 0
    return answer
```

- 선분이 평행이 되는 패턴이 존재함.
  - ` (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0]) == (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])`
    - 4 - 2 / 1 - 9 == 8 - 6 / 11 -3 
  - `(dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0]) == (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0])`
    - 4 - 8 / 1 - 3 == 2 - 6 / 9 - 11



# 겹치는 선분의 길이

## 문제

빨간색, 초록색, 파란색 선분이 x축 위에 있습니다. 세 선분의 x좌표 시작과 끝이 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 `lines`가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를return 하도록 solution 함수를 완성해보세요.

`lines`가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
![스크린샷 2022-08-08 오후 5.08.46.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/4feda8d5-aa8f-4a55-8afc-db776e2f9bcd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-08-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.08.46.png)

선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 2만큼 겹쳐있습니다.

| lines                     | result |
| ------------------------- | ------ |
| [[0, 1], [2, 5], [3, 9]]  | 2      |
| [[-1, 1], [1, 3], [3, 9]] | 0      |
| [[0, 5], [3, 9], [1, 10]] | 8      |



## 답안

```py
def solution(lines):
    line_list = []
    answer = 0
    for i in lines:
        for j in range(i[0], i[1]):
            if j not in line_list:
                line_list.append(j)
            else:
                line_list.remove(j)
                answer += 1
    return answer
```

- "두 개 이상 겹치는 곳"이 어느 곳 인지가 아닌 단순히 겹치는 부분의 길이를 count하기만 하면 되므로 line_list를 만들어서 중복되면 answer에 +1씩 해줌.

  | for i in [[0, 1], [2, 5], [3, 9]] : | for j in range(i[0], i[1]): | if j not in line_list:         | else:                                 |
  | ----------------------------------- | --------------------------- | ------------------------------ | ------------------------------------- |
  | i = [0, 1]                          | j = 0                       | line_list = [0]                |                                       |
  | i = [2, 5]                          | j = 2                       | line_list = [0, 2]             |                                       |
  |                                     | j = 3                       | line_list = [0, 2, 3]          |                                       |
  |                                     | j = 4                       | line_list = [0, 2, 3, 4]       |                                       |
  | i = [3, 9]                          | j = 3                       |                                | line_list = [0, 2, 4]<br />answer = 1 |
  |                                     | j = 4                       |                                | line_list = [0, 2]<br />answer = 2    |
  |                                     | j = 5                       | line_list = [0, 2, 5]          |                                       |
  |                                     | j = 6                       | line_list = [0, 2, 5, 6]       |                                       |
  |                                     | j = 7                       | line_list = [0, 2, 5, 6, 7]    |                                       |
  |                                     | j = 8                       | line_list = [0, 2, 5, 6, 7, 8] |                                       |

  



# 유한소수 판별하기

## 문제

소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

- 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.

두 정수 `a`와 `b`가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

| a    | b    | result |
| ---- | ---- | ------ |
| 7    | 20   | 1      |
| 11   | 22   | 1      |
| 12   | 21   | 2      |



## 답안

```
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
```

- 처음에 `# 2,5 아닌 소인수 확인`부분에서 for문이 아닌 아래와 같은 if문을 사용함

  ```py
      if 2 or 5 in b_num :
          answer = 1
      else: 
          answer = 2
  ```

  - 그 결과, test case 3은 실패가 발생함. 

    ```
    테스트 3
    입력값 〉	12, 21
    기댓값 〉	2
    실행 결과 〉	실행한 결괏값 1이 기댓값 2과 다릅니다.
    출력 〉	[7]
    ```

- 스터디원 조언을 통해 해당 조건문이 잘 못되었음을 알게 되었음.

  - "2 또는 5가 들어있을 때 모두 가능하다" 즉, 유한 소수 조건인 "기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다."와 맞지 않음을 알게됨.