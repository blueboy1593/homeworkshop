# Day5 workshop

## Problem 1

```python
# 파일명 : calc.py

def sum1(x, y):
    return x + y

def sub1(x, y):
    return x - y

def mul1(x, y):
    return x * y

def div1(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('"0"으로 나누려고 하는 경우에는 문자열 "0"으로는 나눌 수 없습니다.')
    
```

4가지의 사칙연산을 구현한 모습이다.

try/except는 수업 시간에 배우고 시도하기로 했다.

except 뒤에는 에러명을 붙여서 처리해줄 수 있다.

```python
import calc

print(calc.sum1(10, 5))
print(calc.sub1(10, 5))
print(calc.mul1(10, 5))
print(calc.div1(10, 5))
print(calc.div1(10, 0))
```

실행파일의 코드이다. 0으로 나누어도 처리가 된다.

```
$ python 05execute.py
15
5
50
2.0
"0"으로 나누려고 하는 경우에는 문자열 "0"으로는 나눌 수 없습니다.
None
```

결과가 나온 모습이다.

