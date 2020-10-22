# Day28 homeworkshop

## homework

1. 위키피디아에서 설명하고 있는 인터넷에 있는 자원을 나타내는 유일한 주소는 a 이다 . a 는 b 와 (c) 두 종류가 있다 . b 는 네트워크상에서 자원이 어디 있는지를 알려주기 위한 규약으로 웹 사이트 주소 뿐만 아니라 다양한 프로토콜 FTP /Telnet 등 에서도 활용된다 . 빈칸 (a), (b), (c) 에 들어갈 용어를작성하시오.

```
a) URI (Uniform Resource Identifier)
b) URL
c) URN
```

2. REST 는 Representational Transfer 의 약자로 자원의 표현을 하기 위한 아키텍처 중 하나이다 . 장점 중에 하나로 HTTP 프로토콜 인프라를 그대로 사용한다 . 즉 , (a) 를 통해 자원을 명시하고 , (b) 를 통해 자원에 대한 동작을 나타낸다 . 빈칸 (a), (b) 에 들어갈 용어를 작성하시오.

```
a) URI
b) HTTP method
```

3. SSAFY 회원 정보가 있는 API 를 구조화 하였을 때 , 1 반 ( 의 3 번 학생 ( 을
   나타내는 URL 예시를 작성하시오

```
http://127.0.0.1:8000/api/v1/classes/1/students/3
```

## workshop

일반적인 REST API 에서 게시글 ( 에 대한 각각의 CRUD 에 대응되는 HTTP Methods 와 URL 을 작성하시오.

```
get - http
post - http
```

```
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
```

