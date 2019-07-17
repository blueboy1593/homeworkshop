# 7/17 Homework, function

## 문제1

*Python에서 기본으로 사용할 수 있는 Built in function 5개를 찾아서 작성하세요.*

```python
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

## 문제2

*다음과 같이 함수가 정의되어 있다. 보기 중, 오류가 발생하는 코드를 고르시오.*

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
    
# 1 작동한다. location과 name이 명시적으로 제시되었기 때문.
ssafy(location='대전', name='철수')
# 2 작동한다. name에 길동이 대체되었고, location은 따로 명시해주었다.
ssafy('길동', location='광주')
# 3 오류가 난다. 앞에서 name을 명시해준 상태에서 뒤에서 location을 따로 명시해주지 않으면 안된다.
ssafy(name='허준', '구미')
```

```
 def ssafy(name, location='서울'):
...     print(f'{name}의 지역은 {location}입니다.')
>>> ssafy(location='대전', name='철수')
철수의 지역은 대전입니다.
>>> ssafy('길동', location='광주')
길동의 지역은 광주입니다.
>>> ssafy(name='허준', '구미')
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

positional argument follows keyword argument 라는 오류가 난다.

## 문제3

*다음과 같이 코드가 작성되어 있을 때, 변수 result에 저장된 값을 작성하시오.*

```python
def my_func(a,b):
    c = a + b
    print(c)

result = my_func(4,7)
```

```
>>> def my_func(a,b):
...     c = a + b
...     print(c)
...
>>> result = my_func(4,7)
11
```

my_func(a,b)라는 함수를 통하여 result의 값은 4 + 7로 저장된다.





