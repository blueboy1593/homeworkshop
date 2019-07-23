# 06 WORKSHOP

*아래와 같은 클래스 Circle이 있을 때, 반지름이 3이고 x, y 좌표가 (2, 4)인 원을 만들어 넓이와 둘레를 출력하시오.*

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0 
    r = 0
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
won = Circle(3,2,4)
# 넓이 출력
print(won.area())
# 둘레 출력
print(won.circumference())
# 중심점의 좌표
print(won.center())
```

```
$ python 06workshop.py
28.259999999999998
18.84
(2, 4)
```

프린트 결과가 나온 모습이다.

Class에서 반지름, x좌표, y좌표를 입력하여 출력하였다.