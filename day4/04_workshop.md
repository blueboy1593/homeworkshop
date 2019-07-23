# 04 Workshop data structure

## Problem

*양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수를 작성하세요. (sqrt() 사용 금지)*

```python
x= 20
b = 1
while (b ** 2) < x: # a를 제곱하고 비교하여 제곱근의 정수부분 구하기
    b += 1
a = b - 1
print(a,b)

def banban(a,b):
              
    if ((a+b)/2) ** 2 >= x:
        return (((a+b)/2), b)
    elif ((a+b)/2) ** 2 < x:
        return (a, ((a+b)/2))

banban(4,5)
```



Code by Jason 강사님

```python
import math
# 이분법으로 제곱근 구하기

def my_sqrt(n):
    x, y = 1, n
    result = 1 # 우리가 추측ㅎ하는 제곱근 result
    
    while abs(result ** 2 - n) > 0.0000001:
        result = (x + y)/2
        if result ** 2 < n:
            x = result
        else:
            y = result
            
return result            

print('math.sqrt : \t', math.sqrt(3))
print('my_sqrt : \t', my_sqrt(3))
```

