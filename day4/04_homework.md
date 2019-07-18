# 04 Homework data structure

## Problem1

*Python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.*

1. Local scope: 정의된 함수

2. Enclosed scope: 상위 함수

3. Global scope: 함수 밖의 변수 혹은 import된 모듈

4. Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

위와 같은 순서로 접근하게 된다.

## Problem2

*다음 중 옳지 않은 것을 고르시오.
(1) 함수는 오직 하나의 객체만 반환할 수 있어서, ‘return a, b’처럼 쓸 수 없다.
(2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 인자(parameter)는 함수를 선언할 때 설정한 값이며, 인수(argument)는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 인자 앞에* **을 붙이고, 이 때는 함수 내에서 tuple로 처리된다.*

1) False

```python
def hamsu():
    return a, b
```

를 입력해도 오류나지 않는다.

2) True

3) True

4) True

## Problem3

*재귀 함수를 쓰는 장점과 단점을 작성하시오.*

for문과 비교했을때 재귀 함수는 동작 속도가 더 느릴 때도 많다. 하지만, 경우에 따라서 for문 대신 재귀 함수를 사용하면 직관적으로 알고리즘을 표현하기가 쉬울 때가 있고, 제 3자로 하여금 해석을 편하게 할 수 있기도 한다. 보통 점화식 형태의 알고리즘에서는 재귀함수를 사용하면 좋다.













