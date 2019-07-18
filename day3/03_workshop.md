# 7/17 Workshop, about function

## Problem 1

*Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다.
따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.*

*단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는
함수 palindrome(word)를 만들어보세요.*

```python
user_word = input("단어를 입력하세요 : ")

def palindrome(user_word):
    len_word = len(user_word)
    list_word = list(user_word)
    for i in range(int(len_word/2)):
        if list_word[i] != list_word[-1-i]:
            return 'False'
        else:
            return 'True'
print(palindrome(user_word))
```

```
student@M702 MINGW64 ~/development/homeworkshop/day3 (master)
$ python 03_review.py
단어를 입력하세요 : 00700
True

student@M702 MINGW64 ~/development/homeworkshop/day3 (master)
$ python 03_review.py
단어를 입력하세요 : abeshit
False
```



Code by 신영훈

```python
def palindrome(word):
    return True if list(word) == list(reversed((word))) else False
# reversed 사용.
```

Code by Jason

```python
def palidrome(word):
    return word == word[::-1]

# 슬라이싱을 거꾸로 하는 것. 
```





