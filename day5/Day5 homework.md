



# 05 homework

## Problem 1

![def](C:\Users\student\development\homeworkshop\day5\def.png)

*위와 같은 코드가 fibo.py 파일에 작성되어 있을 때, 아래와 같이 함수를
실행할 수 있도록 하는 import 구문을 (A), (B), (C)를 채워 넣어 완성하시오.*

```python
from fibo.py import fibo_recursion as recursion
```



## Problem2

*다음 에러들이 어떠한 경우에 발생하는지 간단하게 작성하시오.*

ZeroDivisionError

```
ZeroDivisionError: division by zero
```

0으로 나누기를 하였을 때 발생.

NameError

```
NameError: name 'abc' is not defined
```

지역 혹은 전역 이름 공간내에서 유효하지 않은 이름, 즉 정의되지 않은 변수를 호출 하였을 경우 이름 공간에 없어서 못 찾아서 나는 에러이다.

TypeError

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

타입을 맞지 않게 사용하였을 때 발생하는 에러.

IndexError

```
IndexError: list index out of range
```

리스트에서 인덱스를 잘못 짚었을 때 나는 에러.

KeyError

```
KeyError: 'queen'
```

Dictionary에서 key를 잘못 사용할때 나는 에러이다.

ModuleNotFoundError

```
ModuleNotFoundError: No module named 'reque'
```

모듈을 찾을 수 없는 경우, 그리고 잘못된 모듈을 호출했을 때

ImportError

```
ImportError: cannot import name 'BS' from 'bs4' (c:\users\student\appdata\local\programs\python\python37\lib\site-packages\bs4\__init__.py)
```

bs4에서 BS를 추출하지 못할 때.