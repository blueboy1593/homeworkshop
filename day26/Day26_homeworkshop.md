# Day26_homeworkshop

## homework

1. 로그인을 한 사용자만 게시물을 작성할 수 있도록 코드를 작성하려고 한다 . 아래의 빈
   칸 (a), ( 에 들어갈 코드를 작성하시오

```python
from django.contrib.auth.decorators import login_required
@login_required
```

2. Article 모델에 사용자 정보가 담긴 모델과 1:N 관계를 형성하기 위한 칼럼을 추가하려
   고 한다 . 아래의 빈 칸 (a), ( 에 들어갈 코드를 작성하시오

```python
from django.conf import settings
settings.AUTH_USER_MODEL
```

## workshop

아래의 회원가입 페이지는 Django.contrib.auth.forms 모듈의 UserCreationForm 클래스를 활용한 것이다 . 아래와 같은 페이지를 만들기 위하여 views.py 와 template(signup) 에 작성하여야 하는 코드를 작성하시오.

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
        
    else:  
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/form.html', context)
```

```django
<form method = "post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">회원가입</button>
```

