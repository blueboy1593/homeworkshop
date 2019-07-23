# 06 HOMEWORK

## Problem 1

*Python은 객체 지향 프로그래밍 언어입니다. Python에서 기본적으로 정의되어 있는 클래스 5가지만 작성하시오.*

1. str

2. list

3. dict

4. int

5. float

   

## Problem 2

*다음 매직 메서드의 역할을 간단하게 작성하시오.*

```
• __init__
생성될 때 자동으로 호출되는 메서드
• __del__
소멸될 때 자동으로 호출되는 메서드
• __str__
print 안에 넣으면 호출되는 메서드
• __repr__
그냥 호출하면 나오는 메서드
```



## Problem 3

*아래 코드의 ‘.sort()’와 같이 문자열, 리스트, 딕셔너리 등을 조작할 때 사용하였던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드 3가지를 그 역할과 함께 작성하시오.*

```python
numbers = [5, 1, 2]
numbers.sort()
print(numbers) # [1, 2, 5]
```

```python
.split()
a = '가 나 다 라 마 바 사'
print(a.split())
결과 : ['가', '나', '다', '라', '마', '바', '사']
# 띄어쓰기한 string을 띄어쓰기 칸을 기준으로 list로 구분해준다.
```

```python
.append()
list = []
list.append('사과')
list.append('오렌지')
print(list)
['사과', '오렌지']
# 리스트에 항목을 추가하는 메서드이다.
```

```python
.values()
dict = {'집': '좋은곳', '멀캠': 'ㅎㅎ...'}
print(dict.values())
dict_values(['ㅎㅎ...', '좋은곳'])
# 딕셔너리의 value값을 추출하는 메서드이다.
```