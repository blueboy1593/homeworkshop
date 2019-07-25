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

calc = Calculator()
calc.info()
calc.add(2,4)
calc.add(1,9)
calc.history()