

# 특이한 정렬

## 문제

정수 `n`을 기준으로 `n`과 가까운 수부터 정렬하려고 합니다. 이때 `n`으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 `numlist`와 정수 `n`이 주어질 때 `numlist`의 원소를 `n`으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

| numlist                       | n    | result                               |
| ----------------------------- | ---- | ------------------------------------ |
| [1, 2, 3, 4, 5, 6]            | 4    | [4, 5, 3, 6, 2, 1]                   |
| [10000,20,36,47,40,6,10,7000] | 30   | [36, 40, 20, 47, 10, 6, 7000, 10000] |



## 답안

```python
def solution(numlist, n):
    numlist.sort(reverse=True)
    numlist.sort(key = lambda x: abs(x-n))
    return numlist
```

- numlist를 역순으로정렬.
- lambda 함수의 값을 key로 설정해서 다시 정렬.

### ~~다중조건~~

- ~~lambda x: (abs(x-n), -x)~~

  

# 등수 매기기

## 문제

영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 영어 점수와 수학 점수를 담은 2차원 정수 배열 `score`가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

| score                                                        | result                |
| ------------------------------------------------------------ | --------------------- |
| [[80, 70], [90, 50], [40, 70], [50, 80]]                     | [1, 2, 4, 3]          |
| [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]] | [4, 4, 6, 2, 2, 1, 7] |



## 답안

```py
def solution(score):
    answer = []
    avg_list = []
    
    # 평균점수 리스트
    for i in score:
        avg_list.append((i[0]+i[1])/2)
    
    # 평균점수 리스트 큰 순으로(내림차순) 정렬
    sort_list = sorted(avg_list, reverse=True)
   
	# 정렬된 리스트에서 각 평균 점수의 인덱스를 순위로 집계
    for j in avg_list:
        answer.append(sort_list.index(j)+1)
        
    return answer
```

```python
# return sort_list, avg_list, answer
# 테스트 1 [[80, 70], [90, 50], [40, 70], [50, 80]]
sort_list 	
> [75,70,65,55]
avg_list
> [75,70,55,65]
answer
> [1,2,4,3]

# 테스트 2 [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
sort_list
> [100,95,95,75,75,40,20]
avg_list
> [75,75,40,95,95,100,20]
answer
> [4,4,6,2,2,1,7]
```





# 옹알이(1)

## 문제

머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 `babbling`이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

| babbling                                    | result |
| ------------------------------------------- | ------ |
| ["aya", "yee", "u", "maa", "wyeoo"]         | 1      |
| ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"] | 3      |

## 답안

```py
def solution(babbling):
    answer = 0
    bab_list = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for bab in bab_list:
            i = i.replace(bab, '0')
            print(i)
        if i.isdigit():
            answer += 1
    return answer
```



### replace

```py
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

> x = txt.replace("one", "three")
three three was a race horse, two two was three too.

> x = txt.replace("one", "three", 1)
three one was a race horse, two two was one too.

x = txt.replace("one", "three", 2)
three three was a race horse, two two was one too.
```





# 로그인 성공?

## 문제

머쓱이는 프로그래머스에 로그인하려고 합니다. 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 `id_pw`와 회원들의 정보가 담긴 2차원 배열 `db`가 주어질 때, 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.

- 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
- 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.

## 답안

### 오답

```
def solution(id_pw, db):
    answer = ''
    for check in db :
        if id_pw == check :
            answer = "login"
        elif id_pw[0] == check[0]:
            answer = "wrong pw"
        else : 
            answer = "fail"
    return answer
```

```
def solution(id_pw, db):
    answer = ''
    for check in db :
        if id_pw[0] == check[0] :id_pw[1] == check[1]:
            answer = "login"
        elif id_pw[0] == check[0] and id_pw[1] != check[1]:
            answer = "wrong pw"
        else : 
            answer = "fail"
    return answer
```

- 위의 모든 코드들이 test 1에서 실패 발생함.



### 수정 답안

- else가 아닌 elif로 바꿔주면 에러 발생하지 않음.

```
def solution(id_pw, db):
    answer = ''
    for check in db :
        if id_pw[0] == check[0] and id_pw[1] == check[1]:
            answer = "login"
        elif id_pw[0] == check[0] and id_pw[1] != check[1]:
            answer = "wrong pw"
        elif id_pw[0] != check[0] and id_pw[1] != check[1]:
            answer = "fail"
    return answer
```

