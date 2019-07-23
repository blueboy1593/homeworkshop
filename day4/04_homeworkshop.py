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


print('math.sqrt : \t', math.sqrt(17))
print('my_sqrt : \t', my_sqrt(17))