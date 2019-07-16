# Homework Day 1

## 1번 문제

```python
import keyword
print(keyword.kwlist)
```

False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

위의 예약어는 사용할 수 없다.

## 2번 문제

```python
# 1. abs와 e 사용 자연로그함수와 비교해서 맞은걸로 쳐줘라.
a = 0.1 * 3
b = 0.3
abs(a - b) <= 1e-10
# 2. sys를 import 함수를 따로 사용한다.
import sys
abs(a - b) <= sys.float_info.epsilon
# 3. math.isclose 이런 형식의 함수가 따로 있다.
import math
math.isclose(a, b)
```

## 3번 문제

```python
\n # 줄 바꿈
\t # 탭 생성
\\ # 빽슬래시를 출력하는 것.
```

## 4번 문제

````python
# 1. f string
name = "철수"
print(f'안녕, {name}아')
# 2. % 
print("안녕, %s야" % name)
# 3. str.format()
print('안녕, {}야'.format(name))
````

## 5번 문제

5번.

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-83e77f7140cb> in <module>
----> 1 int ('3.5')

ValueError: invalid literal for int() with base 10: '3.5'
```

다음과 같은 에러가 뜬다.







