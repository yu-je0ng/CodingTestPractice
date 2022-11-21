# 숨어있는 숫자의 덧셈(2)

## 문제

문자열 `my_string`이 매개변수로 주어집니다. `my_string`은 소문자, 대문자, 자연수로만 구성되어있습니다. `my_string`안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

| my_string       | result |
| --------------- | ------ |
| "aAb1B2cC34oOp" | 37     |
| "1a2b3c4d123Z"  | 133    |



## 답안

```py
def solution(my_string):
    answer = 0
    num_str = ''
    for i in my_string:
        if i.isdigit():
            num_str += i
        elif len(num_str): 
            answer += int(num_str)
            num_str = ''
            
    if len(num_str):
        answer += int(num_str)
        
    return answer
```

-   "aAb1B2cC***<u>34o</u>***Op"
    -   if s.isdigit(): # 숫자가 나타나면 num_str에 넣어줌.
        -   3도 넣고 4도 넣는데, 다음 o이 s가 될 때 o은 문자열이므로 if문이 아닌 elif문을 읽고 그 전에 num_str에 넣어둔 34를 숫자로 변환시켜서 answer에 더해줌.

### 코드 단순화(import re)

```
import re

def solution(my_string):
    answer = 0
    nums = re.findall('\d+', my_string)
    for i in nums:
        answer += int(i)
    return answer
```







# 안전지대

## 문제

다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

![image.png](C:\CodingTestPractice\assets\221014.py)

지뢰는 2차원 배열 `board`에 1로 표시되어 있고 `board`에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 `board`가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.



| [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]] | 16   |
| ------------------------------------------------------------ | ---- |
| [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]] | 13   |
| [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]] | 0    |

입출력 예 #1

-   (3, 2)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선 총 8칸은 위험지역입니다. 따라서 16을 return합니다.

입출력 예 #2

-   (3, 2), (3, 3)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선은 위험지역입니다. 따라서 위험지역을 제외한 칸 수 13을 return합니다.

입출력 예 #3

-   모든 지역에 지뢰가 있으므로 안전지역은 없습니다. 따라서 0을 return합니다.



## 답안





# 삼각형의 완성조건(2)

## 문제

선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

-   가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.

삼각형의 두 변의 길이가 담긴 배열 `sides`이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.



## 답안

```py
def solution(sides):
    sides.sort()
    a , b = sides[1]+sides[0] , sides[1]-sides[0]
    return a - b - 1
```





# 외계어 사전

## 문제

PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 `spell`과 외계어 사전 `dic`이 매개변수로 주어집니다. `spell`에 담긴 알파벳을 한번씩만 모두 사용한 단어가 `dic`에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

| ["p", "o", "s"]      | ["sod", "eocd", "qixm", "adio", "soo"]  | 2    |
| -------------------- | --------------------------------------- | ---- |
| ["z", "d", "x"]      | ["def", "dww", "dzx", "loveaw"]         | 1    |
| ["s", "o", "m", "d"] | ["moos", "dzx", "smm", "sunmmo", "som"] | 2    |

입출력 예 #1

-   "p", "o", "s" 를 조합해 만들 수 있는 단어가 `dic`에 존재하지 않습니다. 따라서 2를 return합니다.

입출력 예 #2

-   "z", "d", "x" 를 조합해 만들 수 있는 단어 "dzx"가 `dic`에 존재합니다. 따라서 1을 return합니다.

입출력 예 #3

-   "s", "o", "m", "d" 를 조합해 만들 수 있는 단어가 `dic`에 존재하지 않습니다. 따라서 2을 return합니다.



## 답안

-   dic안의 단어들의 알파벳 순서를 정렬
    -   알파벳 순서대로 정렬된 spell로 만들어진 단어와 비교하여 결과 값 도출

```py
def solution(spell, dic):
    sort_spell = ''.join(sorted(spell))
    sort_dic = []
    for i in dic:
        sort_dic.append(''.join(sorted(i)))
    if sort_spell in sort_dic:
        return 1
    else:
        return 2
```

