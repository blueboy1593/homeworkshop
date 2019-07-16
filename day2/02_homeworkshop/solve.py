print('hello world')


aa = list(range(50))
result = aa[1:50:2]
print(result)

n = 5
m = 9
for i in range(m):
    for j in range(n):
        print('*', end = '')
    print(' ')

som = 0 # 합을 명시
ave = 0 # 평균점수
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
for value in student.values():
    som += value
people_num = len(student)
ave = som/people_num
print(f'평균 점수는 {ave}점입니다!')

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

import random
age = list(range(20,30))
print(age)
dict = {}
name_list = ['강희원', '김정', '조성원', '김수민', '신영훈', '박권응', '백민주', '임건혁', '정승원', '양희철', '김은성', '김혜준', '김현화', '김강현', '김혜련', '윤성민','김주홍','이신호','이인동','윤가영','하지수','공정배','신지영','박재성']
print(name_list)

for i in name_list:
    dict[i] = random.choice(age)
print(dict)