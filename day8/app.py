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
