# Day2 Workshop

## Problem 1

*두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(*'*') 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 사각형을 출력하시오.

```python
n = 5
m = 9
for i in range(m):
    for j in range(n):
        print('*', end = '')
    print(' ')
# print(' ') 자리에 ' ' 대신 '\n'이 들어가게 되면 줄이 한번 더 변한다.    
```

## Problem2

*과목명과 점수가 담긴 딕셔너리가 있을 때, 평균 점수를 출력하시오.*

```python
som = 0 # 합을 명시
ave = 0 # 평균점수
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum(student.values())
351
for value in student.values():
    som += value
people_num = len(student)
ave = som/people_num
print(f'평균 점수는 {ave}점입니다!')
```

## Problem3

*다음은 여러 사람의 혈액형(A, B, AB, O)에 대한 데이터이다. 반복문을 사용하여 key는 혈액형의 종류, value는 인원 수인 딕셔너리를 만들고 출력하시오.*

```python
# 각 혈액형 인원의 숫자.
numA = 0
numB = 0
numO = 0
numAB = 0
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
for i in blood_types:
    if i == 'A':
        numA = numA + 1
    elif i == 'B':
        numB = numB + 1
    elif i == 'O':
        numO = numO + 1
    elif i == 'AB':
        numAB = numAB + 1
result_dict = {'A': numA, 'B': numB, 'O': numO, 'AB': numAB}
print(result_dict)
```









