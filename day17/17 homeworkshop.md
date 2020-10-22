# 17 homeworkshop

## workshop

1. 학생들의 이름과 나이를 저장하기 위한 Form Class를 정의하려고 한다. 다음과 같이 Student Model이 존재할 때, 해당 Model에 데이터를 입력하기 위하여 가장 적절한 Form Class인 StudentForm Class를 작성하시오.

```python
class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label='이름',
        widget=forms.TextInput(
            attrs={
                'placeholder': '이름이 뭐에요?',
            }
        ),
    )
    age = forms.IntegerField(
        label='나이',
    )
```

2. views.py의 코드가 다음과 같을 때, new.html에서 위에서 만든 Form Class를 활용하여 Form Tag가 보여지도록 하는 코드를 작성하시오. (사용자가 데이터를 입력하고 Submit 버튼을 누르면 ‘/students/create/’로 요청을 보내며, method는 POST 방식을 사용한다.)

```django
{% extends 'base.html' %}
{% block title %}크리에이뜨create{% endblock title %}
{% block body %}
<h1>새로운 아티클 생성</h1>
<a href="{% url 'students:index' %}">[Back]</a>
<hr>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">생성하기</button>
</form>
{% endblock body %}
```



## homework

1. Django Form Class를 만들 때, Django에 내장되어 있는 모듈을 import 하고 해당 모듈 에 정의된 Class를 상속받아야 한다. 해당 모듈을 import 하는 코드를 작성하시오.

```python
from django import forms
from .forms import ArticleForm
이런식으로 작성한다.
```

2. Form Class를 Template에서 활용하기 위해서 변수 form에 Form Class의 인스턴스를 할당하여 Template으로 전달하였다. Template에서 <p> Tag로 감싸진 form을 렌더링 하기 위한 코드를 작성하시오.

```python
'DIRS': [os.path.join(BASE_DIR, 'myform', 'templates')],
```

3. Form Class를 활용할 때, Form에 담긴 데이터가 유효한지 체크하기 위해서 is_valid() 메소드를 활용하였다. 유효성 검사를 통과한 후, 유효한 데이터를 가져오기 위하여 빈칸 (a)에 들어가야하는 코드를 작성하시오. (단, StudentForm Class는 forms.Form을 상속 받았다고 가정한다.)

```python
cleaned_data
```

