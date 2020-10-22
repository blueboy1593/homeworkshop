# 13 workshop

## Problem

1. 이름이 ‘classroom’인 프로젝트를 생성하시오.

2. ‘/info’의 주소로 접속했을 때, 다음과 같이 반의 정보를 보여주는 페이지를 만드시오.

3. /student/<학생이름>’의 주소로 접속했을 때, 다음과 같이 학생의 이름과 나이를 보여주는 페이지를 만들어 주세요.

![workshop](C:\Users\student\development\homeworkshop\day13\workshop.JPG)

앞서 배운 setting 방법을 통해 세팅 완료하였다.

```python
from django.shortcuts import render

# Create your views here.

def info(request):
    return render(request, 'info.html')


def student(request, stu_name):
    context={
        'stu_name' : stu_name,
    }
    return render(request, 'student.html', context)
```

views.py에 해당하는 코드.

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info),
    path('student/<str:stu_name>', views.student),
]

```

urls.py에 해당하는 코드

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Info</title>
</head>
<body>
  <h1>우리반정보</h1>
  <br>
  <h2>Teacher</h2>
  <ul>
    <li>NAME</li>
  </ul>
  <h2>Student</h2>
  <ul>
    <li>김강현</li>
    <li>정승원</li>
    <li>김혜준</li>
  </ul>
</body>
</html>
```

info.html의 코드이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <h1>이름: {{ stu_name }}</h1>
  <h2>나이 : 28</h2>
</body>
</html>
```

student.html의 코드이다.

