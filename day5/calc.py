
def sum1(x, y):
    return x + y

def sub1(x, y):
    return x - y

def mul1(x, y):
    return x * y

def div1(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('"0"으로 나누려고 하는 경우에는 문자열 "0"으로는 나눌 수 없습니다.')
    