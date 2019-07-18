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