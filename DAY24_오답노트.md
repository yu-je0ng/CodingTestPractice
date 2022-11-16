# 치킨 쿠폰

## 문제

프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 시켜먹은 치킨의 수 `chicken`이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

| chicken | result |
| ------- | ------ |
| 100     | 11     |
| 1,081   | 120    |



## 답안

- while문을 생각하는데 많은 시간을 소비했음.

```py
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
```

# 이진수 만들기

## 문제

이진수를 의미하는 두 개의 문자열 `bin1`과 `bin2`가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

| bin1   | bin2   | result  |
| ------ | ------ | ------- |
| "10"   | "11"   | "101"   |
| "1001" | "1111" | "11000" |

입출력 예 #1

- 10 + 11 = 101 이므로 "101" 을 return합니다.

입출력 예 #2

- 1001 + 1111 = 11000 이므로 "11000"을 return합니다.



## 답안

### 내장함수 사용

```
def solution(bin1, bin2):
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    return bin(bin1+bin2)[2:]
```

```
return bin1, bin2
> [2,3]
> [9,15]

return bin(bin1+bin2)
> 0b101
> 0b11000
```

- 2진수: 0b
- 8진수: 0o
- 16진수: 0x





### 내장함수 미사용

- 내장함수를 사용하지 않기 위해 코드를 짜는 시간이 많이 들었음.

```
def solution(bin1, bin2):
    answer = ''
    cnt_bin1, cnt_bin2 = 0, 0
    rever_bin1 = reversed(bin1)
    rever_bin2 = reversed(bin2)
    
    # 인덱스로 10진수 변환
    ## bin1
    for i, val in enumerate(rever_bin1):
        cnt = int(val) * pow(2, i)
        cnt_bin1 = cnt_bin1 + cnt
    ## bin2
    for i, val in enumerate(rever_bin2):
        cnt = int(val) * pow(2, i)
        cnt_bin2 = cnt_bin2 + cnt    

    # 10진수 더하기
    total = cnt_bin1 + cnt_bin2
    
    # total이 0일때(test8번)
    if total == 0 :
        answer = '0'
    
    # 10진수 -> 2진수 변환
    while total > 0 :
        answer += str(total % 2)
        total = total // 2
    
    
    return answer[::-1]
```





# k의 개수

## 문제

1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 `i`, `j`, `k`가 매개변수로 주어질 때, `i`부터 `j`까지 `k`가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

| i    | j    | k    | result |
| ---- | ---- | ---- | ------ |
| 1    | 13   | 1    | 6      |
| 10   | 50   | 5    | 5      |
| 3    | 10   | 2    | 0      |

## 답안

```py
def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        if str(k) in str(num) :
            answer += str(num).count(str(k))
    return answer
```



### 오답

- if문을 통해 1을 그냥 한번만 더 했을 때, test case 1번째에서 11의 경우  2번 더해져야 하지만, 1번만 더해져 오류가 발생한다.

```py
def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        if str(k) in str(num) :
            answer += 1
    return answer
```

- 아래와 같이 리스트화를 시도했으나, 굳이 list화를 할 필요가 없다는 생각이 들었다.
  - 그래서 답안과 같이 리스트를 빼고 처음 방식에서 +1이 아닌 count함수를 사용해서 k의 개수를 직접 answer에 더하는 방식을 적용했다.
  - list가 아닌 str문자열에서도 정상적으로 구해진다는 것을 알게되었다.

```py
def solution(i, j, k):
    answer = 0
    list_num = []
    for num in range(i, j+1):
        list_num.append(list(str(num)))
    for cnt in list_num :
        if str(k) in cnt: answer += str(cnt).count(str(k))
    return answer
```

