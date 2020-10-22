# 14workshop

*다음은 임의의 숫자를 입력할 수 있는 Form과, 해당 Form으로부터 넘어온 숫자를 받아 보여주는 2개의 View를 나타낸 것이다. 아래 이미지를 참고하여 ‘urls.py’, ‘views.py’, ‘templates(html)’를 작성하시오.*

## urls.py

```python
urlpatterns = [
    path('pushnumber', views.pushnumber),
    path('pullnumber', views.pullnumber),
]
```

## views.py

```python
def pushnumber(request):
    return render(request, 'pushnumber.html')


def pullnumber(request):
    num = request.GET.get('number')
    context = {
        'num' : num,
    }
    return render(request, 'pullnumber.html', context)
```

## pushnumber.html

```django
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>Push Number</h1>
  <form action="/pullnumber">
    <input type="number" name="number" value="123">
    <button type="submit">Push!</button>
  </form>
</body>
</html>
```

## pullnumber.html

```django
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1><b>Pull Number</b></h1>
  <h1>Pull 해보니 {{ num }}입니다!</h1>
</body>
</html>
```

