# 07 workshop

*아래와 같은 Animal 클래스가 있을 때, 해당 클래스를 상속 받아 아래 보기와 같이 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.*

```python
class Animal:
   def __init__(self, name):
       self.name = name
   def walk(self):
       print(f'{self.name}! 걷는다!')
   def eat(self):
       print(f'{self.name}! 먹는다!')
    
class Dog(Animal):
    def walk(self):
        print(f'{self.name}! 달린다!')
    def run(self):
        print(f'{self.name}! 달린다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')
    
dog = Dog('바둑이')
dog.walk()
dog.run()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```

```
>>> dog = Dog('바둑이')
>>> dog.walk()
바둑이! 달린다!
>>> dog.run()
바둑이! 달린다!

>>> bird = Bird('구구')
>>> bird.walk()
구구! 걷는다!
>>> bird.eat()
구구! 먹는다!
>>> bird.fly()
구구! 푸드덕!
```

실행 코드와 python 프로그램을 통해 나온 결과이다.