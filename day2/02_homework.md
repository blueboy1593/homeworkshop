## Problem 1

*변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 구분 하시오.*

mutable:

list, set, dictionary

immutable:

string, tuple, range

## Problem 2

*range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.*

```python
aa = list(range(50))
result = aa[1:50:2]
print(result)
```

## Problem 3

*반 학생들의 정보를 이용하여 key는 이름, value는 나이인 딕셔너리를 만드시오.*

```python
import random
age = list(range(20,30))
print(age)
dict = {}
name_list = ['강희원', '김정', '조성원', '김수민', '신영훈', '박권응', '백민주', '임건혁', '정승원', '양희철', '김은성', '김혜준', '김현화', '김강현', '김혜련', '윤성민','김주홍','이신호','이인동','윤가영','하지수','공정배','신지영','박재성']
print(name_list)

for i in name_list:
    dict[i] = random.choice(age)
print(dict)
```

