# 07 homework

## Problem 1

*인스턴스 메서드, 스태틱 메서드, 클래스 메서드에 해당 하는 함수가 무엇인지 작성하시오.*

```python
class Calculator:
    count = 0
    
    # 인스턴스 메서드
    def info(self):
        print('나는 계산기 입니다.')
    
    # 스태틱 메서드
    @staticmethod
    def add(a,b):
        Calculator.count += 1
        print(f'{a} + {b} 는 {a + b} 입니다.')
        
    # 클래스 메서드
    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')
```

## Problem 2

*각각의 함수(메서드)를 실행하는 코드를 작성하시오.*

```python
calc = Calculator()
calc.info()
calc.add(2,4)
calc.add(1,9)
calc.history()

$ python 07hw.py
나는 계산기 입니다.
2 + 4 는 6 입니다.
1 + 9 는 10 입니다.
총 2번 계산 했습니다.
```

## Problem 3

*파라미터 self와 cls에는 어떤 값이 할당 되는지 작성하시오.*

self에는 인스턴스 메서드를 통한, class 주체의 instance객체의 정보가 할당된다.

cls에는 클래스 메서드를 통해 class 객체의 정보가 할당된다.