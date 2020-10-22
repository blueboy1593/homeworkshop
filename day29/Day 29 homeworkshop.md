# Day 29 homeworkshop

## homework

1. HTTP 상태 코드에서 200 ok 는 요청에 대해 성공적으로 수행하였음을 나타낸다
   아래의 HTTP 응답 코드의 의미를 작성하시오
   404 - 오브젝트를 가져오지 못했을 때
   405 - 포스트를 잘 못 받았을 때
   500 - 내부 서버 오류

2.  Django 모델에서 지정된 레코드에 값이 없을 때 , 404 에러를 표시하도록 하는 shortcut
   함수와 해당 함수를 import 하는 코드를 작성하시오

   ```python
   from django.shortcuts import get_object_or_404
   ```

   

3. 아래의 설명 중 REST API 설계 기본 규칙에 어긋난 것을 고르시오
   1)
   필요한 경우 자원에 CRUD 동사 표현이 들어갈 수 있다 O
   2)
   자원은 대문자보다 소문자를 사용한다 X
   3)
   URL 에 HTTP Method 를 사용하지 않는다 X
   4)
   자원간의 연관 관계가 있는 경우 ‘/articles/1/ 와 같이 작성한다 O
   5)
   URL 에서 변하는 부분은 ‘/ int:article_pk 와 같이 유일한 값이다 X



## workshop

아래의 두 코드에 적절한 데코레이터를 사용하여 허용되지 않은 HTTP Method 로 요청
이 들어왔을 경우 405 Method Not Allowed 상태 코드를 반환하도록 하는 코드를 작성
하시오

```python
return HttpResponse('405 Method Not Allowed', status=405)
```

