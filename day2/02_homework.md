## Problem 1

*변경할 수 있는(mutable) 것과 변경 불가능한 것(immutable)을 구분 하시오.*

mutable:

list, set, dictionary

set은 for문으로 가져올 수 있다.

```python
>>> my_set = {3, 1, 6, 9, 1, 3}
>>> my_set
{1, 3, 6, 9}
>>> my_set[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> my_set(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not callable
>>> my_set{2}
  File "<stdin>", line 1
    my_set{2}
          ^
SyntaxError: invalid syntax
>>> list(my_set[1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> for i in my_set:
...     print(i)
...
1
3
6
9
```

```python
>>> my_dict = {
...     '짬뽕': '11', '짜장': 2
... }
>>> my_dict
{'짬뽕': '11', '짜장': 2}
>>> my_dict['짬뽕'] = 10
>>> my_dict
{'짬뽕': 10, '짜장': 2}
>>>
```



immutable:

string, tuple, range

```python
>>> x = 'Hello World'
>>> print(x[0])
H
>>> print(x[3])
l
>>> x[1] = t
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 't' is not defined
```

```python
>>> my_tuple = (1, 2, 3)
>>> my_tuple[0]
1
>>> my_tuple[0] = 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
    
>>> my_range = range(5)
>>> my_range
range(0, 5)
>>> my_range[2]
2
>>> my_range[4]
4
>>> my_range[4] = 6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'range' object does not support item assignment
```

직접 파이썬에서 해보면 답이 나온다.

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

list[-1]을 하면 마지막 인덱스를 보여준다.