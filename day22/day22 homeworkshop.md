# day22 homeworkshop

## Workshop

### model.py 파일

```python
class Person(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(
        max_length=100,
        validators=[EmailValidator(message='이메일 형식에 맞지 않습니다.')]
        )
    age = models.IntegerField(
        validators=[MinValueValidator(19, message="미성년자는 노노에요")]
    )
```

### admin.py 파일

```python
from django.contrib import admin
from .models import Person

admin.site.register(Person)
```

### Superuser 생성

```bash
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'student'): 김강현
이메일 주소: snb0303@naver.com
Password:
Password (again):
Error: Blank passwords aren't allowed.
Password:
Password (again):
비밀번호가 이메일 주소와 너무 유사합니다.
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Homework

1. Django Model Validator 는 Database 에 저장될 값이 정해진 조건에 맞지 않으면 특정
   오류를 발생시켜 값이 저장되지 않도록 한다 . 이 때 발생하는 오류가 어떠한 오류인지
   작성하시오

  [`ValidationError`](https://docs.djangoproject.com/en/2.2/ref/exceptions/#django.core.exceptions.ValidationError) 

2. 공식 문서를 통해 Django 의 Bulit in Validator 에는 어떤 것들이 있는지 찾아 3 가지 이상
   작성하시오

### `RegexValidator`

### `EmailValidator`

이메일 형식이 맞는지 검출하는 Validator

### `URLValidator`

URL 형식이 맞는지 검출하는 Validator

