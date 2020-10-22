# 21 Homeworkshop

## Workshop

*투표를 위한 설문 앱을 만들려고 한다. 이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇 표를 받았는지 기록하는 기능을 가지고 있다. 설문 앱은 Question 모델과 Choice 모델로 구성되어 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 형성하고 있다.*

*Question 하나를 보여주는 페이지에서 Choice를 위의 오른쪽 그림과 같이 출력하려고 한다. HTML 파일에 아래와 같은 코드가 작성되어 있다고 할 때, Choice의 내용과 투표수를 출력하는 코드를 작성하시오.*

```django
{% for choice in choices %}
<li>
  {{ choice.content }} : {{ choice.vote }}
</li>
```

## Homework

1. Question 모델과 Comment 모델이 1:N 관계를 형성하고 있을 때, 하나의 Question을 보여주는 페이지에서 Comment를 모두 보여주려고 한다. 다음과 같은 detail.html 파일 이 있을 때, 모든 Comment의 content를 h3 태그를 이용하여 출력하는 for문을 작성하 시오. (단, related_name은 설정하지 않았다고 가정한다.)

```django
{% for choice in choices %}
<li>
  {{ choice.content }} : {{ choice.vote }}
</li>
```

2. 다음과 같은 urls.py 파일이 있을 때, comment를 작성하는 폼을 만들기 위하여 form 태그 안에 action 속성값으로 넣어야 하는 경로를 작성하시오.

```django
<form action="{% url 'questions:comments_create' article.pk %}" method="POST">
```

