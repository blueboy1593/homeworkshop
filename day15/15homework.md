# 15homework

## Problem1

*Django에서는 특정 html을 보여주기 위하여 views.py에서 render 함수를 사용한다. 아래의 이미지와 같은 페이지를 보여주려고 할 때, 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.*

```html
<h1>Hello, {{ name }} !</h1>
```

```python
def hello(request, name):
    context = {
            (a)     ,
    }
    return render(  (b)  , 'hello.html', (c)  )
```

a) 'name' = 'name'

b) request

c) context

## Problem2

*Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 앱 폴더 안의 ____(a)____ 폴더 내부를 탐색합니다. (a)에 들어갈 폴더 이름을 작성하시오.*

a) templates

