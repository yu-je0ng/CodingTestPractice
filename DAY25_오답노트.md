# 문자열 밀기

## 문제

문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 `A`와 `B`가 매개변수로 주어질 때, `A`를 밀어서 `B`가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 밀어서 `B`가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

| A       | B       | result |
| ------- | ------- | ------ |
| "hello" | "ohell" | 1      |
| "apple" | "elppa" | -1     |



## 답안

```py
def solution(A, B):
    for i in range(len(A)):
        answer = ''
        for j in range(len(A)):
            answer += A[j-i]
        #     print(f"j:{j} , i:{i}, j-i:{j-i}")
        # print(answer)
        if answer == B:
            return i
    else:
        return -1
    
```





# 연속된 수의 합

## 문제

연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 `num`과 `total`이 주어집니다. 연속된 수 `num`개를 더한 값이 `total`이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

| num  | total | result           |
| ---- | ----- | ---------------- |
| 3    | 12    | [3, 4, 5]        |
| 5    | 15    | [1, 2, 3, 4, 5]  |
| 4    | 14    | [2, 3, 4, 5]     |
| 5    | 5     | [-1, 0, 1, 2, 3] |



## 답안

```py
def solution(num, total):
    answer = []
    center = total//num
    start = center-(num//2)
    # 배열이 짝수 일때
    if num % 2 == 0:
        answer = list(range(start+1, start+num+1))
    # 배열이 홀수 일때
    else :
        answer = list(range(start, start+num))
    return answer
```

