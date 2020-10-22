# 16workshop

## Problem

1. 자신의 반에 있는 사람들의 데이터를 저장하는 Student Model을 models.py에
작성하시오. Student Model이 가져야 할 필드는 다음과 같습니다.
2. 모델 마이그레이션 작업을 수행한 후, Admin 페이지에서 주변 학생 3명의 정보를
삽입하시오.
3. 정보를 삽입한 후, Admin 페이지에서 학생들의 목록을 보기 쉽게 만들기 위하여
‘__str__’ 메소드를 작성하여 name이 출력되도록 하시오.

### Model.py

```python
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    birthday = models.DateField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}의 생일은 {self.birthday}, 그리고 나이는 {self.age}' 
```

![sqlite capture](C:\Users\student\development\homeworkshop\day16\sqlite capture.JPG)

### admin.py

```python
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birthday', 'age', 'created_at', 'updated_at',)
```







