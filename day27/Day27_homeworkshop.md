# Day27_homeworkshop

## homework

1. attachment 컬럼에 파일을 저장하려고 한다 . 아래의 빈 칸 ( 에 정의해야 하는 field 를
   작성하시오

```python
Filefield()
```

2. 사용자가 업로드한 파일이 저장되는 위치를 Django 프로젝트 폴더 내부의
   uploaded_files 로 지정하고자 한다 . 이 때 , settings.py 에 작성해야 하는 설정 2 가지와
   이것이 의미하는 바를 간략하게 작성하시오

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploaded_files')
# django.com/media/사용자가 업로드한 파일 경로
MEDIA_URL = '/media/'
```

3. 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더
   내부의 ‘/ 에 있다 . 이 폴더 안에 Static 파일이 있다 라고 Django 프로젝트에게
   알려주기 위하여 settings.py 에 작성해야 하는 설정을 작성하시오

```python
STATIC_URL = '/static/'

STATIC_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]
```

## workshop

```html
{% load static %}
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap-reboot.min.css' %}">
  <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap-grid.min.css' %}">
  <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
  
  <title>{% block title %}{% endblock title %}</title>
</head>
<body>
  <header>
    <h1>저희 페이지에 오신 것을 환영합니다.</h1>
    {% if user.is_authenticated %}
    <p>
     <span>Hello, {{ user.username }}</span>
     <a href="{% url 'accounts:logout' %}">[로그아웃]</a>
     <form action="{% url 'accounts:delete' %}" method="post">
      {% csrf_token %}
      <button type="submit">회원탈퇴</button>
     </form>
     <br>
     <a href="{% url 'articles:index' %}">[목록]</a>
    </p>
    {% else %}
      <p>
        <a href="{% url 'accounts:login' %}">[로그인]</a>
        <a href="{% url 'accounts:signup' %}">[회원가입]</a>
      </p>
    {% endif %}
  </header>
  <nav></nav>
  {% block container %}{% endblock container %}
  <footer></footer>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="{% static 'bootstrap/js/bootstrap.bundle.min.js' %}"></script>
  <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script>
</body>
</html>
```

