# 08workshop

## Problem 

*Flask에서 Dictionary 자료형을 이용하여 다음 조건을 만족하는 ‘나만의 영어 단어장’ 페이지를 만들어보세요*

```python
from flask import flask

@app.route('/dictionary/<string:word>')
def dictionary(word):
    work_book = {
        'apple': 'apple은 사과',
        'banana': 'banana는 바나나'
    }

    if word in work_book:
        result = work_book[word]
    else:
        result = f'{word}는 단어장에 없습니다!'

    return result
```





